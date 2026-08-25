# =========================================================
# TEST CUSTOMER MEMORY
# =========================================================

from memory import (
    create_memory,
    update_memory,
    get_memory_summary
)


# =========================================================
# CREATE MEMORY
# =========================================================

memory = create_memory()


# =========================================================
# FIRST CUSTOMER REQUEST
# =========================================================

customer1 = {

    "category": "Laptop",

    "budget": 80000,

    "requirements": [

        "AI/ML",

        "Gaming",

        "Programming"

    ]

}


memory = update_memory(

    memory,

    customer1,

    "I need a laptop for AI and gaming under 80000",

    "ApexBook Pro 15"

)


# =========================================================
# SECOND CUSTOMER REQUEST
# =========================================================

customer2 = {

    "category": "Laptop",

    "budget": 80000,

    "requirements": [

        "Lightweight"

    ]

}


memory = update_memory(

    memory,

    customer2,

    "I want something lighter",

    "NovaBook Air 14"

)


# =========================================================
# DISPLAY MEMORY
# =========================================================

summary = get_memory_summary(
    memory
)


print()
print(
    "======================================"
)

print(
    "       🧠 CUSTOMER MEMORY"
)

print(
    "======================================"
)

print(
    "Category:",
    summary["category"]
)

print(
    "Budget:",
    summary["budget"]
)

print(
    "Requirements:",
    summary["requirements"]
)

print(
    "Previous Requests:"
)

for request in summary[
    "previous_requests"
]:

    print(
        "→",
        request
    )


print(
    "Previous Recommendations:"
)

for recommendation in summary[
    "previous_recommendations"
]:

    print(
        "→",
        recommendation
    )

print(
    "======================================"
)