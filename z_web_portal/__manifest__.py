{
    "name": "[Custom] Portal",
    "summary": "Responsive web client, community-supported",
    "description": "This module contains all the common features of Portal.",
    "version": "1.0.0",
    'category': 'Sales',
    "license": "LGPL-3",
    "depends": ['base','sale'],
    "data": [
        # security


        # report


        # data


        # views
        'views/portal_template.xml',
        'views/web_asset.xml',
        'views/portal_recure.xml',


        # data

    ],
    "sequence": 1,
    'installable': True,
    'auto_install': False,
    'application': True,
}
