frappe.ui.form.on("Committee Decision", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
