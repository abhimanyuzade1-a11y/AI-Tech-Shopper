# =========================================================
# AI PERSONAL TECH SHOPPER
# AGENT PLANNER
# =========================================================


def create_plan(customer):

    requirements = [
        item.lower()
        for item in customer.get(
            "requirements",
            []
        )
    ]

    plan = []


    # =====================================================
    # ALWAYS SEARCH
    # =====================================================

    plan.append(
        "search_products"
    )


    # =====================================================
    # STOCK CHECK
    # =====================================================

    plan.append(
        "check_stock"
    )


    # =====================================================
    # PERFORMANCE EVALUATION
    # =====================================================

    performance_requirements = [

        "gaming",
        "ai/ml",
        "ai",
        "machine learning",
        "programming",
        "photography",
        "content creation",
        "video editing"

    ]


    needs_evaluation = any(

        requirement in performance_requirements

        for requirement in requirements

    )


    if needs_evaluation:

        plan.append(
            "evaluate_products"
        )


    # =====================================================
    # COMPARISON
    # =====================================================

    if len(requirements) >= 1:

        plan.append(
            "compare_products"
        )


    # =====================================================
    # ACCESSORIES
    # =====================================================

    plan.append(
        "recommend_accessories"
    )


    # =====================================================
    # FINAL RECOMMENDATION
    # =====================================================

    plan.append(
        "make_recommendation"
    )


    return plan