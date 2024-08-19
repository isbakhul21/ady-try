from odoo import api, fields, models, _


class EmployeeReimburse(models.Model):

    _name = "employee.reimburse"
    _rec_name = "z_name"

    z_name = fields.Char(string="Description")

    z_category = fields.Many2one('category.reimbursement',string="Category")
    z_group = fields.Many2one('group.reimbursement',string="Golongan")
