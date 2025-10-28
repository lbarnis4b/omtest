# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, date, timedelta

class Company(models.Model):
	_inherit = "res.company"

	user_reports_active = fields.Boolean(string='User reports active',default=True)
	user_reports_address = fields.Char(string='User reports address',default='office@soft4biz.ro')

	@api.model
	def licensed_users_report(self):
		companies = self.env['res.company'].search([('user_reports_active','=',True)])
		#su_id = self.env['res.partner'].browse(SUPERUSER_ID)
		#su_id = self.env['res.users'].browse([('login','=','admin')])
		#template_id = self.env['ir.model.data'].get_object_reference('s4b_users_report','users_report')[1]
		#template_browse = self.env['mail.template'].browse(template_id)
		if not companies:
			return True
		for company in companies:
			users_to = company.user_reports_address
			licensed_users = self.env['res.users'].search([('licensed_user','=',True)])
			if not licensed_users:
				break
			count = 0
			today = date.today()
			for user in licensed_users:
				count += 1
			body_html = _('<body> \
						<h2 align="center">Licensed Users Report for ' + company.name + '</h2> \
						<p>Date: ' + str(today) + '</p> \
						<p><strong>Total licensed users: ' + str(count) + '</strong></p> \
						<div> \
							<style> \
								table, th, td { \
									border : 1px solid black; \
									border-collapse : collapse; \
									padding : 5px; \
								} \
							</style >\
							<table style="border : 1px solid black;">\
								<tr> \
									<th>#</th>\
									<th>Description</th>\
									<th>User</th> \
									<th>Last login</th> \
								</tr>')
			index = 0
			for user in licensed_users:
				index += 1
				body_html += '<tr> \
								<td>' + str(index) + '</td> \
								<td>' + user.name + '</td> \
								<td>' + user.login + '</td> \
								<td>' + str(user.login_date) + '</td> \
								</tr>'
			body_html += '</div> \
						  </body>'

			values = {
				'email_to' : users_to,
				'email_from' : "admin@soft4biz.ro",
				'subject' : _('Users Report'),
				'body_html' : body_html
			}
		
			mail_obj = self.env['mail.mail']
			template_id = mail_obj.create(values)
			mail_obj.send(template_id)

		return True
