from odoo import api, fields, models, _
from datetime import datetime, date, timedelta
from odoo.exceptions import AccessError, UserError, ValidationError


class OwlTodoList(models.TransientModel):
    _name = "owl.todo.list"
    _description = "Owl Todo List"
    _order = "id desc"

    name = fields.Char(string='Name')
    color = fields.Char(string='color')
    completed = fields.Boolean(string='completed')

