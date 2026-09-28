frappe.ui.form.on("Teaching Load", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
