app_name = "academic_management"
app_title = "Academic Management"
app_publisher = "Academic Management Team"
app_description = "Graduate studies management and decision support"
app_email = "admin@example.edu"
app_license = "MIT"

scheduler_events = {
    "daily": [
        "academic_management.api.alerts.evaluate_capacity_alerts",
        "academic_management.api.alerts.evaluate_supervision_alerts",
    ]
}

fixtures = [
    {"dt": "Role", "filters": [["name", "in", ["Academic Administrator", "Dean", "Department Head", "Committee Member", "Academic Advisor", "Graduate Student"]]]},
    {"dt": "Workflow", "filters": [["document_type", "in", ["Academic Status Log", "Committee Decision"]]]},
]
