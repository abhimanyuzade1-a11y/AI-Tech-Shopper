from products import products

from ai_brain import understand_request

from comparison import (
    compare_two_products,
    explain_product,
    recommendation_reason
)


# =========================================================
# CUSTOMER
# =========================================================

message = (
    "I need a laptop for AI and gaming "
    "under 80000"
)


customer = understand_request(
    message
)


print()
print("======================================")
print("        CUSTOMER REQUIREMENTS")
print("======================================")

print(
    "Category:",
    customer["category"]
)

print(
    "Budget:",
    customer["budget"]
)

print(
    "Requirements:",
    customer["requirements"]
)


# =========================================================
# FIND LAPTOPS
# =========================================================

laptops = []


for product in products:

    if product["category"] == "Laptop":

        if product["price"] <= customer["budget"]:

            laptops.append(product)


# =========================================================
# COMPARE FIRST TWO
# =========================================================

if len(laptops) >= 2:

    product1 = laptops[0]
    product2 = laptops[1]


    result = compare_two_products(
        product1,
        product2,
        customer
    )


    print()
    print("======================================")
    print("             COMPARISON")
    print("======================================")


    print()
    print(
        product1["name"],
        "→",
        result["score1"],
        "/100"
    )


    print(
        product2["name"],
        "→",
        result["score2"],
        "/100"
    )


    # Winner

    print()

    if result["winner"]:

        print(
            "🏆 Better Match:",
            result["winner"]["name"]
        )


    # =====================================================
    # EXPLANATION
    # =====================================================

    print()
    print("======================================")
    print("          WHY THIS PRODUCT?")
    print("======================================")


    reasons = recommendation_reason(
        result["winner"],
        customer
    )


    for reason in reasons:

        print(
            "✓",
            reason
        )

else:

    print(
        "Not enough products to compare."
    )