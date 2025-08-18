# test_data_users.py

# ✅ Valid Test Data
valid_user = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": "221B Baker Street",
    "phone": "9876543210"
}

# ❌ Invalid Test Data

# Missing required field: name
invalid_user_missing_name = {
    "email": "john.doe@example.com",
    "address": "221B Baker Street",
    "phone": "9876543210"
}

# Invalid email format
invalid_user_invalid_email = {
    "name": "John Doe",
    "email": "not-an-email",
    "address": "221B Baker Street",
    "phone": "9876543210"
}

# Invalid phone format (not 10 digits)
invalid_user_invalid_phone = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": "221B Baker Street",
    "phone": "12345"
}

# Missing all required fields
invalid_user_missing_all = {}

# ⚠️ Edge Case Test Data

# Empty strings for required fields
edge_case_empty_fields = {
    "name": "",
    "email": "",
    "address": "",
    "phone": ""
}

# Extra unexpected field (age not defined in model)
edge_case_extra_field = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": "221B Baker Street",
    "phone": "9876543210",
    "age": 30
}
