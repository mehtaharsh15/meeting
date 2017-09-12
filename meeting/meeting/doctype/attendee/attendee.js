// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendee', {
	refresh: function(frm) {

	},
	validate: function (frm) {
		if (frm.doc.date_of_birt > get_today()) {
       	 	msgprint("BOD shold less than Today");
        	validated = false;
    	}
	}
});
