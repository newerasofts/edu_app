import frappe

def install_demo_data():
    programs = [
        {"doctype":"Academic Program","code":"CS-MSC","program_name":"ماجستير علوم الحاسب","degree":"ماجستير","college":"كلية الحوسبة","department":"قسم علوم الحاسب","status":"نشط"},
        {"doctype":"Academic Program","code":"ED-PHD","program_name":"دكتوراه أصول التربية","degree":"دكتوراه","college":"كلية التربية","department":"قسم أصول التربية","status":"نشط"},
    ]
    for row in programs:
        if not frappe.db.exists("Academic Program", row["code"]): frappe.get_doc(row).insert(ignore_permissions=True)
    committees = ["الدراسات العليا والمخططات","الإرشاد الأكاديمي","الجودة","الخطط والبرامج"]
    for idx, name in enumerate(committees,1):
        code=f"COM-{idx:02d}"
        if not frappe.db.exists("Committee", code): frappe.get_doc({"doctype":"Committee","code":code,"committee_name":name,"is_active":1}).insert(ignore_permissions=True)
    frappe.db.commit()
    return "تم تحميل البيانات التجريبية"
