import frappe
from frappe.tests.utils import FrappeTestCase

from india_banking.india_banking.doc_events.bank_account import validate_ifsc_code


class TestBankAccountIFSC(FrappeTestCase):
	def test_blank_ifsc_is_allowed(self):
		validate_ifsc_code(frappe._dict(branch_code=None))
		validate_ifsc_code(frappe._dict(branch_code=""))

	def test_valid_ifsc_passes(self):
		validate_ifsc_code(frappe._dict(branch_code="ICIC0002408"))

	def test_invalid_ifsc_is_rejected(self):
		with self.assertRaises(frappe.ValidationError):
			validate_ifsc_code(frappe._dict(branch_code="ALANDUR"))
