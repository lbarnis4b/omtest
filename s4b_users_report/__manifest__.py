# -*- coding: utf-8 -*-
{
	'name': "Licensed users reports",

	'summary': """
			Sends reports with licensed users""",

	'author': "Soft4Biz",
	'website': "http://soft4biz.ro",
	'category': 'Uncategorized',
	'version': '15.0.2.0.0',
	'license': "LGPL-3",
	

	# any module necessary for this one to work correctly
	'depends': [
		'base',
		],

	# always loaded
	'data': [
		'data/email.xml',
		'views/users_views.xml',
		'views/company_views.xml',
	],

	'installable': True,
	'auto_install': False,
	'application': False,
}