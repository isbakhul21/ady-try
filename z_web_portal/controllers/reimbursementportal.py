import logging

from odoo.addons.mail.controllers.mail import MailController
from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)


class ReimbursementPortal(http.Controller):

    @http.route('/my/testtable', type='http', csrf=False, auth='public', website=True)
    def getMenuModuleTable(self, **kw):
        print("MENUUU")

        sale_order_id = request.env['sale.order'].sudo().search([])

        return request.render("z_web_portal.portal_web_reimburse", {
            'sale_order_table': sale_order_id,
        })


    @http.route('/my/menumodule', type='http', csrf=False, auth='public', website=True)
    def getMenuModule(self, **kw):
        print("MENUUU")
        return request.render("z_web_portal.menu_view_module")

    @http.route('/my/pagereimburse', type='http', csrf=False, auth='public', website=True)
    def getFormReimburse(self, **kw):
        print("PAGE REIMBURSE ONNN!!!")
        employee_type_selection = request.env['hr.employee']._fields['z_type_employee'].selection
        return request.render("z_web_portal.custom_form_template")

    def action_button_from_fe(self):
        print("HALLLLOOOOO")

    @http.route('/my/thankyoupage', type='http', csrf=False, auth='public', website=True)
    def getPageThankYou(self):
        print("Thankyou")
        return request.render('z_web_portal.thank_you_template')

    @http.route('/my/submit', type='http', csrf=False, auth='public', website=True)
    def submitReimbursement(self, **post):
        # Extract data from form submission
        nip = post.get('NIP')
        customer = post.get('Customer')
        print('customer : ', customer)

        # Create a new record in the employee.reimburse model
        reimbursement = request.env['employee.reimburse'].sudo().create({
            'z_name': nip,
            'z_customer': customer,
        })

        print(f"Reimbursement created: {reimbursement}")

        # Redirect to the thank you page
        return request.redirect('/my/thankyoupage')

