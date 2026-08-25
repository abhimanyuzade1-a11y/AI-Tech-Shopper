import streamlit as st

from agent_brain import run_agent


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(

    page_title="AI Personal Tech Shopper",

    page_icon="🤖",

    layout="wide"

)


# =========================================================
# TITLE
# =========================================================

st.title(
    "🤖 AI Personal Tech Shopper"
)

st.write(
    "Your intelligent shopping agent that understands "
    "your needs, compares products, negotiates offers, "
    "creates bundles and helps you checkout."
)


st.divider()


# =========================================================
# CUSTOMER REQUEST
# =========================================================

st.header(
    "🛍️ What are you looking for?"
)


user_message = st.text_area(

    "Tell your shopping agent what you need:",

    placeholder=(
        "Example: I need a laptop for AI and gaming "
        "under 80000"
    ),

    height=100

)


# =========================================================
# RUN AGENT
# =========================================================

if st.button(

    "🤖 Ask My Shopping Agent",

    type="primary"

):

    if not user_message.strip():

        st.warning(
            "Please describe what you are looking for."
        )

    else:

        with st.spinner(
            "🤖 Your shopping agent is thinking..."
        ):

            try:

                result = run_agent(
                    user_message
                )

                st.session_state.agent_result = result

            except Exception as error:

                st.error(
                    "Something went wrong."
                )

                st.code(
                    str(error)
                )


# =========================================================
# DISPLAY RESULT
# =========================================================

if "agent_result" in st.session_state:

    result = st.session_state.agent_result


    customer = result.get(
        "customer",
        {}
    )

    plan = result.get(
        "plan",
        []
    )

    products = result.get(
        "products",
        []
    )

    winner = result.get(
        "winner"
    )

    accessories = result.get(
        "accessories",
        []
    )

    offer = result.get(
        "offer"
    )

    negotiation = result.get(
        "negotiation"
    )

    bundle = result.get(
        "bundle"
    )

    trace = result.get(
        "trace",
        []
    )

    memory = result.get(
        "memory",
        {}
    )


    # =====================================================
    # CUSTOMER UNDERSTANDING
    # =====================================================

    st.divider()

    st.header(
        "🧠 What I Understood"
    )


    col1, col2, col3 = st.columns(
        3
    )


    with col1:

        st.metric(

            "Category",

            customer.get(
                "category",
                "Unknown"
            )

        )


    with col2:

        budget = customer.get(
            "budget"
        )


        if budget:

            budget_text = (
                f"₹{budget:,}"
            )

        else:

            budget_text = "Not specified"


        st.metric(

            "Budget",

            budget_text

        )


    with col3:

        st.write(
            "**Requirements**"
        )


        requirements = customer.get(
            "requirements",
            []
        )


        if requirements:

            st.write(
                " • ".join(
                    requirements
                )
            )

        else:

            st.write(
                "None specified"
            )


    # =====================================================
    # CUSTOMER MEMORY
    # =====================================================

    st.divider()

    st.header(
        "💾 Customer Memory"
    )


    memory_col1, memory_col2 = st.columns(
        2
    )


    with memory_col1:

        st.write(
            "**Remembered Preferences**"
        )


        st.write(

            f"Category: "
            f"**{memory.get('category', 'None')}**"

        )


        remembered_budget = memory.get(
            "budget"
        )


        if remembered_budget:

            st.write(

                f"Budget: "
                f"**₹{remembered_budget:,}**"

            )


        remembered_requirements = memory.get(
            "requirements",
            []
        )


        if remembered_requirements:

            st.write(

                "Requirements: "
                +
                ", ".join(
                    remembered_requirements
                )

            )


    with memory_col2:

        st.write(
            "**Previous Requests**"
        )


        previous_requests = memory.get(

            "previous_requests",

            []

        )


        if previous_requests:

            for request in previous_requests:

                st.write(
                    f"• {request}"
                )

        else:

            st.write(
                "No previous requests."
            )


    # =====================================================
    # ACTION PLAN
    # =====================================================

    st.divider()

    st.header(
        "📝 Agent Action Plan"
    )


    if plan:

        for number, action in enumerate(

            plan,

            start=1

        ):

            st.write(

                f"**{number}.** `{action}`"

            )


    # =====================================================
    # DECISION TRACE
    # =====================================================

    st.divider()

    st.header(
        "🤖 Agent Decision Process"
    )


    for step in trace:

        st.write(
            step
        )


    # =====================================================
    # RECOMMENDATION
    # =====================================================

    st.divider()

    st.header(
        "🏆 Best Recommendation"
    )


    if winner:

        st.subheader(
            winner["name"]
        )


        col1, col2, col3 = st.columns(
            3
        )


        with col1:

            st.metric(

                "Original Price",

                f"₹{winner['price']:,}"

            )


        winner_score = 0


        for item in products:

            if item["product"]["name"] == winner["name"]:

                winner_score = item["score"]

                break


        with col2:

            st.metric(

                "Match Score",

                f"{winner_score}/100"

            )


        with col3:

            st.metric(

                "Rating",

                f"{winner.get('rating', 'N/A')}/5"

            )


        use_cases = winner.get(
            "use_cases",
            []
        )


        if use_cases:

            st.write(
                "**Best For:**"
            )

            st.write(
                " • ".join(use_cases)
            )


    else:

        st.error(
            "❌ No suitable product found."
        )


    # =====================================================
    # SMART OFFER
    # =====================================================

    if winner and offer:

        st.divider()

        st.header(
            "💰 Personalized Smart Offer"
        )


        offer_col1, offer_col2, offer_col3 = st.columns(
            3
        )


        with offer_col1:

            st.metric(

                "Original Price",

                f"₹{offer['original_price']:,}"

            )


        with offer_col2:

            st.metric(

                "You Save",

                f"₹{offer['discount']:,}"

            )


        with offer_col3:

            st.metric(

                "Offer Price",

                f"₹{offer['final_price']:,}"

            )


        st.success(

            "🎉 The agent found a personalized "
            "offer for you!"

        )


        st.write(

            f"**Why this offer?** "
            f"{offer['reason']}"

        )


    # =====================================================
    # NEGOTIATION SECTION
    # =====================================================

    if winner:

        st.divider()

        st.header(
            "🤝 Negotiate With The Agent"
        )


        st.write(

            "Think the price is too high? "
            "Make an offer and let the agent "
            "decide within the merchant's rules."

        )


        requested_discount = st.number_input(

            "How much discount would you like?",

            min_value=0,

            max_value=int(
                winner["price"]
            ),

            value=0,

            step=500

        )


        if st.button(
            "🤝 Make My Offer"
        ):

            with st.spinner(
                "🤖 Agent is evaluating your offer..."
            ):

                negotiation_result = run_agent(

                    user_message,

                    int(
                        requested_discount
                    )

                )


            st.session_state.negotiation_result = (
                negotiation_result
            )


        if "negotiation_result" in st.session_state:

            negotiation_data = (
                st.session_state.negotiation_result
            )


            negotiation = negotiation_data.get(
                "negotiation"
            )


            if negotiation:

                st.subheader(
                    "🤖 Agent Response"
                )


                if negotiation["approved"]:

                    st.success(

                        "✅ "
                        + negotiation["message"]

                    )

                else:

                    st.warning(

                        "⚖️ "
                        + negotiation["message"]

                    )


                ncol1, ncol2, ncol3 = st.columns(
                    3
                )


                with ncol1:

                    st.metric(

                        "Requested",

                        f"₹{negotiation['requested_discount']:,}"

                    )


                with ncol2:

                    st.metric(

                        "Approved",

                        f"₹{negotiation['approved_discount']:,}"

                    )


                with ncol3:

                    st.metric(

                        "Final Price",

                        f"₹{negotiation['final_price']:,}"

                    )


                st.info(

                    "🧠 Decision: "
                    + negotiation["reason"]

                )


    # =====================================================
    # ACCESSORIES
    # =====================================================

    if accessories:

        st.divider()

        st.header(
            "🎁 Recommended Add-ons"
        )


        st.write(

            "The agent selected useful accessories "
            "based on your requirements."

        )


        for accessory in accessories:

            if isinstance(
                accessory,
                dict
            ):

                st.write(

                    f"🛍️ **{accessory['name']}** "
                    f"— ₹{accessory['price']:,}"

                )


    # =====================================================
    # SMART BUNDLE
    # =====================================================

    if winner and bundle:

        st.divider()

        st.header(
            "📦 Smart Bundle"
        )


        for item in bundle["items"]:

            st.write(

                f"• **{item['name']}** "
                f"— ₹{item['price']:,}"

            )


        bundle_col1, bundle_col2, bundle_col3 = st.columns(
            3
        )


        with bundle_col1:

            st.metric(

                "Original Total",

                f"₹{bundle['original_total']:,}"

            )


        with bundle_col2:

            st.metric(

                "Bundle Savings",

                f"₹{bundle['bundle_discount']:,}"

            )


        with bundle_col3:

            st.metric(

                "Bundle Price",

                f"₹{bundle['final_total']:,}"

            )


        st.success(
            "🔥 Smart bundle offer available!"
        )


    # =====================================================
    # ALTERNATIVE PRODUCTS
    # =====================================================

    st.divider()

    st.header(
        "🔎 Other Strong Alternatives"
    )


    alternatives = []


    for item in products:

        product = item["product"]


        if not winner:

            alternatives.append(
                item
            )

        elif product["name"] != winner["name"]:

            alternatives.append(
                item
            )


    for item in alternatives[:5]:

        product = item["product"]

        score = item["score"]


        col1, col2, col3 = st.columns(
            3
        )


        with col1:

            st.write(
                f"**{product['name']}**"
            )


        with col2:

            st.write(
                f"₹{product['price']:,}"
            )


        with col3:

            st.write(
                f"Match: **{score}/100**"
            )


        st.progress(
            min(
                score / 100,
                1.0
            )
        )


    # =====================================================
    # SHOPPING CART
    # =====================================================

    st.divider()

    st.header(
        "🛒 Shopping Cart"
    )


    if winner:

        if st.button(
            "➕ Add Recommended Product to Cart"
        ):

            st.session_state.cart = {

                "type": "product",

                "product": winner,

                "price": winner["price"]

            }


            st.success(

                f"🛒 {winner['name']} "
                "added to cart!"

            )


    if bundle:

        if st.button(
            "📦 Add Smart Bundle to Cart"
        ):

            st.session_state.cart = {

                "type": "bundle",

                "items": bundle["items"],

                "price": bundle["final_total"]

            }


            st.success(
                "📦 Smart bundle added to cart!"
            )


    # =====================================================
    # CART
    # =====================================================

    if "cart" in st.session_state:

        cart = st.session_state.cart


        st.divider()

        st.subheader(
            "🛒 Your Cart"
        )


        if cart["type"] == "product":

            st.write(
                f"**{cart['product']['name']}**"
            )


            st.write(

                f"Price: "
                f"**₹{cart['price']:,}**"

            )


        else:

            st.write(
                "**Smart Bundle**"
            )


            for item in cart["items"]:

                st.write(

                    f"• {item['name']} "
                    f"— ₹{item['price']:,}"

                )


            st.write(

                f"Bundle Price: "
                f"**₹{cart['price']:,}**"

            )


        # =================================================
        # CHECKOUT
        # =================================================

        st.subheader(
            "💳 Checkout"
        )


        if st.button(
            "💰 Proceed to Checkout"
        ):

            st.success(
                "🎉 Checkout initiated successfully!"
            )


            st.info(

                "Payment gateway integration "
                "will be added later."

            )