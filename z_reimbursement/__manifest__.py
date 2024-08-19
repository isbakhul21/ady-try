{
    "name": "[Custom] Reimburstment",
    "summary": "Responsive web client, community-supported",
    "description": "This module contains all the common features of Portal.",
    "version": "1.0.0",
    'category': 'Reimbursement',
    "license": "LGPL-3",
    "depends": ['z_base'],
    "data": [
        # security
        'security/ir.model.access.csv',


        # report




        # views
        'views/reimbursement.xml',
        'views/group_reimbursement.xml',
        'views/category_reimbursement.xml',

        # data
        'data/ir_ui_menu.xml',
    ],
    "sequence": 1,
    'installable': True,
    'auto_install': False,
    'application': True,
}
