from tools import search_products


results = search_products(
    category="Smartphone",
    max_price=50000
)


print()
print("======================================")
print("       SMARTPHONE SEARCH")
print("======================================")


for product in results:

    print(
        f"{product['name']} "
        f"→ ₹{product['price']:,}"
    )


print()
print(
    "Smartphones found:",
    len(results)
)