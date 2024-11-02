from odoo.http import request, Response
from odoo import http
from datetime import datetime, date, timedelta
import json

headers_json = {'Content-Type': 'application/json'}


class Controller(http.Controller):

    @http.route('/api-employee-reimburse', auth='none', methods=['GET'], csrf=False)
    def api_employee_reimburse(self, **kwargs):

        datas = []
        employees = request.env['hr.employee'].sudo().search([])
        for employee in employees:
            datas.append({'name': employee.name})
        return Response(json.dumps(datas), headers=headers_json)
