from agent_brain import run_agent


# =========================================================
# FIRST REQUEST
# =========================================================

print()
print(
    "======================================"
)

print(
    "       👤 FIRST REQUEST"
)

print(
    "======================================"
)


result1 = run_agent(

    "I need a laptop for AI and gaming "
    "under 80000"

)


print()
print(
    "Customer:",
    result1["customer"]
)

print(
    "Winner:",
    result1["winner"]["name"]
    if result1["winner"]
    else "None"
)


# =========================================================
# SECOND REQUEST
# =========================================================

print()
print(
    "======================================"
)

print(
    "       👤 FOLLOW-UP REQUEST"
)

print(
    "======================================"
)


result2 = run_agent(

    "I want something lighter"

)


print()
print(
    "Customer:",
    result2["customer"]
)

print(
    "Winner:",
    result2["winner"]["name"]
    if result2["winner"]
    else "None"
)


# =========================================================
# MEMORY
# =========================================================

print()
print(
    "======================================"
)

print(
    "       🧠 MEMORY"
)

print(
    "======================================"
)


memory = result2["memory"]


print(
    "Category:",
    memory["category"]
)

print(
    "Budget:",
    memory["budget"]
)

print(
    "Requirements:",
    memory["requirements"]
)

print(
    "Previous Requests:",
    memory["previous_requests"]
)

print(
    "Previous Recommendations:",
    memory[
        "previous_recommendations"
    ]
)