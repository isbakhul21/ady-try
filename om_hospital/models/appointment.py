from odoo import  api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("TOMBOL DI KLIK cok ")
        sales_order_ids = self.env['sale.order'].sudo().search([])
        for product in sales_order_ids:
            print(product.order_line.order_id.id)
            print(product.order_line.mapped('price_unit'))

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    ref = fields.Char(string='Reference')
    gender = fields.Selection(tracking=True, related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    pharmamcy_line_ids = fields.One2many("appointment.pharmacy.line", "appointment_id", string="Pharmacy Lines")
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')], string="Priority"
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In_consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="Status", default='draft', required=True
    )
    doctor_id = fields.Many2one("res.users", string="Doctor", tracking=True)

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_in_done(self):
        for rec in self:
            rec.state = 'done'

    def action_in_cancel(self):
        for rec in self:
            rec.state = 'cancel'





class AppointmentPharmacyLine(models.Model):
    _name = "appointment.pharmacy.line"
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one("product.product", required=True)
    price_unit = fields.Float(string="Price", related="product_id.list_price")
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")











