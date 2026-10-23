import frappe


def execute():
	"""Undo the mandatory Bank Account fields that older installs created.

	Foreign and credit-card accounts have no IFSC, email or mobile number.
	IFSC is enforced when a payment payload is built instead.
	"""
	frappe.db.delete(
		"Property Setter",
		{"doc_type": "Bank Account", "field_name": "branch_code", "property": "reqd"},
	)
	for fieldname in ("email", "currency"):
		frappe.db.set_value(
			"Custom Field", {"dt": "Bank Account", "fieldname": fieldname}, "reqd", 0
		)
	frappe.db.set_value(
		"Custom Field",
		{"dt": "Bank Account", "fieldname": "mobile_number"},
		"mandatory_depends_on",
		"",
	)
	frappe.clear_cache(doctype="Bank Account")
