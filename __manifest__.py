{
    'name': 'EState',
    'version': '0.1.0',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'The state module',
    'description': 'This is a module of test',
    'website': 'https://viraweb123.ir',
    'depends': [
        'base',
    ],
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',

        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}