class ShoppingCart:

    def __init__(self):
        self.items = []


    # =====================================
    # ADD PRODUCT
    # =====================================

    def add_product(self, product):

        self.items.append(product)

        print(
            f"✅ Added {product['name']} to cart."
        )


    # =====================================
    # REMOVE PRODUCT
    # =====================================

    def remove_product(self, product_name):

        for product in self.items:

            if product["name"].lower() == product_name.lower():

                self.items.remove(product)

                print(
                    f"❌ Removed {product['name']}."
                )

                return

        print("Product not found in cart.")


    # =====================================
    # TOTAL
    # =====================================

    def get_total(self):

        total = 0

        for product in self.items:

            total += product["price"]

        return total


    # =====================================
    # SHOW CART
    # =====================================

    def show_cart(self):

        print()
        print("================================")
        print("           🛒 YOUR CART")
        print("================================")

        if not self.items:

            print("Your cart is empty.")

            return


        for index, product in enumerate(
            self.items,
            start=1
        ):

            print(
                f"{index}. {product['name']}"
            )

            print(
                f"   ₹{product['price']:,}"
            )


        print("--------------------------------")

        print(
            f"TOTAL: ₹{self.get_total():,}"
        )
    