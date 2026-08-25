# =========================================================
# AI PERSONAL TECH SHOPPER
# MERCHANT ANALYTICS DASHBOARD
# =========================================================

import streamlit as st

from analytics import (
    AnalyticsManager,
    create_demo_data
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Merchant Analytics",

    page_icon="📊",

    layout="wide"

)


# =========================================================
# LOAD ANALYTICS
# =========================================================

analytics = create_demo_data()

summary = analytics.get_summary()


# =========================================================
# HEADER
# =========================================================

st.title(
    "📊 Merchant Analytics"
)

st.write(

    "AI-powered insights from customer "
    "shopping activity."

)


st.divider()


# =========================================================
# MAIN METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(
    4
)


with col1:

    st.metric(

        "💰 Revenue",

        f"₹{summary['total_revenue']:,}"

    )


with col2:

    st.metric(

        "🛒 Orders",

        summary["total_orders"]

    )


with col3:

    st.metric(

        "📦 Products Sold",

        summary["products_sold"]

    )


with col4:

    st.metric(

        "💵 Avg Order Value",

        f"₹{summary['average_order_value']:,.0f}"

    )


st.divider()


# =========================================================
# SECONDARY METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(
    4
)


with col1:

    st.metric(

        "🤖 Recommendations",

        summary[
            "recommendations"
        ]

    )


with col2:

    st.metric(

        "🤝 Negotiations",

        summary[
            "negotiations"
        ]

    )


with col3:

    st.metric(

        "🛒 Cart Additions",

        summary[
            "cart_additions"
        ]

    )


with col4:

    st.metric(

        "💸 Discounts Given",

        f"₹{summary['total_discounts']:,}"

    )


st.divider()


# =========================================================
# TOP PRODUCTS
# =========================================================

st.header(
    "🏆 Top Selling Products"
)


top_products = summary[
    "top_products"
]


if top_products:

    for index, (
        product,
        quantity
    ) in enumerate(

        top_products,

        start=1

    ):

        col1, col2, col3 = st.columns(
            3
        )


        with col1:

            st.write(

                f"**#{index} "
                f"{product}**"

            )


        with col2:

            st.write(

                f"📦 {quantity} sold"

            )


        with col3:

            if index == 1:

                st.success(
                    "🥇 Best Seller"
                )

            elif index == 2:

                st.info(
                    "🥈 Second"
                )

            else:

                st.write(
                    "Product"
                )


else:

    st.info(
        "No sales data yet."
    )


st.divider()


# =========================================================
# TOP RECOMMENDATIONS
# =========================================================

st.header(
    "🤖 AI Recommendation Performance"
)


recommendations = summary[
    "top_recommendations"
]


if recommendations:

    for product, count in recommendations:

        st.write(

            f"**{product}** — "
            f"{count} recommendation(s)"

        )

else:

    st.info(
        "No recommendation data yet."
    )


st.divider()


# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.header(
    "🧠 AI Business Insights"
)


if summary["total_orders"] > 0:

    if (

        summary[
            "average_order_value"
        ]

        >=

        50000

    ):

        st.success(

            "💰 Customers are generating "
            "high-value orders."

        )


    if summary[
        "negotiations"
    ] > 0:

        st.info(

            "🤝 Customers are actively "
            "negotiating prices. Consider "
            "using targeted offers to "
            "improve conversion."

        )


    if summary[
        "recommendations"
    ] > summary[
        "total_orders"
    ]:

        st.info(

            "🤖 The AI agent is making "
            "multiple recommendations "
            "before purchases."

        )


    if summary[
        "cart_additions"
    ] > 0:

        st.success(

            "🛒 Customers are actively "
            "adding products to carts."

        )


else:

    st.warning(

        "Not enough data to generate "
        "business insights."

    )


st.divider()


# =========================================================
# AGENT ACTIVITY
# =========================================================

st.header(
    "🤖 Agent Activity"
)


col1, col2 = st.columns(
    2
)


with col1:

    st.metric(

        "Product Recommendations",

        summary[
            "recommendations"
        ]

    )


    st.metric(

        "Price Negotiations",

        summary[
            "negotiations"
        ]

    )


with col2:

    st.metric(

        "Cart Additions",

        summary[
            "cart_additions"
        ]

    )


    st.metric(

        "Cart Removals",

        summary[
            "cart_removals"
        ]

    )


st.divider()


st.caption(

    "AI Personal Tech Shopper • "
    "Merchant Intelligence Layer"

)