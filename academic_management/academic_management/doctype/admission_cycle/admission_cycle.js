frappe.ui.form.on("Admission Cycle", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
