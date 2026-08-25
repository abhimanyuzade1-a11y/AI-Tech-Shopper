# =========================================================
# AI PERSONAL TECH SHOPPER
# END-TO-END COMMERCE FLOW
# =========================================================

from cart_manager import CartManager

from checkout import CheckoutManager


print()

print(
    "=========================================="
)

print(
    "      🤖 AI COMMERCE JOURNEY"
)

print(
    "=========================================="
)

print()


# =========================================================
# CUSTOMER
# =========================================================

print(
    "👤 CUSTOMER"
)

print(
    "I want a laptop for AI and gaming."
)

print()


# =========================================================
# AGENT RECOMMENDATION
# =========================================================

laptop = {

    "name":
        "ApexBook Pro 15",

    "price":
        74999

}


print(
    "🤖 AGENT"
)

print(

    f"I recommend "
    f"{laptop['name']}."

)

print(

    f"Price: ₹{laptop['price']:,}"

)

print()


# =========================================================
# NEGOTIATION
# =========================================================

discount = 3000


print(
    "👤 CUSTOMER"
)

print(
    "Can you give me a discount?"
)

print()


print(
    "🤖 AGENT"
)

print(

    f"I can offer you "
    f"₹{discount:,} off."

)

print()


# =========================================================
# ADD TO CART
# =========================================================

cart = CartManager()


cart.add_product(

    laptop,

    quantity=1,

    discount=discount

)


print(
    "🛒 PRODUCT ADDED TO CART"
)

print()


# =========================================================
# ADD ACCESSORY
# =========================================================

mouse = {

    "name":
        "HyperMouse G1",

    "price":
        2499

}


cart.add_product(

    mouse,

    quantity=1,

    discount=200

)


print(
    "🎁 ACCESSORY ADDED"
)

print(
    mouse["name"]
)

print()


# =========================================================
# CART SUMMARY
# =========================================================

summary = cart.get_summary()


print(
    "=========================================="
)

print(
    "             🛒 CART"
)

print(
    "=========================================="
)

print()


print(

    "Subtotal:",

    f"₹{summary['subtotal']:,}"

)


print(

    "Discount:",

    f"₹{summary['discount']:,}"

)


print(

    "Total:",

    f"₹{summary['total']:,}"

)


print()


# =========================================================
# CHECKOUT
# =========================================================

checkout = CheckoutManager(

    cart

)


result = checkout.prepare_checkout()


print(
    "=========================================="
)

print(
    "             💳 CHECKOUT"
)

print(
    "=========================================="
)

print()


if result["success"]:

    print(
        "✅ Cart validated"
    )


    print(

        "Amount Payable:",

        f"₹{result['total']:,}"

    )


    print()

    print(
        "🟢 CHECKOUT READY"
    )


else:

    print(
        "❌ Checkout failed"
    )


    for error in result["errors"]:

        print(
            "•",
            error
        )


print()

print(
    "=========================================="
)

print(
    "       ✅ COMMERCE FLOW COMPLETE"
)

print(
    "=========================================="
)