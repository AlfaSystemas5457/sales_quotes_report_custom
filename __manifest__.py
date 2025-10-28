# -*- coding: utf-8 -*-
{
    'name': "Reporte custom de ventas",
    'summary': """Agrega un diseño predeterminado de los reportes de las ventas.""",
    'description': """Agrega un diseño predeterminado de los reportes de las ventas.""",

    'author': "DGV",
    'website': "https://github.com/AlfaSystemas5457/sales_quotes_report_custom",

    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': 1,
    'application': False,

    'depends': ['sale'],

    'data': [
        'views/custam_report_sale_template.xml',
        'views/view_assets.xml',
    ],
}
