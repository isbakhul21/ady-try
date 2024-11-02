from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class CustomPortalLogin(AuthSignupHome):

    @http.route('/web/login', type='http', auth="public", website=True)
    def web_login(self, redirect=None, **kw):
        response = super(CustomPortalLogin, self).web_login(redirect=redirect, **kw)

        if request.env.user.has_group('base.group_portal'):
            custom_page = request.env.user.custom_page_url
            if custom_page:
                return request.redirect(custom_page)

        return response

class CustomPortalPages(http.Controller):

    @http.route('/my/page/1', type='http', auth="user", website=True)
    def portal_page_1(self, **kw):
        if request.env.user.has_group('base.group_portal') and request.env.user.custom_page_url == '/my/page/1':
            return request.render('om_hospital.portal_page_1')
        else:
            return request.redirect('/my')

    @http.route('/my/page/2', type='http', auth="user", website=True)
    def portal_page_2(self, **kw):
        if request.env.user.has_group('base.group_portal') and request.env.user.custom_page_url == '/my/page/2':
            return request.render('om_hospital.portal_page_2')
        else:
            return request.redirect('/my')
