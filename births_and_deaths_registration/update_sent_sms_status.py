from __future__ import unicode_literals

import six
from six import string_types

import frappe
from frappe import _, msgprint, throw
from frappe.model.document import Document
from frappe.utils import nowdate

@frappe.whitelist()
def update_ready_for_payment(ref_doctype, ref_name):
	frappe.db.set_value(ref_doctype, ref_name, 'ready_for_payment', 1)


@frappe.whitelist()
def update_approved(ref_doctype, ref_name):
	frappe.db.set_value(ref_doctype, ref_name, 'approved', 1)


