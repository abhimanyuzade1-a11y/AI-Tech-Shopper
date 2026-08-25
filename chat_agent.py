# =========================================================
# AI PERSONAL TECH SHOPPER
# INTERACTIVE SHOPPING AGENT
# =========================================================

from conversation_manager import ConversationManager

from intent_engine import detect_intent

from agent_brain import run_agent


# =========================================================
# START CONVERSATION
# =========================================================

conversation = ConversationManager()


print()

print(
    "======================================"
)

print(
    "   🤖 AI PERSONAL TECH SHOPPER"
)

print(
    "======================================"
)

print()

print(
    "Type 'exit' to end the conversation."
)

print()


# =========================================================
# CHAT LOOP
# =========================================================

while True:

    user_message = input(
        "👤 You: "
    ).strip()


    # =====================================================
    # EXIT
    # =====================================================

    if user_message.lower() in [

        "exit",

        "quit",

        "bye"

    ]:

        print()

        print(
            "🤖 Agent: Thanks for shopping with me!"
        )

        break


    # =====================================================
    # EMPTY MESSAGE
    # =====================================================

    if not user_message:

        continue


    # =====================================================
    # SAVE CUSTOMER MESSAGE
    # =====================================================

    conversation.add_message(

        "customer",

        user_message

    )


    # =====================================================
    # DETECT INTENT
    # =====================================================

    intent_result = detect_intent(

        user_message

    )


    intent = intent_result[
        "intent"
    ]


    conversation.update_profile(

        intent=intent

    )


    # =====================================================
    # RUN AGENT
    # =====================================================

    try:

        result = run_agent(

            user_message

        )

    except Exception as error:

        print()

        print(
            "⚠️ Agent error:"
        )

        print(
            error
        )

        print()

        continue


    # =====================================================
    # UPDATE CUSTOMER PROFILE
    # =====================================================

    customer = result.get(

        "customer",

        {}

    )


    winner = result.get(

        "winner"

    )


    winner_name = None


    if winner:

        winner_name = winner.get(

            "name"

        )


    conversation.update_profile(

        customer=customer,

        intent=intent,

        product=winner_name

    )


    # =====================================================
    # AGENT RESPONSE
    # =====================================================

    if winner:

        response = (

            f"I recommend "
            f"{winner['name']} "
            f"at ₹{winner['price']:,}."

        )


        if result.get("offer"):

            discount = result[
                "offer"
            ].get(

                "discount",

                0

            )


            if discount > 0:

                response += (

                    f" I can also offer "
                    f"₹{discount:,} off."

                )


    else:

        response = (

            "I couldn't find a suitable "
            "product. Try adjusting your "
            "budget or requirements."

        )


    # =====================================================
    # SAVE AGENT RESPONSE
    # =====================================================

    conversation.add_message(

        "agent",

        response

    )


    print()

    print(
        "🤖 Agent:",
        response

    )


    # =====================================================
    # SHOW MEMORY
    # =====================================================

    print()

    print(
        "🧠 Current Customer Memory:"
    )


    profile = conversation.get_profile()


    print(

        f"   Budget: "
        f"{profile['budget']}"

    )


    print(

        f"   Category: "
        f"{profile['category']}"

    )


    print(

        f"   Requirements: "
        f"{profile['requirements']}"

    )


    print(

        f"   Last Product: "
        f"{profile['last_product']}"

    )


    print()