# =========================================================
# AI PERSONAL TECH SHOPPER
# CHECKOUT ENGINE
# =========================================================

from merchant_rules import get_rule


class CheckoutManager:

    def __init__(

        self,

        cart

    ):

        self.cart = cart


    # =====================================================
    # VALIDATE CART
    # =====================================================

    def validate_cart(self):

        errors = []


        if self.cart.get_item_count() == 0:

            errors.append(

                "Your cart is empty."

            )


        minimum_order = get_rule(

            "minimum_order_value",

            1000

        )


        if (

            self.cart.get_total()

            <

            minimum_order

        ):

            errors.append(

                f"Minimum order value is "
                f"₹{minimum_order:,}."

            )


        return errors


    # =====================================================
    # PREPARE CHECKOUT
    # =====================================================

    def prepare_checkout(self):

        errors = self.validate_cart()


        if errors:

            return {

                "success":
                    False,

                "errors":
                    errors

            }


        summary = self.cart.get_summary()


        return {

            "success":
                True,

            "items":
                summary["items"],

            "subtotal":
                summary["subtotal"],

            "discount":
                summary["discount"],

            "total":
                summary["total"],

            "status":
                "READY_FOR_PAYMENT"

        }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    from cart_manager import CartManager


    cart = CartManager()


    laptop = {

        "name":
            "ApexBook Pro 15",

        "price":
            74999

    }


    mouse = {

        "name":
            "HyperMouse G1",

        "price":
            2499

    }


    cart.add_product(

        laptop,

        discount=3000

    )


    cart.add_product(

        mouse,

        discount=200

    )


    checkout = CheckoutManager(

        cart

    )


    result = checkout.prepare_checkout()


    print()

    print(
        "======================================"
    )

    print(
        "          💳 CHECKOUT"
    )

    print(
        "======================================"
    )

    print()


    if result["success"]:

        print(
            "✅ Cart validated"
        )

        print()

        print(

            "Subtotal:",

            f"₹{result['subtotal']:,}"

        )


        print(

            "Discount:",

            f"₹{result['discount']:,}"

        )


        print(

            "Amount Payable:",

            f"₹{result['total']:,}"

        )


        print()

        print(
            "Status:",
            result["status"]
        )


        print()

        print(
            "💳 Ready for payment"
        )


    else:

        print(
            "❌ Checkout cannot continue"
        )


        for error in result["errors"]:

            print(
                "•",
                error
            )


    print()