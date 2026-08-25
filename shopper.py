from products import products


def search_products(category, max_price, use_case=None):
    results = []

    for product in products:
        if product["category"].lower() == category.lower():

            if product["price"] <= max_price:

                if use_case is None or use_case in product["use_cases"]:
                    results.append(product)

    return results


# Test 1: Gaming laptops
print("===== GAMING LAPTOPS =====")

results = search_products("Laptop", 80000, "Gaming")

for product in results:
    print(product["name"], "₹", product["price"])


# Test 2: Smartphones under ₹50,000
print("\n===== SMARTPHONES =====")

results = search_products("Smartphone", 50000)

for product in results:
    print(product["name"], "₹", product["price"])


# Test 3: Gaming accessories
print("\n===== GAMING ACCESSORIES =====")

results = search_products("Accessory", 5000, "Gaming")

for product in results:
    print(product["name"], "₹", product["price"])