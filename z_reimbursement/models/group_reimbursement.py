from odoo import api, fields, models, _


class GroupReimbursement(models.Model):

    _name = "group.reimbursement"
    _rec_name = "z_group"

    z_group = fields.Char(string="Name",tracking=True)
    z_amount_limit_reimburse = fields.Float(string="Limit Reimburse",tracking=True)