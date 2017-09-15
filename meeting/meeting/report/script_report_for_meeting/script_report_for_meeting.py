# Copyright (c) 2013, SBK and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = ["Name:Data:100"]+["Date:Date:100"]+["Subject:Data:120"]+["attendee:Data:120"]+["full_name:Data:120"]
	

	query="""select tabMeeting.name, meeting_date, subject, attendee, full_name 
			from tabMeeting, `tabAttendee Table` """
	
	from_date = filters.get("from_date")
	to_date = filters.get("to_date")

	query += " where meeting_date between '{0}' and '{1}'".format(from_date,to_date)

	data = frappe.db.sql(query,as_list=1,debug=1)


	return columns, data
