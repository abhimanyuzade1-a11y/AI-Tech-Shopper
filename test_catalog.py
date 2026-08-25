from products import products


print()
print("======================================")
print("       AI SHOPPER PRODUCT CATALOG")
print("======================================")


categories = {}


for product in products:

    category = product["category"]

    if category not in categories:

        categories[category] = 0

    categories[category] += 1


for category, count in categories.items():

    print(
        f"{category}: {count} products"
    )


print()
print(
    "Total products:",
    len(products)
)