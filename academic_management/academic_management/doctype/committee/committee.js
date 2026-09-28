frappe.ui.form.on("Committee", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
