# =========================================================
# AI PERSONAL TECH SHOPPER
# SMART OFFERS & DISCOUNTS
# =========================================================


# =========================================================
# CALCULATE SMART DISCOUNT
# =========================================================

def calculate_discount(
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

    score = customer.get(
        "match_score",
        0
    )


    discount = 0

    reason = ""


    # =====================================================
    # HIGH MATCH PRODUCT
    # =====================================================

    if score >= 90:

        discount = 2000

        reason = (
            "High match with customer requirements"
        )


    # =====================================================
    # PRODUCT CLOSE TO BUDGET
    # =====================================================

    elif budget and price >= budget * 0.90:

        discount = 1500

        reason = (
            "Product is close to the customer's "
            "maximum budget"
        )


    # =====================================================
    # LOWER PRICED PRODUCT
    # =====================================================

    elif budget and price <= budget * 0.75:

        discount = 1000

        reason = (
            "Customer has additional budget "
            "available"
        )


    # =====================================================
    # DEFAULT OFFER
    # =====================================================

    else:

        discount = 500

        reason = (
            "Standard promotional offer"
        )


    # =====================================================
    # NEVER DISCOUNT MORE THAN PRODUCT PRICE
    # =====================================================

    discount = min(
        discount,
        price
    )


    final_price = (
        price - discount
    )


    return {

        "original_price": price,

        "discount": discount,

        "final_price": final_price,

        "reason": reason

    }


# =========================================================
# CREATE BUNDLE
# =========================================================

def create_bundle(
    product,
    accessories
):

    bundle_items = [
        product
    ]


    for accessory in accessories:

        if isinstance(
            accessory,
            dict
        ):

            bundle_items.append(
                accessory
            )


    # =====================================================
    # CALCULATE TOTAL
    # =====================================================

    total = 0


    for item in bundle_items:

        total += item.get(
            "price",
            0
        )


    # =====================================================
    # BUNDLE DISCOUNT
    # =====================================================

    bundle_discount = 0


    if len(bundle_items) >= 3:

        bundle_discount = 2500

    elif len(bundle_items) == 2:

        bundle_discount = 1000


    bundle_discount = min(
        bundle_discount,
        total
    )


    final_price = (
        total - bundle_discount
    )


    return {

        "items": bundle_items,

        "original_total": total,

        "bundle_discount": bundle_discount,

        "final_total": final_price

    }