from agent_brain import run_agent


print()
print("======================================")
print("       🤖 AI COMMERCE AGENT")
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
# CUSTOMER NEGOTIATION
# =========================================================

requested_discount = 10000


print()
print("💬 CUSTOMER NEGOTIATION")
print(
    f"Can you give me ₹{requested_discount:,} off?"
)


# =========================================================
# RUN AGENT
# =========================================================

result = run_agent(

    message,

    requested_discount

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
# NEGOTIATION RESULT
# =========================================================

print()
print("======================================")
print("        🤝 NEGOTIATION RESULT")
print("======================================")


negotiation = result.get(
    "negotiation"
)


if negotiation:

    print(
        "Requested Discount:",
        f"₹{negotiation['requested_discount']:,}"
    )

    print(
        "Approved Discount:",
        f"₹{negotiation['approved_discount']:,}"
    )

    print(
        "Final Price:",
        f"₹{negotiation['final_price']:,}"
    )

    print()

    print(
        "🤖 Agent:",
        negotiation["message"]
    )

    print()

    print(
        "Reason:",
        negotiation["reason"]
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