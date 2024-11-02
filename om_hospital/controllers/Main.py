from odoo.http import request, Response
from odoo import http
# from datetime import datetime, date, timedelta
# import json


class Hospital(http.Controller):


    @http.route('/hospital/patient', methods=['POST'], auth='none', csrf=False)
    def hospital_patient_crud(self, name, age, **kw):
        print("1")
        check_existing_data = request.env['hospital.patient'].sudo().search([('name','=',name)])
        print("Checking Done")
        if not name or not age:
            return "Maaf data yang anda masukan ngga ada name atau age nya"

        if check_existing_data:
            check_existing_data.write({'age': int(age)})
            print("data updated")
        else:

            patient_data = {
                'name': name,
                'age': int(age),
            }
            print(patient_data)

            request.env['hospital.patient'].sudo().create(patient_data)
            print("data berhasil dibuat")

        return "Patient Flow Process  Success"
