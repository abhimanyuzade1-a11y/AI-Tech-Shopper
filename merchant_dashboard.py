import streamlit as st
import json
import os

from merchant_rules import MERCHANT_RULES


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Merchant Dashboard",

    page_icon="🏪",

    layout="wide"

)


# =========================================================
# TITLE
# =========================================================

st.title(
    "🏪 Merchant Control Center"
)

st.write(
    "Manage your product catalog and control "
    "the business rules used by the AI commerce agent."
)


st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "🏪 Merchant Controls"
)

st.sidebar.write(
    "Configure the rules that control "
    "agent decisions."
)


# =========================================================
# LOAD PRODUCT CATALOG
# =========================================================

possible_files = [

    "products.json",

    "product_catalog.json",

    "catalog.json",

    "products.py"

]


product_file = None


for file in possible_files:

    if os.path.exists(file):

        product_file = file

        break


products = []


if product_file:

    try:

        if product_file.endswith(".json"):

            with open(

                product_file,

                "r",

                encoding="utf-8"

            ) as file:

                products = json.load(file)


        elif product_file.endswith(".py"):

            from products import products

    except Exception as error:

        st.error(
            "Could not load product catalog."
        )

        st.code(
            str(error)
        )


# =========================================================
# NORMALIZE PRODUCTS
# =========================================================

if isinstance(products, dict):

    if "products" in products:

        products = products["products"]

    else:

        products = list(
            products.values()
        )


# =========================================================
# DASHBOARD TABS
# =========================================================

tab1, tab2, tab3 = st.tabs(

    [
        "📦 Products",
        "⚙️ Agent Rules",
        "📊 Business Overview"
    ]

)


# =========================================================
# TAB 1 — PRODUCTS
# =========================================================

with tab1:

    st.header(
        "📦 Product Catalog"
    )


    if products:

        total_products = len(
            products
        )


        total_value = sum(

            product.get(
                "price",
                0
            )

            for product in products

        )


        average_price = (

            total_value /

            total_products

        )


        col1, col2, col3 = st.columns(
            3
        )


        with col1:

            st.metric(

                "📦 Total Products",

                total_products

            )


        with col2:

            st.metric(

                "💰 Catalog Value",

                f"₹{total_value:,.0f}"

            )


        with col3:

            st.metric(

                "📊 Average Price",

                f"₹{average_price:,.0f}"

            )


        st.divider()


        search = st.text_input(

            "🔎 Search products",

            placeholder=(
                "Search by product name..."
            )

        )


        filtered_products = products


        if search:

            filtered_products = [

                product

                for product in products

                if search.lower()
                in product.get(
                    "name",
                    ""
                ).lower()

            ]


        for product in filtered_products:

            with st.container():

                col1, col2, col3, col4 = st.columns(
                    4
                )


                with col1:

                    st.subheader(

                        product.get(
                            "name",
                            "Unknown"
                        )

                    )

                    st.write(

                        product.get(
                            "category",
                            "Unknown"
                        )

                    )


                with col2:

                    st.write(
                        "**Price**"
                    )

                    st.write(

                        f"₹{product.get('price', 0):,}"

                    )


                with col3:

                    st.write(
                        "**Rating**"
                    )

                    st.write(

                        f"⭐ "
                        f"{product.get('rating', 'N/A')}"

                    )


                with col4:

                    st.write(
                        "**Stock**"
                    )

                    stock = product.get(

                        "stock",

                        product.get(
                            "available",
                            True
                        )

                    )


                    if isinstance(
                        stock,
                        bool
                    ):

                        if stock:

                            st.success(
                                "Available"
                            )

                        else:

                            st.error(
                                "Out of Stock"
                            )

                    else:

                        st.write(
                            str(stock)
                        )


                st.divider()


    else:

        st.warning(
            "No product catalog found."
        )


# =========================================================
# TAB 2 — AGENT RULES
# =========================================================

with tab2:

    st.header(
        "⚙️ AI Agent Business Rules"
    )


    st.write(

        "These settings determine how much "
        "freedom the AI agent has when making "
        "commerce decisions."

    )


    st.divider()


    # =====================================================
    # NEGOTIATION
    # =====================================================

    st.subheader(
        "🤝 Negotiation Rules"
    )


    maximum_negotiation_discount = st.number_input(

        "Maximum Negotiation Discount (₹)",

        min_value=0,

        max_value=50000,

        value=int(

            MERCHANT_RULES.get(

                "maximum_negotiation_discount",

                3000

            )

        ),

        step=500

    )


    maximum_discount_percent = st.slider(

        "Maximum Discount Percentage",

        min_value=0,

        max_value=50,

        value=int(

            MERCHANT_RULES.get(

                "maximum_discount_percent",

                10

            )

        )

    )


    st.divider()


    # =====================================================
    # BUNDLE
    # =====================================================

    st.subheader(
        "📦 Bundle Rules"
    )


    bundle_discount_percent = st.slider(

        "Bundle Discount Percentage",

        min_value=0,

        max_value=30,

        value=int(

            MERCHANT_RULES.get(

                "bundle_discount_percent",

                5

            )

        )

    )


    maximum_bundle_discount = st.number_input(

        "Maximum Bundle Discount (₹)",

        min_value=0,

        max_value=50000,

        value=int(

            MERCHANT_RULES.get(

                "maximum_bundle_discount",

                5000

            )

        ),

        step=500

    )


    st.divider()


    # =====================================================
    # RECOVERY
    # =====================================================

    st.subheader(
        "🛒 Cart Recovery Rules"
    )


    recovery_discount_percent = st.slider(

        "Recovery Discount Percentage",

        min_value=0,

        max_value=20,

        value=int(

            MERCHANT_RULES.get(

                "recovery_discount_percent",

                5

            )

        )

    )


    maximum_recovery_discount = st.number_input(

        "Maximum Recovery Discount (₹)",

        min_value=0,

        max_value=50000,

        value=int(

            MERCHANT_RULES.get(

                "maximum_recovery_discount",

                2000

            )

        ),

        step=500

    )


    st.divider()


    # =====================================================
    # INVENTORY
    # =====================================================

    st.subheader(
        "📦 Inventory Rules"
    )


    low_stock_threshold = st.number_input(

        "Low Stock Threshold",

        min_value=0,

        max_value=100,

        value=int(

            MERCHANT_RULES.get(

                "low_stock_threshold",

                5

            )

        )

    )


    st.divider()


    # =====================================================
    # SAVE RULES
    # =====================================================

    if st.button(

        "💾 Save Agent Rules",

        type="primary"

    ):

        MERCHANT_RULES[

            "maximum_negotiation_discount"

        ] = maximum_negotiation_discount


        MERCHANT_RULES[

            "maximum_discount_percent"

        ] = maximum_discount_percent


        MERCHANT_RULES[

            "bundle_discount_percent"

        ] = bundle_discount_percent


        MERCHANT_RULES[

            "maximum_bundle_discount"

        ] = maximum_bundle_discount


        MERCHANT_RULES[

            "recovery_discount_percent"

        ] = recovery_discount_percent


        MERCHANT_RULES[

            "maximum_recovery_discount"

        ] = maximum_recovery_discount


        MERCHANT_RULES[

            "low_stock_threshold"

        ] = low_stock_threshold


        st.success(

            "✅ Agent business rules updated!"

        )


        st.info(

            "The AI agent will use these "
            "rules for future decisions."

        )


# =========================================================
# TAB 3 — BUSINESS OVERVIEW
# =========================================================

with tab3:

    st.header(
        "📊 Business Overview"
    )


    st.subheader(
        "Current Agent Configuration"
    )


    col1, col2 = st.columns(
        2
    )


    with col1:

        st.metric(

            "Maximum Negotiation",

            f"₹{MERCHANT_RULES.get('maximum_negotiation_discount', 0):,}"

        )


        st.metric(

            "Bundle Discount",

            f"{MERCHANT_RULES.get('bundle_discount_percent', 0)}%"

        )


    with col2:

        st.metric(

            "Maximum Recovery",

            f"₹{MERCHANT_RULES.get('maximum_recovery_discount', 0):,}"

        )


        st.metric(

            "Low Stock Threshold",

            MERCHANT_RULES.get(

                "low_stock_threshold",

                0

            )

        )


    st.divider()


    st.success(

        "🧠 The AI agent operates within "
        "merchant-defined business policies."

    )


    st.write(

        "This prevents the agent from making "
        "uncontrolled pricing decisions."

    )