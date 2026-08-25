# =========================================================
# AI PERSONAL TECH SHOPPER
# CUSTOMER INTENT ENGINE
# =========================================================


# =========================================================
# INTENT KEYWORDS
# =========================================================

INTENT_KEYWORDS = {

    "NEGOTIATE": [

        "discount",

        "cheaper",

        "reduce",

        "lower price",

        "offer",

        "negotiate",

        "price",

        "less"

    ],


    "COMPARE": [

        "compare",

        "comparison",

        "versus",

        "vs",

        "difference",

        "better",

        "which one"

    ],


    "BUNDLE": [

        "bundle",

        "accessories",

        "accessory",

        "mouse",

        "keyboard",

        "headphones",

        "bag",

        "add"

    ],


    "RECOVERY": [

        "abandoned",

        "cart recovery",

        "left my cart",

        "forgot checkout",

        "didn't checkout",

        "did not checkout"

    ],


    "CART": [

        "cart",

        "checkout",

        "buy",

        "purchase",

        "order",

        "add to cart"

    ],


    "RECOMMEND": [

        "recommend",

        "suggest",

        "best",

        "what should i buy",

        "which should i buy",

        "help me choose",

        "suggestion"

    ],


    "SEARCH": [

        "show me",

        "find",

        "looking for",

        "search",

        "need a",

        "want a",

        "laptop",

        "phone",

        "tablet",

        "headphones"

    ]

}


# =========================================================
# DETECT INTENT
# =========================================================

def detect_intent(
    message
):

    text = message.lower().strip()


    scores = {}


    # =====================================================
    # CALCULATE KEYWORD SCORES
    # =====================================================

    for intent, keywords in INTENT_KEYWORDS.items():

        score = 0


        for keyword in keywords:

            if keyword in text:

                score += 1


        scores[intent] = score


    # =====================================================
    # SPECIAL PRIORITY
    # =====================================================

    # Recovery is more specific than normal cart activity

    if scores["RECOVERY"] > 0:

        return {

            "intent":
                "RECOVERY",

            "confidence":
                min(
                    100,
                    60 + scores["RECOVERY"] * 20
                ),

            "scores":
                scores

        }


    # Negotiation should override normal product search

    if scores["NEGOTIATE"] > 0:

        return {

            "intent":
                "NEGOTIATE",

            "confidence":
                min(
                    100,
                    60 + scores["NEGOTIATE"] * 10
                ),

            "scores":
                scores

        }


    # Comparison should override recommendation

    if scores["COMPARE"] > 0:

        return {

            "intent":
                "COMPARE",

            "confidence":
                min(
                    100,
                    60 + scores["COMPARE"] * 10
                ),

            "scores":
                scores

        }


    # Bundle

    if scores["BUNDLE"] > 0:

        return {

            "intent":
                "BUNDLE",

            "confidence":
                min(
                    100,
                    60 + scores["BUNDLE"] * 10
                ),

            "scores":
                scores

        }


    # Cart

    if scores["CART"] > 0:

        return {

            "intent":
                "CART",

            "confidence":
                min(
                    100,
                    60 + scores["CART"] * 10
                ),

            "scores":
                scores

        }


    # Recommendation

    if scores["RECOMMEND"] > 0:

        return {

            "intent":
                "RECOMMEND",

            "confidence":
                min(
                    100,
                    60 + scores["RECOMMEND"] * 10
                ),

            "scores":
                scores

        }


    # Search

    if scores["SEARCH"] > 0:

        return {

            "intent":
                "SEARCH",

            "confidence":
                min(
                    100,
                    60 + scores["SEARCH"] * 10
                ),

            "scores":
                scores

        }


    # =====================================================
    # GENERAL
    # =====================================================

    return {

        "intent":
            "GENERAL",

        "confidence":
            30,

        "scores":
            scores

    }


# =========================================================
# HUMAN-READABLE EXPLANATION
# =========================================================

def explain_intent(
    intent_result
):

    intent = intent_result[
        "intent"
    ]

    confidence = intent_result[
        "confidence"
    ]


    explanations = {

        "SEARCH":
            "Customer wants to find products.",

        "RECOMMEND":
            "Customer wants the agent to recommend the best option.",

        "COMPARE":
            "Customer wants to compare products.",

        "NEGOTIATE":
            "Customer wants a better price or discount.",

        "BUNDLE":
            "Customer wants accessories or a product bundle.",

        "CART":
            "Customer wants to purchase or manage their cart.",

        "RECOVERY":
            "Customer is dealing with an abandoned cart.",

        "GENERAL":
            "Customer intent is not specific enough yet."

    }


    return {

        "intent":
            intent,

        "confidence":
            confidence,

        "explanation":
            explanations.get(

                intent,

                "Unknown customer intent."

            )

    }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    test_messages = [

        "I need a laptop for gaming",

        "Which laptop is better?",

        "Can you give me a discount?",

        "Add a gaming mouse",

        "I want to buy this",

        "I left my laptop in the cart",

        "Recommend something for programming",

        "Show me laptops under 80000"

    ]


    print()

    print(
        "======================================"
    )

    print(
        "       🧠 CUSTOMER INTENT ENGINE"
    )

    print(
        "======================================"
    )

    print()


    for message in test_messages:

        result = detect_intent(
            message
        )


        explanation = explain_intent(
            result
        )


        print(
            "Customer:",
            message
        )


        print(
            "Intent:",
            explanation["intent"]
        )


        print(
            "Confidence:",
            f"{explanation['confidence']}%"
        )


        print(
            "Reason:",
            explanation["explanation"]
        )


        print(
            "-" * 50
        )