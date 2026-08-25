from ai_brain import understand_request
from intent_engine import detect_intent

from tools import (
    search_products,
    check_stock,
    recommend_accessories
)

from recommendation import calculate_score
from comparison import compare_two_products
from agent_planner import create_plan

from memory import (
    create_memory,
    update_memory
)

from offers import (
    calculate_discount,
    create_bundle
)

from negotiation import (
    negotiate_offer
)

from cart_recovery import (
    create_recovery_offer
)


# =========================================================
# CUSTOMER MEMORY
# =========================================================

memory = create_memory()


# =========================================================
# RUN SHOPPING AGENT
# =========================================================

def run_agent(
    user_message,
    requested_discount=0,
    cart_abandoned=False
):

    global memory

    trace = []
    # =====================================================
    # CUSTOMER INTENT
    # =====================================================

    intent_result = detect_intent(
        user_message
    )

    customer_intent = intent_result["intent"]

    trace.append(
        f"🎯 Customer intent detected: "
        f"{customer_intent}"
    )

    trace.append(
        f"📊 Intent confidence: "
        f"{intent_result['confidence']}%"
    )

    # =====================================================
    # 1. UNDERSTAND CUSTOMER
    # =====================================================

    trace.append(
        "🧠 Understanding customer goal"
    )

    customer = understand_request(
        user_message
    )


    # =====================================================
    # 2. APPLY MEMORY
    # =====================================================

    if memory.get("category"):

        if not customer.get("category"):

            customer["category"] = memory["category"]


    if memory.get("budget"):

        if not customer.get("budget"):

            customer["budget"] = memory["budget"]


    previous_requirements = memory.get(
        "requirements",
        []
    )

    current_requirements = customer.get(
        "requirements",
        []
    )


    combined_requirements = []


    for requirement in (
        previous_requirements +
        current_requirements
    ):

        if requirement not in combined_requirements:

            combined_requirements.append(
                requirement
            )


    customer["requirements"] = combined_requirements


    if memory.get("previous_requests"):

        trace.append(
            "💾 Using previous customer preferences"
        )


    # =====================================================
    # 3. CREATE AGENT PLAN
    # =====================================================

    plan = create_plan(
        customer
    )


    trace.append(
        "📝 Agent created an action plan"
    )


    for number, action in enumerate(
        plan,
        start=1
    ):

        trace.append(
            f"   {number}. {action}"
        )


    # =====================================================
    # 4. SEARCH PRODUCTS
    # =====================================================

    trace.append(
        "🔎 Searching product catalog"
    )


    products = search_products(

        category=customer["category"],

        max_price=customer["budget"]

    )


    trace.append(
        f"📦 Found {len(products)} "
        "products within budget"
    )


    # =====================================================
    # 5. CHECK STOCK
    # =====================================================

    available = []


    for product in products:

        stock = check_stock(
            product["name"]
        )


        if stock["available"]:

            available.append(
                product
            )


    trace.append(
        f"📦 {len(available)} "
        "products currently available"
    )


    # =====================================================
    # 6. SCORE PRODUCTS
    # =====================================================

    scored = []


    for product in available:

        score = calculate_score(
            product,
            customer
        )


        scored.append({

            "product": product,

            "score": score

        })


    scored.sort(

        key=lambda item: item["score"],

        reverse=True

    )


    trace.append(
        "📊 Products scored against "
        "customer requirements"
    )


    # =====================================================
    # 7. COMPARE TOP PRODUCTS
    # =====================================================

    winner = None


    if len(scored) >= 2:

        product1 = scored[0]["product"]

        product2 = scored[1]["product"]


        compare_two_products(

            product1,

            product2,

            customer

        )


        trace.append(
            "⚖️ Compared the two strongest candidates"
        )


        winner = scored[0]["product"]


    elif len(scored) == 1:

        winner = scored[0]["product"]


        trace.append(
            "🏆 Only one suitable product was available"
        )


    # =====================================================
    # 8. RECOMMEND ACCESSORIES
    # =====================================================

    accessories = []


    if winner:

        accessories = recommend_accessories(

            customer["requirements"]

        )


        trace.append(
            "🎁 Found relevant accessories"
        )


    # =====================================================
    # 9. CALCULATE SMART OFFER
    # =====================================================

    offer = None

    winner_score = 0


    if winner:

        for item in scored:

            if item["product"]["name"] == winner["name"]:

                winner_score = item["score"]

                break


        offer_customer = {

            "budget": customer.get(
                "budget",
                0
            ),

            "match_score": winner_score

        }


        offer = calculate_discount(

            winner,

            offer_customer

        )


        trace.append(
            "💰 Agent calculated a smart offer"
        )


        trace.append(

            f"   💸 Discount: "
            f"₹{offer['discount']:,}"

        )


        trace.append(

            f"   💡 Reason: "
            f"{offer['reason']}"

        )


    # =====================================================
    # 10. NEGOTIATION
    # =====================================================

    negotiation = None


    if winner:

        negotiation_customer = {

            "budget": customer.get(
                "budget",
                0
            ),

            "match_score": winner_score

        }


        negotiation = negotiate_offer(

            winner,

            negotiation_customer,

            requested_discount

        )


        if requested_discount > 0:

            trace.append(
                "🤝 Customer requested a discount"
            )


            if negotiation["approved"]:

                trace.append(

                    f"✅ Discount approved: "
                    f"₹{negotiation['approved_discount']:,}"

                )

            else:

                trace.append(

                    "⚖️ Requested discount exceeded "
                    "merchant limit"

                )


                trace.append(

                    f"💰 Maximum approved discount: "
                    f"₹{negotiation['approved_discount']:,}"

                )


    # =====================================================
    # 11. SMART BUNDLE
    # =====================================================

    bundle = None


    if winner and accessories:

        bundle = create_bundle(

            winner,

            accessories

        )


        trace.append(
            "📦 Agent created a smart bundle"
        )


        trace.append(

            f"   💰 Bundle savings: "
            f"₹{bundle['bundle_discount']:,}"

        )


    # =====================================================
    # 12. CART RECOVERY
    # =====================================================

    recovery = None


    if winner and cart_abandoned:

        recovery_customer = {

            "budget": customer.get(
                "budget",
                0
            ),

            "match_score": winner_score

        }


        recovery = create_recovery_offer(

            winner,

            recovery_customer

        )


        trace.append(
            "🛒 Agent detected an abandoned cart"
        )


        trace.append(

            f"   🎯 Customer interest: "
            f"{recovery['customer_interest']}"

        )


        trace.append(

            f"   💰 Recovery discount: "
            f"₹{recovery['discount']:,}"

        )


        trace.append(
            "📩 Personalized recovery offer generated"
        )


    # =====================================================
    # 13. UPDATE MEMORY
    # =====================================================

    recommendation_name = None


    if winner:

        recommendation_name = winner["name"]


    memory = update_memory(

        memory,

        customer,

        user_message,

        recommendation_name

    )


    trace.append(
        "💾 Customer preferences saved"
    )


    # =====================================================
    # 14. FINAL DECISION
    # =====================================================

    if winner:

        trace.append(

            f"🏆 Selected "
            f"{winner['name']} "
            "as the best match"

        )

    else:

        trace.append(
            "❌ No suitable product found"
        )


    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {
                "intent": intent_result,

        "customer": customer,

        "plan": plan,

        "products": scored,

        "winner": winner,

        "accessories": accessories,

        "offer": offer,

        "negotiation": negotiation,

        "bundle": bundle,

        "recovery": recovery,

        "trace": trace,

        "memory": memory

    }