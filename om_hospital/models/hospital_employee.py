from odoo import  api, fields, models

class HospitalEmployee(models.Model):
    _name = "hospital.employee"
    _description = "Hospital Employee"

    id = fields.Char(string="id")
    nip = fields.Char(string="nip")
    nik = fields.Char(string="nik")
    name = fields.Char(string="name")
