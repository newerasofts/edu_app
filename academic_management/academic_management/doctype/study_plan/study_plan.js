frappe.ui.form.on("Study Plan", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
