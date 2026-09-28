frappe.ui.form.on("Course Offering", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
