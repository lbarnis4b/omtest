from odoo import api, fields, models, tools, _

class Module(models.Model):
	_name = "ir.module.module"
	_inherit = "ir.module.module"

	license = fields.Selection(selection_add=[
	('S4BPL', 'Soft4Biz Private Licence'),
	('S4BCRD', 'Soft4Biz Client Request Development'),
	('S4BERD', 'Soft4Biz Exclusive Request Development')])

