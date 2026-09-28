frappe.ui.form.on("Graduate Student", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
