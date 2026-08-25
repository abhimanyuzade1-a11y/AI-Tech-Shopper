# =========================================================
# AI PERSONAL TECH SHOPPER
# CART MANAGEMENT ENGINE
# =========================================================


class CartManager:

    def __init__(self):

        self.items = []


    # =====================================================
    # ADD PRODUCT
    # =====================================================

    def add_product(

        self,

        product,

        quantity=1,

        discount=0

    ):

        price = product.get(

            "price",

            0

        )


        item = {

            "name":
                product.get(
                    "name",
                    "Unknown Product"
                ),

            "price":
                price,

            "quantity":
                quantity,

            "discount":
                discount

        }


        self.items.append(

            item

        )


        return item


    # =====================================================
    # REMOVE PRODUCT
    # =====================================================

    def remove_product(

        self,

        product_name

    ):

        original_count = len(
            self.items
        )


        self.items = [

            item

            for item in self.items

            if item["name"].lower()
            != product_name.lower()

        ]


        return (

            len(self.items)

            <

            original_count

        )


    # =====================================================
    # CALCULATE SUBTOTAL
    # =====================================================

    def get_subtotal(self):

        subtotal = 0


        for item in self.items:

            subtotal += (

                item["price"]

                *

                item["quantity"]

            )


        return subtotal


    # =====================================================
    # CALCULATE DISCOUNT
    # =====================================================

    def get_discount(self):

        discount = 0


        for item in self.items:

            discount += (

                item["discount"]

                *

                item["quantity"]

            )


        return discount


    # =====================================================
    # CALCULATE TOTAL
    # =====================================================

    def get_total(self):

        subtotal = self.get_subtotal()

        discount = self.get_discount()


        return max(

            subtotal - discount,

            0

        )


    # =====================================================
    # ITEM COUNT
    # =====================================================

    def get_item_count(self):

        return sum(

            item["quantity"]

            for item in self.items

        )


    # =====================================================
    # VIEW CART
    # =====================================================

    def get_cart(self):

        return self.items


    # =====================================================
    # CLEAR CART
    # =====================================================

    def clear(self):

        self.items = []


    # =====================================================
    # CART SUMMARY
    # =====================================================

    def get_summary(self):

        return {

            "items":
                self.items,

            "item_count":
                self.get_item_count(),

            "subtotal":
                self.get_subtotal(),

            "discount":
                self.get_discount(),

            "total":
                self.get_total()

        }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

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

        quantity=1,

        discount=3000

    )


    cart.add_product(

        mouse,

        quantity=1,

        discount=200

    )


    summary = cart.get_summary()


    print()

    print(
        "======================================"
    )

    print(
        "          🛒 SHOPPING CART"
    )

    print(
        "======================================"
    )

    print()


    for item in summary["items"]:

        print(

            f"{item['name']} "
            f"x{item['quantity']}"

        )

        print(

            f"Price: ₹{item['price']:,}"

        )

        print(

            f"Discount: ₹{item['discount']:,}"

        )

        print()


    print(
        "--------------------------------------"
    )


    print(

        "Items:",

        summary["item_count"]

    )


    print(

        "Subtotal:",

        f"₹{summary['subtotal']:,}"

    )


    print(

        "Discount:",

        f"₹{summary['discount']:,}"

    )


    print(

        "Final Total:",

        f"₹{summary['total']:,}"

    )


    print()