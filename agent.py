from ai_brain import understand_request

from tools import (
    search_products,
    check_stock,
    recommend_accessories
)

from recommendation import calculate_score

from cart import ShoppingCart

from checkout import (
    create_order,
    process_payment,
    show_order
)


# ==========================================
# SHOPPING AGENT
# ==========================================

def shopping_agent(user_message):

    print()
    print("======================================")
    print("        🤖 AI SHOPPING AGENT")
    print("======================================")


    # ==========================================
    # STEP 1 — UNDERSTAND CUSTOMER
    # ==========================================

    print()
    print("1️⃣ Understanding customer request...")

    customer = understand_request(
        user_message
    )

    print(
        "Category:",
        customer["category"]
    )

    print(
        "Budget: ₹",
        customer["budget"]
    )

    print(
        "Requirements:",
        ", ".join(
            customer["requirements"]
        )
    )


    # ==========================================
    # STEP 2 — SEARCH PRODUCTS
    # ==========================================

    print()
    print("2️⃣ Searching product catalog...")

    found_products = search_products(
        category=customer["category"],
        max_price=customer["budget"]
    )


    # ==========================================
    # STEP 3 — SCORE PRODUCTS
    # ==========================================

    print()
    print("3️⃣ Evaluating products...")

    recommendations = []


    for product in found_products:

        score = calculate_score(
            product,
            customer
        )

        recommendations.append(
            {
                "product": product,
                "score": score
            }
        )


    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    # ==========================================
    # STEP 4 — CHECK STOCK
    # ==========================================

    print()
    print("4️⃣ Checking product availability...")

    available_products = []


    for item in recommendations:

        product = item["product"]

        stock = check_stock(
            product["name"]
        )


        if stock["available"]:

            available_products.append(
                item
            )


    # ==========================================
    # STEP 5 — SELECT BEST PRODUCTS
    # ==========================================

    print()
    print("5️⃣ Selecting best matches...")


    best_products = available_products[:3]


    if not best_products:

        print()
        print(
            "❌ Sorry, no suitable products were found."
        )

        return []


    # ==========================================
    # STEP 6 — SHOW RECOMMENDATIONS
    # ==========================================

    print()
    print("======================================")
    print("        ✨ BEST PRODUCTS")
    print("======================================")


    for index, item in enumerate(
        best_products,
        start=1
    ):

        product = item["product"]

        print()

        print(
            f"{index}. {product['name']}"
        )

        print(
            f"   Price: ₹{product['price']:,}"
        )

        print(
            f"   Match Score: "
            f"{item['score']}/100"
        )

        print(
            f"   Stock: "
            f"{product['stock']}"
        )


    # ==========================================
    # STEP 7 — RECOMMEND ACCESSORIES
    # ==========================================

    print()
    print("7️⃣ Finding useful accessories...")


    accessories = recommend_accessories(
        customer["requirements"]
    )


    if accessories:

        print()
        print("🎁 Suggested Accessories:")


        for accessory in accessories[:3]:

            print(
                f"- {accessory['name']} "
                f"₹{accessory['price']:,}"
            )


    else:

        print(
            "No additional accessories found."
        )


    # ==========================================
    # RETURN RESULTS
    # ==========================================

    return best_products


# ==========================================
# PURCHASE PRODUCT
# ==========================================

def purchase_product(product):

    print()
    print("======================================")
    print("        🛒 SHOPPING CART")
    print("======================================")


    # Create cart

    cart = ShoppingCart()


    # Add selected product

    cart.add_product(
        product
    )


    # Show cart

    cart.show_cart()


    # ==========================================
    # CUSTOMER CONFIRMATION
    # ==========================================

    print()

    confirmation = input(
        "Do you want to continue to checkout? "
        "(yes/no): "
    )


    if confirmation.lower() not in [
        "yes",
        "y"
    ]:

        print()
        print(
            "❌ Checkout cancelled."
        )

        return


    # ==========================================
    # CREATE ORDER
    # ==========================================

    print()
    print(
        "📦 Creating your order..."
    )


    order = create_order(
        cart
    )


    if order is None:

        print(
            "❌ Unable to create order."
        )

        return


    # ==========================================
    # DEMO PAYMENT
    # ==========================================

    order = process_payment(
        order
    )


    # ==========================================
    # ORDER CONFIRMATION
    # ==========================================

    show_order(
        order
    )


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print()
    print("🛍️ Welcome to AI Personal Tech Shopper")


    message = input(
        "\nWhat are you looking for? "
    )


    # Run shopping agent

    recommendations = shopping_agent(
        message
    )


    # ==========================================
    # CUSTOMER SELECTS PRODUCT
    # ==========================================

    if recommendations:

        print()
        print(
            "======================================"
        )

        print(
            "Select a product to purchase."
        )


        choice = input(
            "Enter product number "
            "(1, 2, 3) or 'no': "
        )


        if choice.lower() != "no":

            try:

                product_number = int(
                    choice
                )


                if (
                    product_number >= 1
                    and
                    product_number <= len(
                        recommendations
                    )
                ):

                    selected_product = (
                        recommendations[
                            product_number - 1
                        ]["product"]
                    )


                    print()

                    print(
                        "You selected:",
                        selected_product["name"]
                    )


                    # Purchase flow

                    purchase_product(
                        selected_product
                    )


                else:

                    print(
                        "❌ Invalid product number."
                    )


            except ValueError:

                print(
                    "❌ Please enter a valid number."
                )