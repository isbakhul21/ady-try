{
    "name": "[Custom] Reimburstment",
    "summary": "Responsive web client, community-supported",
    "description": "This module contains all the common features of Portal.",
    "version": "1.0.0",
    'category': 'Reimbursement',
    "license": "LGPL-3",
    "depends": ['z_base','z_management_equipment','z_contract','web'],
    "data": [
        # security
        'security/ir.model.access.csv',


        # report




        # views
        'views/reimbursement.xml',
        'views/group_reimbursement.xml',
        'views/category_reimbursement.xml',
        'views/rab_loan.xml',
        'views/rab_loan_product.xml',
        'views/todo_list.xml',
        # 'views/res_partner.xml',

        # data
        'data/ir_ui_menu.xml',
    ],
    "sequence": 1,
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
            'web.assets_backend': [
                'z_reimbursement/static/src/components/*/*.js',
                'z_reimbursement/static/src/components/*/*.xml',
                'z_reimbursement/static/src/components/*/*.scss',



                # 'z_reimbursement/static/src/xml/preview_attachment.js',
                # 'z_reimbursement/static/src/xml/preview_attachment.js',
            ],
        },
}
