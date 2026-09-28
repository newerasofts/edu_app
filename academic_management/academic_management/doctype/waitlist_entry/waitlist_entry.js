frappe.ui.form.on("Waitlist Entry", {
    refresh(frm) {
        frm.set_df_property("language", "hidden", 1);
    }
});
