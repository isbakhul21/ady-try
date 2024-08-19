from odoo import api, fields, models, _


class CategoryReimbursement(models.Model):

    _name = "category.reimbursement"
    _rec_name = "z_name"

    z_name = fields.Char(string="Name",tracking=True)