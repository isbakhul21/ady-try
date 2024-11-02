from odoo import  api, fields, models
from odoo.tools.safe_eval import  safe_eval

class PlaygroundSpace(models.Model):
    _name = "playground.space"
    _description = "Playground Space"
    _rec_name = "custom_name"

    DEFAULT_ENV_VARIABELS = """"""


    model_id = fields.Many2one('ir.model', string='Model')
    code = fields.Text(string='Code', default=DEFAULT_ENV_VARIABELS)
    result = fields.Text(string='Result')
    custom_name = fields.Char(string='Custom Name', default='')



    def result_code(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
            self.result = safe_eval(self.code.strip(), {'self': model})
        except Exception as e:
            self.result = str(e)
