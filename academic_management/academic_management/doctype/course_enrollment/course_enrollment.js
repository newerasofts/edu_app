frappe.ui.form.on("Course Enrollment", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
