frappe.ui.form.on("Course", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
