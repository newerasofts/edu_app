frappe.ui.form.on("Academic Program", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
