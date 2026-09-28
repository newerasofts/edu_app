import frappe
from frappe.utils import flt

@frappe.whitelist()
def get_dashboard_metrics():
    """مؤشرات تنفيذية موحدة للوحة التخطيط."""
    return {
        "students": frappe.db.count("Graduate Student", {"current_status": "منتظم"}),
        "programs": frappe.db.count("Academic Program", {"status": "نشط"}),
        "faculty": frappe.db.count("Faculty Member"),
        "waitlisted": frappe.db.count("Waitlist Entry", {"status": "انتظار"}),
        "expected_graduates": frappe.db.count("Graduate Student", {"expected_graduation_term": ["!=", ""]}),
        "open_decisions": frappe.db.count("Committee Decision", {"status": ["in", ["مقترح", "قيد التنفيذ", "متأخر"]]}),
    }

@frappe.whitelist()
def get_program_demand():
    rows = frappe.db.sql("""
        SELECT program, SUM(applicants) applicants, SUM(accepted) accepted,
               SUM(capacity) capacity, ROUND(SUM(accepted)/NULLIF(SUM(applicants),0)*100,1) acceptance_rate
        FROM `tabAdmission Cycle` GROUP BY program ORDER BY applicants DESC
    """, as_dict=True)
    return rows

@frappe.whitelist()
def get_course_demand():
    return frappe.db.sql("""
        SELECT co.course, c.course_name, COUNT(ce.name) demand,
               MAX(co.capacity) capacity, (COUNT(ce.name) - MAX(co.capacity)) gap
        FROM `tabCourse Enrollment` ce
        JOIN `tabCourse Offering` co ON co.name = ce.offering
        JOIN `tabCourse` c ON c.name = co.course
        WHERE ce.status = 'مسجل'
        GROUP BY co.course, c.course_name ORDER BY demand DESC LIMIT 10
    """, as_dict=True)
