
{
    'name': "om_tasks",

    'summary': """""",

    'description': """""",

    'author': "Khodary",

    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['sale'],

    'data': [
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'report/sale_report_inherit.xml',
    ],

    'demo': [],
}
