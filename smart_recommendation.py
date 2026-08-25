from products import products
from ai_brain import understand_request
from recommendation import calculate_score


def get_recommendations(user_message):

    # Understand customer
    customer = understand_request(user_message)

    print()
    print("===== CUSTOMER INTENT =====")

    print("Category:", customer["category"])
    print("Budget: ₹", customer["budget"])
    print(
        "Requirements:",
        ", ".join(customer["requirements"])
    )


    # Find products

    recommendations = []

    for product in products:

        if product["category"].lower() != customer["category"].lower():
            continue

        if product["price"] > customer["budget"]:
            continue


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


    # Highest score first

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    return customer, recommendations


# -------------------------
# TEST
# -------------------------

message = input(
    "\nTell me what you want to buy: "
)

customer, recommendations = get_recommendations(
    message
)


print()
print("===== RECOMMENDED PRODUCTS =====")


if not recommendations:

    print(
        "Sorry, I couldn't find a matching product."
    )

else:

    for item in recommendations[:5]:

        product = item["product"]

        print()
        print(product["name"])
        print("Price: ₹", product["price"])
        print(
            "Match Score:",
            item["score"],
            "/ 100"
        )