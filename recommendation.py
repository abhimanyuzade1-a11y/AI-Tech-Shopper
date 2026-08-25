# =========================================================
# AI PERSONAL TECH SHOPPER
# SMART RECOMMENDATION ENGINE
# =========================================================


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def contains_text(value, keywords):

    if not value:
        return False

    value = str(value).lower()

    for keyword in keywords:

        if keyword.lower() in value:

            return True

    return False


# =========================================================
# SCORE PRODUCT
# =========================================================

def calculate_score(product, customer):

    score = 0

    requirements = customer.get(
        "requirements",
        []
    )


    # =====================================================
    # REQUIREMENT MATCH
    # =====================================================

    use_cases = [

        item.lower()
        for item in product.get(
            "use_cases",
            []
        )

    ]


    for requirement in requirements:

        requirement = requirement.lower()


        # -------------------------------------------------
        # DIRECT USE-CASE MATCH
        # -------------------------------------------------

        if requirement in use_cases:

            score += 20


        # =================================================
        # AI / ML
        # =================================================

        if requirement in [
            "ai/ml",
            "ai",
            "machine learning",
            "ml"
        ]:

            # GPU
            if contains_text(
                product.get("gpu"),
                [
                    "rtx",
                    "gpu"
                ]
            ):

                score += 15


            # RAM
            if contains_text(
                product.get("ram"),
                [
                    "16gb",
                    "24gb",
                    "32gb",
                    "64gb"
                ]
            ):

                score += 10


            # Processor
            if contains_text(
                product.get("processor"),
                [
                    "i7",
                    "i9",
                    "ryzen 7",
                    "ryzen 9",
                    "snapdragon 8"
                ]
            ):

                score += 5


        # =================================================
        # GAMING
        # =================================================

        if requirement == "gaming":

            # Dedicated GPU
            if contains_text(
                product.get("gpu"),
                [
                    "rtx",
                    "rx"
                ]
            ):

                score += 15


            # High refresh display
            if contains_text(
                product.get("display"),
                [
                    "120hz",
                    "144hz",
                    "165hz",
                    "240hz"
                ]
            ):

                score += 10


            # Gaming processor
            if contains_text(
                product.get("processor"),
                [
                    "i7",
                    "i9",
                    "ryzen 7",
                    "ryzen 9",
                    "snapdragon 8"
                ]
            ):

                score += 5


        # =================================================
        # PROGRAMMING
        # =================================================

        if requirement == "programming":

            # RAM
            if contains_text(
                product.get("ram"),
                [
                    "16gb",
                    "24gb",
                    "32gb",
                    "64gb"
                ]
            ):

                score += 10


            # Strong processor
            if contains_text(
                product.get("processor"),
                [
                    "i7",
                    "i9",
                    "ryzen 7",
                    "ryzen 9"
                ]
            ):

                score += 10


            # SSD
            if contains_text(
                product.get("storage"),
                [
                    "512gb",
                    "1tb"
                ]
            ):

                score += 5


        # =================================================
        # PHOTOGRAPHY
        # =================================================

        if requirement == "photography":

            if contains_text(
                product.get("camera"),
                [
                    "108mp",
                    "200mp",
                    "50mp"
                ]
            ):

                score += 20


            if "amoled" in str(
                product.get(
                    "display",
                    ""
                )
            ).lower():

                score += 5


        # =================================================
        # CONTENT CREATION
        # =================================================

        if requirement in [
            "content creation",
            "video editing"
        ]:

            if contains_text(
                product.get("gpu"),
                [
                    "rtx",
                    "rx"
                ]
            ):

                score += 10


            if contains_text(
                product.get("ram"),
                [
                    "16gb",
                    "24gb",
                    "32gb",
                    "64gb"
                ]
            ):

                score += 10


            if contains_text(
                product.get("display"),
                [
                    "oled",
                    "2.5k",
                    "qhd"
                ]
            ):

                score += 5


        # =================================================
        # COLLEGE
        # =================================================

        if requirement == "college":

            # Affordable products get preference
            price = product.get(
                "price",
                999999
            )


            if price <= 60000:

                score += 10


            # Portable display
            if contains_text(
                product.get("display"),
                [
                    "14-inch"
                ]
            ):

                score += 5


        # =================================================
        # OFFICE
        # =================================================

        if requirement == "office":

            price = product.get(
                "price",
                999999
            )


            if price <= 60000:

                score += 10


    # =====================================================
    # CUSTOMER BUDGET
    # =====================================================

    budget = customer.get(
        "budget"
    )


    price = product.get(
        "price",
        999999
    )


    if budget:

        # Excellent value
        if price <= budget * 0.70:

            score += 10


        # Good budget usage
        elif price <= budget * 0.90:

            score += 7


        # Within budget
        elif price <= budget:

            score += 4


    # =====================================================
    # PRODUCT RATING
    # =====================================================

    rating = product.get(
        "rating",
        0
    )


    if rating >= 4.7:

        score += 5

    elif rating >= 4.5:

        score += 4

    elif rating >= 4.3:

        score += 3

    elif rating >= 4.0:

        score += 2


    # =====================================================
    # STOCK AVAILABILITY
    # =====================================================

    stock = product.get(
        "stock",
        0
    )


    if stock >= 10:

        score += 3

    elif stock > 0:

        score += 1


    # =====================================================
    # LIMIT SCORE
    # =====================================================

    return min(
        score,
        100
    )


# =========================================================
# GENERATE RECOMMENDATION REASONS
# =========================================================

def recommendation_reason(
    product,
    customer
):

    reasons = []

    requirements = customer.get(
        "requirements",
        []
    )


    use_cases = [

        item.lower()
        for item in product.get(
            "use_cases",
            []
        )

    ]


    # =====================================================
    # USE CASE REASONS
    # =====================================================

    for requirement in requirements:

        requirement_lower = (
            requirement.lower()
        )


        if requirement_lower in use_cases:

            reasons.append(

                f"Designed for {requirement}"

            )


    # =====================================================
    # AI / ML
    # =====================================================

    if any(

        req.lower() in [
            "ai/ml",
            "ai",
            "machine learning",
            "ml"
        ]

        for req in requirements

    ):

        if contains_text(
            product.get("gpu"),
            ["rtx", "rx"]
        ):

            reasons.append(
                "Dedicated GPU is suitable "
                "for AI/ML workloads"
            )


        if contains_text(
            product.get("ram"),
            [
                "16gb",
                "24gb",
                "32gb",
                "64gb"
            ]
        ):

            reasons.append(
                "Higher RAM is useful for "
                "data science and ML workloads"
            )


    # =====================================================
    # GAMING
    # =====================================================

    if "gaming" in [

        req.lower()
        for req in requirements

    ]:

        if contains_text(
            product.get("gpu"),
            ["rtx", "rx"]
        ):

            reasons.append(
                "Dedicated GPU provides "
                "strong gaming performance"
            )


        if contains_text(
            product.get("display"),
            [
                "120hz",
                "144hz",
                "165hz",
                "240hz"
            ]
        ):

            reasons.append(
                "High refresh-rate display "
                "is ideal for gaming"
            )


    # =====================================================
    # PROGRAMMING
    # =====================================================

    if "programming" in [

        req.lower()
        for req in requirements

    ]:

        if contains_text(
            product.get("ram"),
            [
                "16gb",
                "24gb",
                "32gb"
            ]
        ):

            reasons.append(
                "16GB+ RAM is suitable for "
                "development tools and multitasking"
            )


        if contains_text(
            product.get("storage"),
            [
                "512gb",
                "1tb"
            ]
        ):

            reasons.append(
                "Fast SSD storage provides "
                "space for development environments"
            )


    # =====================================================
    # PHOTOGRAPHY
    # =====================================================

    if "photography" in [

        req.lower()
        for req in requirements

    ]:

        camera = product.get(
            "camera"
        )


        if camera:

            reasons.append(
                f"Strong camera setup: {camera}"
            )


    # =====================================================
    # RATING
    # =====================================================

    rating = product.get(
        "rating"
    )


    if rating:

        reasons.append(
            f"Customer rating: {rating}/5"
        )


    # =====================================================
    # PRICE
    # =====================================================

    budget = customer.get(
        "budget"
    )


    price = product.get(
        "price"
    )


    if budget and price:

        if price <= budget:

            reasons.append(
                "Fits within the customer's budget"
            )


    return reasons