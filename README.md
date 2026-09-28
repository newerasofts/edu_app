# Academic Management — Frappe App

تطبيق Frappe مخصص لإدارة الدراسات العليا (ماجستير ودكتوراه) ودعم لجان الدراسات العليا والتخطيط والجودة.

## النطاق
- البرامج والمسارات والطاقة الاستيعابية والقبول وقوائم الانتظار.
- الطلبة والحالات الأكاديمية والخطط الدراسية والمقررات المطروحة.
- أعضاء هيئة التدريس والعبء التدريسي والإشراف العلمي.
- اللجان الأكاديمية ومحاضر الاجتماعات والقرارات ومتابعة التنفيذ.
- مؤشرات لوحة التخطيط عبر API آمن قابل للاستخدام من Desk أو واجهة مخصصة.

## التثبيت داخل Bench
```bash
bench get-app academic_management /path/to/academic_frappe
bench --site your-site install-app academic_management
bench --site your-site migrate
```

> تم إعداد التطبيق وفق بنية Frappe القياسية. يحتاج التشغيل الكامل إلى Bench مع MariaDB/Redis/Node حسب إصدار Frappe المستهدف.

## بيانات تجريبية
```bash
bench --site your-site execute academic_management.setup.install_demo_data
```

## API مؤشرات اللوحة
- `academic_management.api.dashboard.get_dashboard_metrics`
- `academic_management.api.dashboard.get_program_demand`
- `academic_management.api.dashboard.get_course_demand`

## ملاحظات الإصدار الأول
هذه نسخة أساس عملية (MVP) تضع النموذج العلاقي، الـ DocTypes، الصلاحيات، التقارير، ونقاط التكامل. يمكن توصيلها لاحقًا بنظام القبول والموارد البشرية والمالية عبر REST/Webhooks.
