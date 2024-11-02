from odoo import api, fields, models, _


class EmployeeReimburse(models.Model):

    _name = "employee.reimburse"
    _rec_name = "z_name"

    @api.onchange('z_name','z_customer')
    def get_name_for_buttoijo_customer(self):
        print("ONCHANGE JALAN")
        for this in self:
            if this.z_name == 1 or this.z_name == '1':
                this.z_customer = 'OKEE DATA MASUK'
            else:
                this.z_customer = 'Data Ngga Masuk'

    # Field untuk generate URL attachment sebagai string list
    z_document_url_list = fields.Text(string="Document URLs", compute='_compute_document_urls')

    @api.depends('z_document_return_ids')
    def _compute_document_urls(self):
        for record in self:
            if record.z_document_return_ids:
                urls = []
                for attachment in record.z_document_return_ids:
                    url = '/web/content/%s?download=false' % attachment.id
                    urls.append(url)
                record.z_document_url_list = ','.join(urls)
            else:
                record.z_document_url_list = ''

    z_name = fields.Char(string="Description")
    z_customer = fields.Char(string="Customer")

    z_category = fields.Many2one('category.reimbursement',string="Category")
    z_group = fields.Many2one('group.reimbursement',string="Golongan")

    z_document_return_ids = fields.Many2many('ir.attachment',relation='employee_reimburse_document_return_ids_rel',string='Document')

    z_document_urls = fields.Char(string="Document URLs", compute=_compute_document_urls)



    @api.model
    def action_preview(self):
        # Method ini tidak perlu mengembalikan apa pun, karena preview akan ditangani oleh JavaScript
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ir.attachment',
            'views': [(False, 'form')],
            'target': 'new',
        }

    def action_test_anything(self):
        print('HELOO TEST ANTYHIN')
        contract_ids = self.env['res.contract'].sudo().search([('z_journal_id', '!=', False),('z_state', 'not in', ('closed', 'cancel'))])
        print('mapped', contract_ids.sudo().mapped('z_name'))
        print('sorted', contract_ids.sudo().sorted(lambda x : x.create_date, reverse=False))
        print('filtered OKE',contract_ids.sudo().filtered(lambda x : x.z_partner_id.id == 78))
        print('filtered', len(contract_ids.sudo().filtered(lambda x : x.z_partner_id.id == 78)))







