frappe.ui.form.on("Supervision Assignment", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
