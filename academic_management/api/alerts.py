import frappe

@frappe.whitelist()
def evaluate_capacity_alerts():
    alerts=[]
    for row in frappe.get_all("Admission Cycle", fields=["name","program","accepted","capacity"]):
        if row.capacity and row.accepted >= row.capacity * 0.9:
            alerts.append({"type":"capacity","record":row.name,"message":f"البرنامج {row.program} اقترب من الطاقة الاستيعابية"})
    return alerts

@frappe.whitelist()
def evaluate_supervision_alerts():
    return frappe.db.sql("""
        SELECT f.name, f.full_name, f.max_supervision, COUNT(s.name) active_supervisions
        FROM `tabFaculty Member` f LEFT JOIN `tabSupervision Assignment` s
        ON s.faculty_member=f.name AND s.status='قيد التنفيذ'
        GROUP BY f.name HAVING active_supervisions > f.max_supervision
    """, as_dict=True)
