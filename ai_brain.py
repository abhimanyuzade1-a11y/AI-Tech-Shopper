import re


def understand_request(user_message):

    message = user_message.lower()

    # -------------------------
    # Detect category
    # -------------------------

    category = "Laptop"

    if "phone" in message or "smartphone" in message:
        category = "Smartphone"

    elif "mouse" in message or "keyboard" in message or "charger" in message:
        category = "Accessory"

    elif "laptop" in message or "notebook" in message:
        category = "Laptop"


    # -------------------------
    # Detect budget
    # -------------------------

    budget = 80000

    budget_match = re.search(
        r"(?:under|below|less than|within|around)\s*[₹]?\s*(\d+(?:,\d+)*)",
        message
    )

    if budget_match:

        budget_text = budget_match.group(1)

        budget = int(
            budget_text.replace(",", "")
        )


    # -------------------------
    # Detect requirements
    # -------------------------

    requirements = []

    keyword_map = {

        "AI/ML": [
            "ai",
            "machine learning",
            "ml",
            "artificial intelligence"
        ],

        "Gaming": [
            "gaming",
            "game",
            "games"
        ],

        "Programming": [
            "programming",
            "coding",
            "developer",
            "development"
        ],

        "Photography": [
            "photography",
            "camera",
            "photos"
        ],

        "College": [
            "college",
            "student",
            "study",
            "studies"
        ],

        "Business": [
            "business",
            "office",
            "work"
        ],

        "Content Creation": [
            "content creation",
            "video editing",
            "editing",
            "creator"
        ],

        "Travel": [
            "travel",
            "travelling"
        ],

        "Music": [
            "music",
            "songs"
        ],

        "Everyday": [
            "everyday",
            "daily",
            "normal use"
        ]
    }


    for requirement, keywords in keyword_map.items():

        for keyword in keywords:

            if keyword in message:

                requirements.append(requirement)

                break


    return {
        "category": category,
        "budget": budget,
        "requirements": requirements
    }


# -------------------------
# TEST
# -------------------------

if __name__ == "__main__":

    message = input(
        "What are you looking for? "
    )

    result = understand_request(message)

    print()
    print("===== AI UNDERSTANDING =====")

    print("Category:", result["category"])
    print("Budget: ₹", result["budget"])
    print(
        "Requirements:",
        ", ".join(result["requirements"])
    )