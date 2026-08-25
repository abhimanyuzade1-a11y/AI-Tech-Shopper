# =========================================================
# AI PERSONAL TECH SHOPPER
# ABANDONED CART RECOVERY ENGINE
# =========================================================


def create_recovery_offer(
    product,
    customer
):

    price = product.get(
        "price",
        0
    )

    budget = customer.get(
        "budget",
        0
    )

    match_score = customer.get(
        "match_score",
        0
    )


    # =====================================================
    # DETERMINE CUSTOMER INTEREST
    # =====================================================

    if match_score >= 90:

        interest = "high"

    elif match_score >= 75:

        interest = "medium"

    else:

        interest = "low"


    # =====================================================
    # DETERMINE RECOVERY DISCOUNT
    # =====================================================

    if interest == "high":

        discount = 2000

    elif interest == "medium":

        discount = 1500

    else:

        discount = 500


    # Never exceed 5% of product price

    maximum_allowed = int(
        price * 0.05
    )


    discount = min(
        discount,
        maximum_allowed
    )


    final_price = (
        price - discount
    )


    # =====================================================
    # CREATE MESSAGE
    # =====================================================

    if interest == "high":

        message = (

            f"You left {product['name']} "
            f"in your cart. Since it strongly "
            f"matches your requirements, we can "
            f"offer you ₹{discount:,} off."

        )

    elif interest == "medium":

        message = (

            f"Still considering "
            f"{product['name']}? "
            f"We can offer you ₹{discount:,} "
            f"off to help you complete your purchase."

        )

    else:

        message = (

            f"{product['name']} is still waiting "
            f"in your cart. You can save "
            f"₹{discount:,} if you complete "
            f"your purchase."

        )


    # =====================================================
    # RETURN RECOVERY ACTION
    # =====================================================

    return {

        "product":
            product["name"],

        "original_price":
            price,

        "discount":
            discount,

        "final_price":
            final_price,

        "customer_interest":
            interest,

        "message":
            message,

        "action":
            "Send personalized abandoned-cart offer"

    }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    product = {

        "name":
            "ApexBook Pro 15",

        "price":
            74999

    }


    customer = {

        "budget":
            80000,

        "match_score":
            100

    }


    result = create_recovery_offer(

        product,

        customer

    )


    print()
    print(
        "======================================"
    )

    print(
        "      🛒 CART RECOVERY AGENT"
    )

    print(
        "======================================"
    )

    print()


    print(
        "Product:",
        result["product"]
    )

    print(
        "Original Price:",
        f"₹{result['original_price']:,}"
    )

    print(
        "Customer Interest:",
        result["customer_interest"]
    )

    print(
        "Recovery Discount:",
        f"₹{result['discount']:,}"
    )

    print(
        "Recovery Price:",
        f"₹{result['final_price']:,}"
    )

    print()

    print(
        "🤖 Agent Message:"
    )

    print(
        result["message"]
    )

    print()

    print(
        "Agent Action:"
    )

    print(
        result["action"]
    )

    print()