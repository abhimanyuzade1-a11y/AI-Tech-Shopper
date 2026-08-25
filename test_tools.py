from tools import (
    search_products,
    check_stock,
    compare_products,
    recommend_accessories,
    get_product_details
)


# ==========================================
# TEST SEARCH
# ==========================================

print("===== SEARCH TOOL =====")

results = search_products(
    category="Laptop",
    max_price=80000,
    use_case="Gaming"
)

for product in results:

    print(
        product["name"],
        "₹",
        product["price"]
    )


# ==========================================
# TEST STOCK
# ==========================================

print("\n===== STOCK TOOL =====")

stock = check_stock(
    "ApexBook Pro 15"
)

print(stock)


# ==========================================
# TEST COMPARISON
# ==========================================

print("\n===== COMPARE TOOL =====")

comparison = compare_products(
    [
        "ApexBook Pro 15",
        "Titan Gaming 16"
    ]
)

for product in comparison:

    print(
        product["name"],
        "₹",
        product["price"]
    )


# ==========================================
# TEST ACCESSORIES
# ==========================================

print("\n===== ACCESSORY TOOL =====")

accessories = recommend_accessories(
    ["Gaming", "AI/ML"]
)

for product in accessories:

    print(
        product["name"],
        "₹",
        product["price"]
    )


# ==========================================
# TEST DETAILS
# ==========================================

print("\n===== DETAILS TOOL =====")

details = get_product_details(
    "ApexBook Pro 15"
)

print(details)