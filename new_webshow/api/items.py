import frappe

@frappe.whitelist(allow_guest=True)
def get_all_items():
    """
    Public API to retrieve all active items
    """
    return frappe.get_all(
        "Item",
     
        fields=[
            "name",
            "item_code",
            "item_name",
            "item_group",
            "stock_uom",
            "is_stock_item",
            "standard_rate",
            "description",
            "image"
        ],
        order_by="modified desc"  
    )