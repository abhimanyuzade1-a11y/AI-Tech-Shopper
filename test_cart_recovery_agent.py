from agent_brain import run_agent


print()
print("======================================")
print("       🛒 CART RECOVERY AGENT")
print("======================================")


# =========================================================
# CUSTOMER REQUEST
# =========================================================

message = (
    "I need a laptop for AI and gaming "
    "under 80000"
)


print()
print("👤 CUSTOMER")
print(message)


# =========================================================
# SIMULATE ABANDONED CART
# =========================================================

print()
print("🛒 CUSTOMER ADDED PRODUCT TO CART")


print()
print("⏳ CUSTOMER DID NOT COMPLETE CHECKOUT")


# =========================================================
# RUN AGENT
# =========================================================

result = run_agent(

    message,

    cart_abandoned=True

)


# =========================================================
# RECOMMENDATION
# =========================================================

print()
print("======================================")
print("        🏆 RECOMMENDATION")
print("======================================")


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
# RECOVERY OFFER
# =========================================================

print()
print("======================================")
print("       📩 RECOVERY OFFER")
print("======================================")


recovery = result.get(
    "recovery"
)


if recovery:

    print(
        "Customer Interest:",
        recovery["customer_interest"]
    )

    print(
        "Original Price:",
        f"₹{recovery['original_price']:,}"
    )

    print(
        "Recovery Discount:",
        f"₹{recovery['discount']:,}"
    )

    print(
        "Recovery Price:",
        f"₹{recovery['final_price']:,}"
    )

    print()

    print(
        "🤖 Agent Message:"
    )

    print(
        recovery["message"]
    )

    print()

    print(
        "Agent Action:"
    )

    print(
        recovery["action"]
    )


# =========================================================
# AGENT TRACE
# =========================================================

print()
print("======================================")
print("        🤖 AGENT DECISION TRACE")
print("======================================")


for step in result["trace"]:

    print(
        "→",
        step
    )


print()
print("======================================")
print("             TEST COMPLETE")
print("======================================")