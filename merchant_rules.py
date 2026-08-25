# =========================================================
# AI PERSONAL TECH SHOPPER
# MERCHANT BUSINESS RULES
# =========================================================


MERCHANT_RULES = {

    # -----------------------------------------------------
    # DISCOUNT RULES
    # -----------------------------------------------------

    "maximum_discount_percent": 10,

    "maximum_negotiation_discount": 3000,

    "minimum_product_margin": 0.05,


    # -----------------------------------------------------
    # BUNDLE RULES
    # -----------------------------------------------------

    "bundle_discount_percent": 5,

    "maximum_bundle_discount": 5000,


    # -----------------------------------------------------
    # CART RECOVERY RULES
    # -----------------------------------------------------

    "recovery_discount_percent": 5,

    "maximum_recovery_discount": 2000,


    # -----------------------------------------------------
    # INVENTORY RULES
    # -----------------------------------------------------

    "low_stock_threshold": 5,


    # -----------------------------------------------------
    # ORDER RULES
    # -----------------------------------------------------

    "minimum_order_value": 1000,

}


# =========================================================
# GET RULE
# =========================================================

def get_rule(
    rule_name,
    default=None
):

    return MERCHANT_RULES.get(

        rule_name,

        default

    )


# =========================================================
# DISPLAY RULES
# =========================================================

def display_rules():

    print()
    print(
        "======================================"
    )

    print(
        "       🏪 MERCHANT BUSINESS RULES"
    )

    print(
        "======================================"
    )

    print()


    for rule, value in MERCHANT_RULES.items():

        print(

            f"{rule}: {value}"

        )


    print()


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    display_rules()