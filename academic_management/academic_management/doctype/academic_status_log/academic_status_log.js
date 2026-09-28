frappe.ui.form.on("Academic Status Log", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
