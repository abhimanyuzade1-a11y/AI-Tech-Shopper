# =========================================================
# AI PERSONAL TECH SHOPPER
# NEGOTIATION ENGINE
# =========================================================

from merchant_rules import get_rule


def negotiate_offer(

    product,

    customer,

    requested_discount=0

):

    price = product.get(

        "price",

        0

    )


    match_score = customer.get(

        "match_score",

        0

    )


    # =====================================================
    # MERCHANT DISCOUNT LIMIT
    # =====================================================

    merchant_limit = get_rule(

        "maximum_negotiation_discount",

        3000

    )


    maximum_percent = get_rule(

        "maximum_discount_percent",

        10

    )


    percentage_limit = int(

        price * maximum_percent / 100

    )


    maximum_discount = min(

        merchant_limit,

        percentage_limit

    )


    # =====================================================
    # HIGH MATCH CUSTOMERS
    # =====================================================

    if match_score >= 90:

        customer_limit = maximum_discount

    elif match_score >= 80:

        customer_limit = int(

            maximum_discount * 0.80

        )

    elif match_score >= 70:

        customer_limit = int(

            maximum_discount * 0.60

        )

    else:

        customer_limit = int(

            maximum_discount * 0.40

        )


    maximum_discount = max(

        customer_limit,

        0

    )


    # =====================================================
    # NO DISCOUNT REQUEST
    # =====================================================

    if requested_discount <= 0:

        return {

            "approved": True,

            "requested_discount": 0,

            "approved_discount":
                maximum_discount,

            "final_price":
                price - maximum_discount,

            "message":
                f"I can offer you "
                f"₹{maximum_discount:,} off.",

            "reason":
                "The offer was generated "
                "according to merchant rules."

        }


    # =====================================================
    # REQUEST WITHIN LIMIT
    # =====================================================

    if requested_discount <= maximum_discount:

        final_price = (

            price -

            requested_discount

        )


        return {

            "approved": True,

            "requested_discount":
                requested_discount,

            "approved_discount":
                requested_discount,

            "final_price":
                final_price,

            "message":
                f"Your requested discount "
                f"of ₹{requested_discount:,} "
                f"has been approved.",

            "reason":
                "The requested discount is "
                "within the merchant's "
                "allowed limit."

        }


    # =====================================================
    # REQUEST EXCEEDS LIMIT
    # =====================================================

    final_price = (

        price -

        maximum_discount

    )


    return {

        "approved": False,

        "requested_discount":
            requested_discount,

        "approved_discount":
            maximum_discount,

        "final_price":
            final_price,

        "message":
            f"I cannot approve "
            f"₹{requested_discount:,}, "
            f"but I can offer "
            f"₹{maximum_discount:,} off.",

        "reason":
            "The requested discount exceeds "
            "the merchant-defined limit."

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


    print()

    print(
        "======================================"
    )

    print(
        "       🤝 NEGOTIATION ENGINE"
    )

    print(
        "======================================"
    )

    print()


    print(
        "Product:",
        product["name"]
    )


    print(
        "Price:",
        f"₹{product['price']:,}"
    )


    print()


    print(
        "Merchant Maximum:",
        f"₹{get_rule('maximum_negotiation_discount'):,}"
    )


    print()


    result = negotiate_offer(

        product,

        customer,

        10000

    )


    print(
        "Customer Request:",
        "₹10,000 discount"
    )


    print()


    print(
        "Agent:",
        result["message"]
    )


    print(

        "Final Price:",

        f"₹{result['final_price']:,}"

    )


    print()


    print(
        "Reason:",
        result["reason"]
    )


    print()