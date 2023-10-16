{
    'name': 'Codilar expense forcast',
    'version': '15.0.1.1.0',
    'sequence': -100,
    'description': """
        This module is expense sheet
        """,

    'author': "Thanveer",
    'company': 'Codilar Technology',
    'maintainer': 'Codilar Technology',
    'website': "https://www.codilar.com",
    'depends': ['project', 'hr_timesheet', 'account','hr_expense','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/expense_type.xml',
        'views/inherit_hr_expense.xml',

    ],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
