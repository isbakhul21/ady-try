from odoo import  api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    custom_page_url = fields.Char(string="Custom Page URL")
