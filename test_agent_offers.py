from agent_brain import run_agent


print()
print(
    "======================================"
)

print(
    "      🤖 AI COMMERCE AGENT"
)

print(
    "======================================"
)


result = run_agent(

    "I need a laptop for AI and gaming "
    "under 80000"

)


# =========================================================
# CUSTOMER
# =========================================================

print()

print(
    "👤 CUSTOMER"
)

print(
    "Category:",
    result["customer"]["category"]
)

print(
    "Budget:",
    f"₹{result['customer']['budget']:,}"
)


# =========================================================
# RECOMMENDATION
# =========================================================

print()

print(
    "🏆 RECOMMENDATION"
)


if result["winner"]:

    print(
        "Product:",
        result["winner"]["name"]
    )

    print(
        "Price:",
        f"₹{result['winner']['price']:,}"
    )


# =========================================================
# SMART OFFER
# =========================================================

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


if result["offer"]:

    offer = result["offer"]


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
# BUNDLE
# =========================================================

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


if result["bundle"]:

    bundle = result["bundle"]


    for item in bundle["items"]:

        print(

            f"{item['name']} "
            f"— ₹{item['price']:,}"

        )


    print()

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


# =========================================================
# DECISION TRACE
# =========================================================

print()

print(
    "======================================"
)

print(
    "        🤖 AGENT TRACE"
)

print(
    "======================================"
)


for step in result["trace"]:

    print(
        "→",
        step
    )