# -*- coding: utf-8 -*-
{
    'name': "Reporte custom de ventas",
    'summary': """Agrega un diseño predeterminado de los reportes de las ventas.""",
    'description': """Agrega un diseño predeterminado de los reportes de las ventas.""",

    'author': "DGV",
    # 'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': 1,
    'application': True,

    'depends': ['sale'],
    
    'assets': {
        'web.report_assets_common': [
            'sales_quotes_report_custom/static/src/css/fonts.css',
        ],
    },
    
    'data': [
        'views/custam_report_sale_template.xml',
    ],
}