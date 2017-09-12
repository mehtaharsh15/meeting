// Copyright (c) 2017, SBK and contributors
// For license information, please see license.txt

cur_frm.add_fetch("attendee", "full_name", "full_name");

frappe.ui.form.on('Meeting', {
	refresh: function(frm) {

	}
});
