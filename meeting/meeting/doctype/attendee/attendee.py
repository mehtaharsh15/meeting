# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Attendee(Document):
	def validate(self):
		self.age = 25
		self.create_user()

	def create_user(self):
		user = frappe.new_doc("User")
		user.email = self.email
		user.first_name = self.full_name
		user.save(ignore_permissions=True)
		frappe.msgprint("New user is created")