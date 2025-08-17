# Valid order
valid_order = {
    "user_id": "60c72b2f9b1d8a5f08a9c123",
    "items": ["60c72b2f9b1d8a5f08a9c456"],  # just item IDs
    "total": 2400,
    "status": "pending"
}

# Invalid orders
invalid_order_missing_user = {
    "items": [
        {"item_id": "60c72b2f9b1d8a5f08a9c456", "quantity": 2}
    ],
    "total_price": 2400
}

invalid_order_empty_items = {
    "user_id": "60c72b2f9b1d8a5f08a9c123",
    "items": [],
    "total_price": 0
}
