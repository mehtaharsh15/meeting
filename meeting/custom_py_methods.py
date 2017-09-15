import frappe
from frappe.utils import flt,rounded,money_in_words
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _
from erpnext.hr.doctype.process_payroll.process_payroll import get_month_details
import datetime


def validate_customer(doc,method):
	frappe.msgprint("Hi from custom app")
	frappe.msgprint(doc.customer_name)
	# doc.tax_id = "IN24-1112"

	meeting = frappe.get_doc("Meeting", "08f3a06265")
	# doc.tax_id = meeting.subject + " ABC"
	# doc.full_name
	doc.customer_name = doc.customer_name + meeting.subject

	doc.name = doc.customer_name
	# doc.tax_id = doc.customer_name + doc.customer_type + doc.territory