{
    'name': 'Subcontractors Module',
    'version': '1.0',
    'summary': 'MOdule to manage the Subcontractors',
    'description': 'A module to receive sub contractors data and process it',
    'category': 'Apps',
    'author': 'Fairchoice for CRM',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'views/subcontractor_view.xml',
        'views/menu.xml',
        # 'views/webhook_log_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
}
