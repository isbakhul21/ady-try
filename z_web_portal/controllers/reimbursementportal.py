import logging

from odoo.addons.mail.controllers.mail import MailController
from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)


class ReimbursementPortal(http.Controller):

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
        name = post.get('name')
        age = int(post.get('age', 0))
        email = post.get('email')

        if age < 16:
            # Jika umur kurang dari 16, kirim pesan kesalahan
            return request.render('z_web_portal.custom_form_template', {
                'error_message': "Anda harus berumur 16 tahun atau lebih untuk mengirim form ini."
            })

        # Create a new record in the employee.reimburse model
        reimbursement = request.env['employee.reimburse'].sudo().create({
            'z_name': name,
            'z_age': age,
            'z_email': email,
        })

        print(f"Reimbursement created: {reimbursement}")

        # Redirect to the thank you page
        return request.redirect('/my/thankyoupage')

