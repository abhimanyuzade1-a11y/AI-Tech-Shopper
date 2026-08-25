customer = {
    "name": "Demo Customer",
    "budget": 80000,
    "category": "Laptop",
    "requirements": [
        "AI/ML",
        "Gaming",
        "Programming"
    ],
    "priorities": {
        "performance": 5,
        "battery": 3,
        "price": 4
    }
}


def show_customer_profile():
    print("===== CUSTOMER PROFILE =====")
    print("Name:", customer["name"])
    print("Budget: ₹", customer["budget"])
    print("Category:", customer["category"])
    print("Requirements:", ", ".join(customer["requirements"]))


show_customer_profile()