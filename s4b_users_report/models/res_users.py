# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _

class Users(models.Model):
	_inherit = "res.users"

	licensed_user = fields.Boolean(string="Licensed User",default=True)

	def licensed_on_off(self):
		for user in self:
			user.licensed_user = not user.licensed_user

	# server action, for multiple license change
	def reverse_licensing(self):
		users = self.env['res.users'].browse(self._context.get('active_ids', []))
		for user in users:
			user.licensed_on_off()
