from datetime import date
from odoo import  api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "hospital patient"



    @api.depends('tall','weight_body')
    def _getProportion(self):
        for this in self:
           result = this.tall + this.weight_body
           this.proportion = result

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            print(today)
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
                print(rec.age)
            else:
                rec.age = 1
                print(rec.age)
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        print("function from origin tereksekusi........................... ", vals)
        return super(HospitalPatient, self).create(vals)


    def write(self, vals):
        print("function inherit dieksekusi .................................")
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    name = fields.Char(string='Name')
    ref = fields.Char(string='Reference', default="Reference Ditulis Disini", store=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute=_compute_age, tracking=True, store=True)
    gender = fields.Selection([('male','Male'),('female','Female')],tracking=True, default="female")
    active = fields.Boolean(string="Active", default=True)
    tall = fields.Float(string='Tall')
    weight_body = fields.Float(string='Weight body')
    proportion = fields.Float(string='Proportion' , compute=_getProportion, store=True  )
    image = fields.Image(string="Image", store=True)

    id_payroll = fields.Char(string="id_payroll")
    nip_payroll = fields.Char(string="nip_payroll")
    nik_payroll = fields.Char(string="nik_payroll")
    name_payroll = fields.Char(string="name_payroll")











