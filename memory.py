# =========================================================
# AI PERSONAL TECH SHOPPER
# CUSTOMER MEMORY
# =========================================================


def create_memory():

    return {

        "category": None,

        "budget": None,

        "requirements": [],

        "previous_requests": [],

        "previous_recommendations": [],

        "conversation": []

    }


# =========================================================
# UPDATE MEMORY
# =========================================================

def update_memory(
    memory,
    customer,
    user_message,
    recommendation=None
):

    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    if customer.get("category"):

        memory["category"] = customer[
            "category"
        ]


    # -----------------------------------------------------
    # BUDGET
    # -----------------------------------------------------

    if customer.get("budget"):

        memory["budget"] = customer[
            "budget"
        ]


    # -----------------------------------------------------
    # REQUIREMENTS
    # -----------------------------------------------------

    new_requirements = customer.get(
        "requirements",
        []
    )


    for requirement in new_requirements:

        if requirement not in memory[
            "requirements"
        ]:

            memory["requirements"].append(
                requirement
            )


    # -----------------------------------------------------
    # PREVIOUS REQUEST
    # -----------------------------------------------------

    memory["previous_requests"].append(
        user_message
    )


    # -----------------------------------------------------
    # PREVIOUS RECOMMENDATION
    # -----------------------------------------------------

    if recommendation:

        memory[
            "previous_recommendations"
        ].append(
            recommendation
        )


    # -----------------------------------------------------
    # CONVERSATION
    # -----------------------------------------------------

    memory["conversation"].append({

        "user": user_message,

        "category": customer.get(
            "category"
        ),

        "budget": customer.get(
            "budget"
        ),

        "requirements": customer.get(
            "requirements",
            []
        ),

        "recommendation": recommendation

    })


    return memory


# =========================================================
# GET MEMORY SUMMARY
# =========================================================

def get_memory_summary(memory):

    return {

        "category": memory.get(
            "category"
        ),

        "budget": memory.get(
            "budget"
        ),

        "requirements": memory.get(
            "requirements",
            []
        ),

        "previous_requests": memory.get(
            "previous_requests",
            []
        ),

        "previous_recommendations": memory.get(
            "previous_recommendations",
            []
        )

    }