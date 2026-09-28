frappe.ui.form.on("Faculty Member", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
