from products import products


def recommend_bundle(main_product, customer_requirements):

    bundle = []

    for product in products:

        if product["category"] != "Accessory":
            continue

        matching_requirements = set(product["use_cases"]) & set(
            customer_requirements
        )

        if matching_requirements:
            bundle.append(product)

    return bundle


customer_requirements = [
    "AI/ML",
    "Gaming",
    "Programming"
]

main_product = products[0]

bundle = recommend_bundle(
    main_product,
    customer_requirements
)

print("===== PERSONALIZED BUNDLE =====")

print()
print("Main Product:")
print(main_product["name"])
print("₹", main_product["price"])

print()
print("Recommended Accessories:")

for product in bundle:
    print(
        "-",
        product["name"],
        "| ₹",
        product["price"]
    )