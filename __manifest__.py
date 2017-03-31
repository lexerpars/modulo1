# -*- coding: utf-8 -*-
{
    'name': "modulo1",

    'summary': """
        Modulo 1 de prueba""",

    'description': """
        Este es un modulo de prueba en odoo 10
    """,

    'author': "rperez",
    'website': "http://www.bavaria.com.gt",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/reportes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}