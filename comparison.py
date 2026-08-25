from recommendation import calculate_score


# =========================================================
# COMPARE TWO PRODUCTS
# =========================================================

def compare_two_products(product1, product2, customer):

    score1 = calculate_score(
        product1,
        customer
    )

    score2 = calculate_score(
        product2,
        customer
    )


    # Determine winner

    if score1 > score2:

        winner = product1
        loser = product2

    elif score2 > score1:

        winner = product2
        loser = product1

    else:

        winner = None
        loser = None


    return {
        "product1": product1,
        "product2": product2,
        "score1": score1,
        "score2": score2,
        "winner": winner,
        "loser": loser
    }


# =========================================================
# EXPLAIN PRODUCT
# =========================================================

def explain_product(product, customer):

    score = calculate_score(
        product,
        customer
    )


    matched_requirements = []

    unmatched_requirements = []


    for requirement in customer["requirements"]:

        if requirement in product["use_cases"]:

            matched_requirements.append(
                requirement
            )

        else:

            unmatched_requirements.append(
                requirement
            )


    # Build explanation

    explanation = {

        "product": product["name"],

        "score": score,

        "matched": matched_requirements,

        "not_matched": unmatched_requirements,

        "price": product["price"],

        "within_budget":
            product["price"]
            <= customer["budget"]

    }


    return explanation


# =========================================================
# GENERATE RECOMMENDATION REASON
# =========================================================

def recommendation_reason(product, customer):

    explanation = explain_product(
        product,
        customer
    )


    reasons = []


    # Budget

    if explanation["within_budget"]:

        remaining = (
            customer["budget"]
            - product["price"]
        )

        reasons.append(
            f"It fits your budget with "
            f"₹{remaining:,} remaining."
        )


    # Requirements

    if explanation["matched"]:

        reasons.append(
            "It matches your needs for "
            + ", ".join(
                explanation["matched"]
            )
            + "."
        )


    # Score

    reasons.append(
        f"Its overall match score is "
        f"{explanation['score']}/100."
    )


    return reasons