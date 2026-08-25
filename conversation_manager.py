# =========================================================
# AI PERSONAL TECH SHOPPER
# CONVERSATION MANAGER
# =========================================================


class ConversationManager:

    def __init__(self):

        self.history = []

        self.customer_profile = {

            "name": None,

            "budget": None,

            "category": None,

            "requirements": [],

            "last_product": None,

            "last_intent": None

        }


    # =====================================================
    # ADD MESSAGE
    # =====================================================

    def add_message(

        self,

        role,

        message

    ):

        self.history.append({

            "role": role,

            "message": message

        })


    # =====================================================
    # UPDATE PROFILE
    # =====================================================

    def update_profile(

        self,

        customer=None,

        intent=None,

        product=None

    ):

        if customer:

            if customer.get("name"):

                self.customer_profile["name"] = (

                    customer["name"]

                )


            if customer.get("budget"):

                self.customer_profile["budget"] = (

                    customer["budget"]

                )


            if customer.get("category"):

                self.customer_profile["category"] = (

                    customer["category"]

                )


            requirements = customer.get(

                "requirements",

                []

            )


            for requirement in requirements:

                if requirement not in (

                    self.customer_profile[
                        "requirements"
                    ]

                ):

                    self.customer_profile[
                        "requirements"
                    ].append(

                        requirement

                    )


        if intent:

            self.customer_profile[
                "last_intent"
            ] = intent


        if product:

            self.customer_profile[
                "last_product"
            ] = product


    # =====================================================
    # GET PROFILE
    # =====================================================

    def get_profile(self):

        return self.customer_profile


    # =====================================================
    # GET HISTORY
    # =====================================================

    def get_history(self):

        return self.history


    # =====================================================
    # GET LAST MESSAGE
    # =====================================================

    def get_last_message(self):

        if not self.history:

            return None


        return self.history[-1]


    # =====================================================
    # GET CONVERSATION SUMMARY
    # =====================================================

    def get_summary(self):

        profile = self.customer_profile


        return {

            "customer_name":
                profile["name"],

            "budget":
                profile["budget"],

            "category":
                profile["category"],

            "requirements":
                profile["requirements"],

            "last_product":
                profile["last_product"],

            "last_intent":
                profile["last_intent"],

            "messages":
                len(self.history)

        }


    # =====================================================
    # CLEAR CONVERSATION
    # =====================================================

    def clear(self):

        self.history = []

        self.customer_profile = {

            "name": None,

            "budget": None,

            "category": None,

            "requirements": [],

            "last_product": None,

            "last_intent": None

        }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    conversation = ConversationManager()


    conversation.add_message(

        "customer",

        "I need a laptop"

    )


    conversation.add_message(

        "agent",

        "What is your budget?"

    )


    conversation.add_message(

        "customer",

        "My budget is 80000"

    )


    conversation.update_profile({

        "budget": 80000,

        "category": "Laptop"

    })


    conversation.add_message(

        "agent",

        "What will you use it for?"

    )


    conversation.add_message(

        "customer",

        "AI, gaming and programming"

    )


    conversation.update_profile({

        "requirements": [

            "AI/ML",

            "Gaming",

            "Programming"

        ]

    })


    print()

    print(
        "======================================"
    )

    print(
        "      💬 CONVERSATION MANAGER"
    )

    print(
        "======================================"
    )

    print()


    print(
        "Conversation Summary:"
    )


    print(
        conversation.get_summary()
    )


    print()

    print(
        "Conversation History:"
    )


    for message in conversation.get_history():

        print(

            f"{message['role'].upper()}: "
            f"{message['message']}"

        )