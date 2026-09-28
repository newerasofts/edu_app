frappe.ui.form.on("Committee Meeting", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
