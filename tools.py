from products import products


# =========================================================
# SEARCH PRODUCTS
# =========================================================

def search_products(category=None, max_price=None):

    results = []

    for product in products:

        # Category filter
        if category:

            if product["category"].lower() != category.lower():

                continue

        # Price filter
        if max_price is not None:

            if product["price"] > max_price:

                continue

        results.append(product)

    return results


# =========================================================
# CHECK STOCK
# =========================================================

def check_stock(product_name):

    for product in products:

        if product["name"].lower() == product_name.lower():

            if product["stock"] > 0:

                return {
                    "available": True,
                    "quantity": product["stock"]
                }

            else:

                return {
                    "available": False,
                    "quantity": 0
                }

    return {
        "available": False,
        "quantity": 0
    }


# =========================================================
# ACCESSORY RECOMMENDATIONS
# =========================================================

def recommend_accessories(requirements):

    accessories = []

    requirement_text = " ".join(
        requirements
    ).lower()


    for product in products:

        category = product.get(
            "category",
            ""
        ).lower()


        # Ignore main products
        if category in [
            "laptop",
            "smartphone",
            "tablet"
        ]:

            continue


        use_cases = [
            item.lower()
            for item in product.get(
                "use_cases",
                []
            )
        ]


        # Check whether accessory matches
        # customer's requirements

        matched = False


        for requirement in requirements:

            if requirement.lower() in use_cases:

                matched = True

                break


        if matched:

            accessories.append(
                product
            )


    return accessories