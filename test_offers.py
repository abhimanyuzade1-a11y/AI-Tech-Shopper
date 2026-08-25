from offers import (
    calculate_discount,
    create_bundle
)


# =========================================================
# DEMO PRODUCT
# =========================================================

product = {

    "name": "ApexBook Pro 15",

    "price": 74999,

    "match_score": 100

}


# =========================================================
# CUSTOMER
# =========================================================

customer = {

    "budget": 80000

}


# =========================================================
# CALCULATE OFFER
# =========================================================

offer = calculate_discount(

    product,

    customer

)


print()
print(
    "======================================"
)

print(
    "        💰 SMART OFFER"
)

print(
    "======================================"
)

print(
    "Original Price:",
    f"₹{offer['original_price']:,}"
)

print(
    "Discount:",
    f"₹{offer['discount']:,}"
)

print(
    "Final Price:",
    f"₹{offer['final_price']:,}"
)

print(
    "Reason:",
    offer["reason"]
)


# =========================================================
# DEMO ACCESSORIES
# =========================================================

accessories = [

    {

        "name": "HyperMouse G1",

        "price": 2499

    },

    {

        "name": "HyperCool X1",

        "price": 1999

    }

]


# =========================================================
# CREATE BUNDLE
# =========================================================

bundle = create_bundle(

    product,

    accessories

)


print()
print(
    "======================================"
)

print(
    "        📦 SMART BUNDLE"
)

print(
    "======================================"
)


for item in bundle["items"]:

    print(

        f"{item['name']} "
        f"— ₹{item['price']:,}"

    )


print(
    "Original Total:",
    f"₹{bundle['original_total']:,}"
)

print(
    "Bundle Discount:",
    f"₹{bundle['bundle_discount']:,}"
)

print(
    "Bundle Total:",
    f"₹{bundle['final_total']:,}"
)