# ============================================================
# AI PERSONAL TECH SHOPPER
# FINAL CUSTOMER SHOPPING APPLICATION
# ============================================================

import streamlit as st
import re
from datetime import datetime

from products import products
from cart_manager import CartManager
from analytics import AnalyticsManager


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Personal Tech Shopper",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PRODUCT IMAGES
# ============================================================

PRODUCT_IMAGES = {
    "ApexBook Pro 15":
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1000&q=80",

    "Titan Gaming 16":
        "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?auto=format&fit=crop&w=1000&q=80",

    "ZenBook Creator 15":
        "https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=1000&q=80",

    "NovaBook Air 14":
        "https://images.unsplash.com/photo-1484788984921-03950022c9ef?auto=format&fit=crop&w=1000&q=80",

    "PowerMax Studio 16":
        "https://images.unsplash.com/photo-1593642532400-2682810df593?auto=format&fit=crop&w=1000&q=80",

    "CodeMaster 14":
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1000&q=80",

    "CreatorX Pro":
        "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?auto=format&fit=crop&w=1000&q=80",

    "StudentBook 15":
        "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1000&q=80",

    "NovaPhone X":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=1000&q=80",

    "ApexPhone Pro":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=1000&q=80",

    "Titan Gaming Phone":
        "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?auto=format&fit=crop&w=1000&q=80",

    "PixelView Ultra":
        "https://images.unsplash.com/photo-1556656793-08538906a9f8?auto=format&fit=crop&w=1000&q=80",

    "ZenPhone Lite":
        "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=1000&q=80",

    "UltraCam Pro":
        "https://images.unsplash.com/photo-1512499617640-c2f999fe3f02?auto=format&fit=crop&w=1000&q=80",

    "SoundBuds Pro":
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1000&q=80",

    "GameSound X":
        "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=1000&q=80",

    "StudioPods":
        "https://images.unsplash.com/photo-1545127398-14699f92334b?auto=format&fit=crop&w=1000&q=80",

    "HyperMouse G1":
        "https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=1000&q=80",

    "GameKey RGB":
        "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=1000&q=80",

    "HyperCool X1":
        "https://images.unsplash.com/photo-1625842268584-8f3296236761?auto=format&fit=crop&w=1000&q=80",

    "PowerMax 65W":
        "https://images.unsplash.com/photo-1609592424724-0f3c6f6d6d2c?auto=format&fit=crop&w=1000&q=80",

    "TravelPack Pro":
        "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=1000&q=80"
}


# ============================================================
# SESSION STATE
# ============================================================

if "cart" not in st.session_state:
    st.session_state.cart = CartManager()

if "analytics" not in st.session_state:
    st.session_state.analytics = AnalyticsManager()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

if "discounts" not in st.session_state:
    st.session_state.discounts = {}

if "checkout" not in st.session_state:
    st.session_state.checkout = False

if "order_complete" not in st.session_state:
    st.session_state.order_complete = False

if "last_order" not in st.session_state:
    st.session_state.last_order = None


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* SIDEBAR TEXT VISIBILITY FIX */

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] [data-testid="stMetricLabel"] {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f7f9fc 0%,
                #eef3ff 50%,
                #ffffff 100%
            );
    }

    .hero {
    padding: 35px;
    border-radius: 24px;
    margin-bottom: 25px;
    background:
        linear-gradient(
            135deg,
            #111827,
            #312e81,
            #4f46e5
        );
    color: white;
    box-shadow: 0 12px 35px rgba(0,0,0,0.15);
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
    color: white !important;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
    color: white !important;
}
 {
    color: white !important;
}
   .card {
    background: white;
    color: #111827 !important;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(0,0,0,0.07);
    margin-bottom: 20px;
}

.card *,
.card p,
.card span,
.card div,
.card h1,
.card h2,
.card h3,
.card h4,
.card h5,
.card h6 {
    color: #111827 !important;
}

    .winner-card {
        border: 2px solid #4f46e5;
        box-shadow: 0 12px 30px rgba(79,70,229,0.16);
    }

    .price {
        font-size: 30px;
        font-weight: 800;
    }

    .old-price {
        text-decoration: line-through;
        color: #888;
        font-size: 16px;
    }

    .discount {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: #dcfce7;
        color: #166534;
        font-weight: 700;
    }

    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: #ede9fe;
        color: #5b21b6;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .feature {
    padding: 10px;
    border-radius: 10px;
    background: #f8fafc;
    color: #111827;
    margin-bottom: 6px;
}
    .section-title {
       font-size: 28px;
    font-weight: 800;
    color: #111827 !important;
    margin-top: 20px;
    margin-bottom: 15px;
    }
/* Fix Streamlit text visibility on light background */
[data-testid="stAppViewContainer"] .stMarkdown,
[data-testid="stAppViewContainer"] .stMarkdown p,
[data-testid="stAppViewContainer"] .stMarkdown span,
[data-testid="stAppViewContainer"] .stMarkdown div {
    color: #111827;
}

[data-testid="stAppViewContainer"] h1,
[data-testid="stAppViewContainer"] h2,
[data-testid="stAppViewContainer"] h3,
[data-testid="stAppViewContainer"] h4,
[data-testid="stAppViewContainer"] h5,
[data-testid="stAppViewContainer"] h6 {
    color: #111827 !important;
}

[data-testid="stAppViewContainer"] .stCaption {
    color: #4b5563 !important;
}
    .chat-box {
    background: white;
    color: #111827;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
}

        .success-box {
        padding: 20px;
        border-radius: 18px;
        background: #ecfdf5;
        border: 1px solid #86efac;
    }

/* CART TOTAL SUMMARY - VISIBILITY FIX */

.stMetric {
    background: #ffffff !important;
    border: 1px solid #d1d5db !important;
    border-radius: 16px !important;
    padding: 20px !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08) !important;
}

[data-testid="stMetricLabel"] {
    color: #111827 !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #111827 !important;
    font-weight: 800 !important;
}

[data-testid="stMetricDelta"] {
    color: #166534 !important;
}

    /* ============================================================
       SIDEBAR TEXT VISIBILITY
       ============================================================ */

    [data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div {
    color: white !important;
}

[data-testid="stSidebar"] svg {
    color: white !important;
    fill: white !important;
}



    
/* CHECKOUT FORM TEXT VISIBILITY FIX */

.stTextInput label,
.stTextArea label,
.stRadio > label {
    color: #111827 !important;
    font-weight: 600 !important;
}

.stRadio label {
    color: #111827 !important;
}

[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {
    color: #111827 !important;
}

[data-testid="stRadio"] label {
    color: #111827 !important;
}
   /* ============================================================
   FINAL VISIBILITY FIX
   ============================================================ */

/* CHECKOUT PAYMENT OPTIONS */
[data-testid="stRadio"] label,
[data-testid="stRadio"] label p,
[data-testid="stRadio"] label span,
[data-testid="stRadio"] label div {
    color: #111827 !important;
    opacity: 1 !important;
}

/* PAYMENT METHOD TITLE */
[data-testid="stRadio"] > label {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* SIDEBAR CART METRICS */
[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: #272933 !important;
    border: none !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
    color: #ffffff !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800 !important;
}

[data-testid="stSidebar"] [data-testid="stMetricDelta"] {
    color: #ffffff !important;
}
     </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"₹{int(value):,}"


def get_image(product):
    return PRODUCT_IMAGES.get(
        product.get("name"),
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=1000&q=80"
    )


def extract_budget(text):
    text = text.lower()

    patterns = [
        r"(?:under|below|within|budget(?:\s+of)?|upto|up to)\s*₹?\s*([0-9,]+)",
        r"₹\s*([0-9,]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            try:
                return int(
                    match.group(1).replace(",", "")
                )
            except:
                pass

    return 80000


def detect_category(text):
    text = text.lower()

    if any(
        word in text
        for word in [
            "laptop",
            "notebook",
            "macbook"
        ]
    ):
        return "Laptop"

    if any(
        word in text
        for word in [
            "phone",
            "smartphone",
            "mobile"
        ]
    ):
        return "Smartphone"

    if any(
        word in text
        for word in [
            "headphone",
            "earbuds",
            "audio"
        ]
    ):
        return "Audio"

    if "mouse" in text:
        return "Mouse"

    if "keyboard" in text:
        return "Keyboard"

    return "Laptop"


def extract_requirements(text):
    text = text.lower()

    requirements = []

    mapping = {
        "ai/ml": [
            "ai",
            "ai/ml",
            "machine learning",
            "ml"
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
        "Video Editing": [
            "video editing",
            "editing"
        ],
        "Content Creation": [
            "content creation",
            "creator"
        ],
        "Photography": [
            "photography",
            "camera"
        ],
        "College": [
            "college",
            "student"
        ],
        "Office": [
            "office",
            "work"
        ]
    }

    for name, words in mapping.items():

        if any(
            word in text
            for word in words
        ):
            requirements.append(name)

    if not requirements:
        requirements = [
            "Programming"
        ]

    return requirements


def score_product(product, budget, requirements):

    score = 0

    price = product.get(
        "price",
        0
    )

    use_cases = [
        str(x).lower()
        for x in product.get(
            "use_cases",
            []
        )
    ]

    # Budget
    if price <= budget:
        score += 30
    else:
        score -= 35

    # Requirements
    for requirement in requirements:

        if requirement.lower() in use_cases:
            score += 15

    # Rating
    rating = product.get(
        "rating",
        0
    )

    score += int(
        rating * 4
    )

    # Stock
    if product.get("stock", 0) > 0:
        score += 5

    return max(
        0,
        min(score, 100)
    )


def find_recommendations(
    text
):

    budget = extract_budget(text)

    category = detect_category(text)

    requirements = extract_requirements(
        text
    )

    candidates = []

    for product in products:

        if product.get("category") != category:
            continue

        if product.get("stock", 0) <= 0:
            continue

        product_copy = dict(product)

        product_copy["match_score"] = score_product(
            product,
            budget,
            requirements
        )

        candidates.append(
            product_copy
        )

    candidates.sort(
        key=lambda p: (
            p["match_score"],
            p.get("rating", 0),
            -p.get("price", 0)
        ),
        reverse=True
    )

    return (
        candidates[:2],
        budget,
        category,
        requirements
    )


def calculate_discount(product):

    price = product.get(
        "price",
        0
    )

    # Safe demo negotiation:
    # 5% standard offer, maximum ₹5000
    discount = int(
        min(
            price * 0.05,
            5000
        )
    )

    return discount


def negotiate_discount(
    product,
    target_price=None
):

    price = product.get(
        "price",
        0
    )

    standard_discount = calculate_discount(
        product
    )

    standard_price = price - standard_discount

    if target_price:

        # Accept target if it is not
        # unrealistically low.
        minimum_price = int(
            price * 0.92
        )

        if target_price >= standard_price:

            discount = price - target_price

            return {
                "accepted": True,
                "discount": max(
                    0,
                    discount
                ),
                "final_price": target_price,
                "message":
                    "Great! Your target price is achievable."
            }

        if target_price >= minimum_price:

            discount = price - target_price

            return {
                "accepted": True,
                "discount": discount,
                "final_price": target_price,
                "message":
                    "I negotiated a special target-price offer for you."
            }

        return {
            "accepted": True,
            "discount": standard_discount,
            "final_price": standard_price,
            "message":
                f"I couldn't reach {money(target_price)}, "
                f"but I can offer {money(standard_discount)} off."
        }

    return {
        "accepted": True,
        "discount": standard_discount,
        "final_price": standard_price,
        "message":
            f"Good news! I can offer you "
            f"{money(standard_discount)} off."
    }


def add_message(
    role,
    text
):

    st.session_state.messages.append(
        {
            "role": role,
            "content": text
        }
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🤖 AI Personal Tech Shopper</h1>
        <p>
            Find smarter. Compare faster. Negotiate better.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🛍️ Your Shopping Assistant")

    st.write(
        "Tell me what technology you need "
        "and I'll find the best matches."
    )

    st.divider()

    st.subheader("🛒 Cart")

    cart_summary = (
        st.session_state.cart.get_summary()
    )

    st.metric(
        "Items",
        cart_summary["item_count"]
    )

    st.metric(
        "Cart Total",
        money(cart_summary["total"])
    )

    if cart_summary["discount"] > 0:

        st.success(
            f"Saving {money(cart_summary['discount'])}"
        )

    st.divider()

    if st.button(
        "🗑️ Clear Cart",
        use_container_width=True
    ):

        st.session_state.cart.clear()

        st.rerun()

    if st.button(
        "🔄 Start New Shopping Search",
        use_container_width=True
    ):

        st.session_state.recommendations = []

        st.session_state.selected_product = None

        st.session_state.discounts = {}

        st.session_state.messages = []

        st.session_state.checkout = False

        st.session_state.order_complete = False

        st.rerun()


# ============================================================
# SHOPPING CHAT
# ============================================================

st.markdown(
    '<div class="section-title">💬 What are you looking for?</div>',
    unsafe_allow_html=True
)

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


user_message = st.chat_input(
    "Example: I need a laptop for AI and gaming under ₹80000"
)


# ============================================================
# CHAT PROCESSING
# ============================================================

if user_message:

    add_message(
        "user",
        user_message
    )

    lower = user_message.lower()


    # --------------------------------------------------------
    # DISCOUNT REQUEST
    # --------------------------------------------------------

    discount_words = [
        "discount",
        "give me a discount",
        "give discount",
        "reduce the price",
        "lower the price",
        "better price",
        "better deal",
        "cheaper",
        "negotiate",
        "negotiate price",
        "special price",
        "best price",
        "deal"
    ]

    is_discount_request = any(
        word in lower
        for word in discount_words
    )


    # --------------------------------------------------------
    # TARGET PRICE
    # --------------------------------------------------------

    target_match = re.search(
        r"(?:₹|rs\.?|rupees?)\s*([0-9,]+)",
        lower
    )

    target_price = None

    if target_match:

        try:

            target_price = int(
                target_match.group(1).replace(
                    ",",
                    ""
                )
            )

        except:

            target_price = None


    # --------------------------------------------------------
    # DISCOUNT / NEGOTIATION
    # --------------------------------------------------------

    if (
        is_discount_request
        or target_price is not None
    ):

        # ----------------------------------------------------
        # NO PRODUCT SELECTED
        # ----------------------------------------------------

        if not st.session_state.selected_product:

            response = (
                "🤝 **Absolutely! I can try to get you a better price.**\n\n"
                "First, tell me which product you want a discount on "
                "or ask me to find a product for you.\n\n"
                "For example:\n"
                "- **Give me a discount on ApexBook Pro 15**\n"
                "- **Can you reduce the price of the best laptop?**\n"
                "- **Find me a laptop under ₹80000 and get me a discount.**"
            )

            add_message(
                "assistant",
                response
            )

            st.rerun()


        # ----------------------------------------------------
        # PRODUCT SELECTED
        # ----------------------------------------------------

        product = (
            st.session_state.selected_product
        )

        negotiation = negotiate_discount(
            product,
            target_price
        )

        discount = negotiation["discount"]


        st.session_state.discounts[
            product["name"]
        ] = discount


        try:

            st.session_state.analytics.record_negotiation(
                product["name"],
                discount
            )

        except Exception:

            pass


        response = (
            f"🤝 **Deal found!**\n\n"
            f"**Product:** "
            f"{product['name']}\n\n"
            f"**Original price:** "
            f"{money(product['price'])}\n\n"
            f"**Discount:** "
            f"{money(discount)}\n\n"
            f"**Your final price:** "
            f"{money(negotiation['final_price'])}\n\n"
            f"{negotiation['message']}\n\n"
            f"🛒 **The negotiated discount will be used "
            f"when you add this product to your cart.**"
        )


        add_message(
            "assistant",
            response
        )


        st.rerun()


    # --------------------------------------------------------
    # NORMAL PRODUCT SEARCH
    # --------------------------------------------------------

    recommendations, budget, category, requirements = (
        find_recommendations(
            user_message
        )
    )


    st.session_state.recommendations = (
        recommendations
    )


    if recommendations:

        best = recommendations[0]

        st.session_state.selected_product = (
            best
        )


        for product in recommendations:

            try:

                st.session_state.analytics.record_product_view(
                    product["name"]
                )

                st.session_state.analytics.record_recommendation(
                    product["name"]
                )

            except Exception:

                pass


        response = (
            f"🎯 I found the **top {len(recommendations)} "
            f"matches** for your request.\n\n"
            f"Your budget: {money(budget)}\n\n"
            f"Category: {category}\n\n"
            f"Requirements: "
            f"{', '.join(requirements)}"
        )


    else:

        response = (
            "I couldn't find suitable products "
            "for that request."
        )


    add_message(
        "assistant",
        response
    )


    st.rerun()


# ============================================================
# RECOMMENDATIONS
# ============================================================

recommendations = (
    st.session_state.recommendations
)


if recommendations:

    st.markdown(
        '<div class="section-title">🏆 Top Recommendations</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "I've limited this to the two strongest matches "
        "instead of showing you a huge product list."
    )

    columns = st.columns(
        len(recommendations)
    )

    for index, product in enumerate(
        recommendations
    ):

        with columns[index]:

            is_best = index == 0

            card_class = (
                "card winner-card"
                if is_best
                else "card"
            )

            st.markdown(
                f'<div class="{card_class}">',
                unsafe_allow_html=True
            )

            if is_best:

                st.markdown(
                    '<span class="badge">'
                    '🏆 BEST MATCH'
                    '</span>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    '<span class="badge">'
                    '⭐ ALTERNATIVE'
                    '</span>',
                    unsafe_allow_html=True
                )

            st.image(
                get_image(product),
                use_container_width=True
            )

            st.subheader(
                product["name"]
            )

            st.write(
                f"**{product['brand']}**"
            )

            st.markdown(
                f'<div class="price">'
                f'{money(product["price"])}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.write(
                f"⭐ {product.get('rating', 'N/A')}/5"
            )

            st.progress(
                product["match_score"] / 100
            )

            st.write(
                f"🎯 Match: "
                f"**{product['match_score']}/100**"
            )

            st.markdown(
                f"""
                <div class="feature">
                🧠 <b>Processor:</b>
                {product.get("processor", "N/A")}
                </div>

                <div class="feature">
                🧮 <b>RAM:</b>
                {product.get("ram", "N/A")}
                </div>

                <div class="feature">
                💾 <b>Storage:</b>
                {product.get("storage", "N/A")}
                </div>

                <div class="feature">
                🎮 <b>GPU:</b>
                {product.get("gpu", "N/A")}
                </div>

                <div class="feature">
                🖥️ <b>Display:</b>
                {product.get("display", "N/A")}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                "### Best for"
            )

            for use_case in product.get(
                "use_cases",
                []
            ):

                st.write(
                    f"✓ {use_case}"
                )

            if st.button(
                "🏆 Choose This Product",
                key=f"choose_{index}",
                use_container_width=True
            ):

                st.session_state.selected_product = (
                    product
                )

                st.success(
                    f"{product['name']} selected."
                )

                st.rerun()

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# ============================================================
# SELECTED PRODUCT
# ============================================================

selected = (
    st.session_state.selected_product
)


if selected:

    st.markdown(
        '<div class="section-title">'
        '🛍️ Your Selected Product'
        '</div>',
        unsafe_allow_html=True
    )

    discount = st.session_state.discounts.get(
        selected["name"],
        0
    )

    final_price = max(
        selected["price"] - discount,
        0
    )

    col1, col2 = st.columns(
        [1.3, 1]
    )

    with col1:

        st.image(
            get_image(selected),
            use_container_width=True
        )

    with col2:

        st.markdown(
            f"## {selected['name']}"
        )

        st.write(
            f"Brand: **{selected['brand']}**"
        )

        st.write(
            f"⭐ Rating: "
            f"**{selected.get('rating', 'N/A')}/5**"
        )

        if discount > 0:

            st.markdown(
                f'<span class="old-price">'
                f'{money(selected["price"])}'
                f'</span>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="price">'
                f'{money(final_price)}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<span class="discount">'
                f'💰 You save {money(discount)}'
                f'</span>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<div class="price">'
                f'{money(selected["price"])}'
                f'</div>',
                unsafe_allow_html=True
            )

        st.write(
            f"📦 Stock available: "
            f"**{selected.get('stock', 0)}**"
        )


# ============================================================
# NEGOTIATION
# ============================================================

if selected:

    st.markdown(
        '<div class="section-title">'
        '🤝 Get a Better Price'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "You can negotiate directly here — "
        "no API is required."
    )

    neg_col1, neg_col2 = st.columns(
        [1, 1]
    )

    with neg_col1:

        if st.button(
            "💰 Give Me a Discount",
            type="primary",
            use_container_width=True
        ):

            result = negotiate_discount(
                selected
            )

            discount = result["discount"]

            st.session_state.discounts[
                selected["name"]
            ] = discount

            try:

                st.session_state.analytics.record_negotiation(
                    selected["name"],
                    discount
                )

            except Exception:
                pass

            add_message(
                "assistant",
                (
                    f"🤝 **Deal found!**\n\n"
                    f"Original price: "
                    f"{money(selected['price'])}\n\n"
                    f"Discount: "
                    f"{money(discount)}\n\n"
                    f"Final price: "
                    f"{money(result['final_price'])}\n\n"
                    f"Add it to your cart to use this deal."
                )
            )

            st.rerun()

    with neg_col2:

        target = st.number_input(
            "🎯 Request Your Target Price",
            min_value=1000,
            max_value=max(
                selected["price"],
                1000
            ),
            value=max(
                selected["price"] - 5000,
                1000
            ),
            step=1000,
            key="target_price_box"
        )

        if st.button(
            "🤝 Negotiate Target Price",
            use_container_width=True
        ):

            result = negotiate_discount(
                selected,
                target
            )

            discount = result["discount"]

            st.session_state.discounts[
                selected["name"]
            ] = discount

            try:

                st.session_state.analytics.record_negotiation(
                    selected["name"],
                    discount
                )

            except Exception:
                pass

            add_message(
                "assistant",
                (
                    f"🎯 **Negotiation Result**\n\n"
                    f"Your target: "
                    f"{money(target)}\n\n"
                    f"Original price: "
                    f"{money(selected['price'])}\n\n"
                    f"Discount offered: "
                    f"{money(discount)}\n\n"
                    f"Final price: "
                    f"{money(result['final_price'])}\n\n"
                    f"{result['message']}"
                )
            )

            st.rerun()


# ============================================================
# ADD TO CART
# ============================================================

if selected:

    st.divider()

    st.markdown(
        '<div class="section-title">🛒 Add to Cart</div>',
        unsafe_allow_html=True
    )

    current_discount = (
        st.session_state.discounts.get(
            selected["name"],
            0
        )
    )

    cart_col1, cart_col2, cart_col3 = st.columns(
        [1, 1, 1]
    )

    with cart_col1:

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=min(
                10,
                selected.get(
                    "stock",
                    10
                )
            ),
            value=1,
            step=1,
            key="cart_quantity"
        )

    with cart_col2:

        if current_discount > 0:

            st.metric(
                "Your Discount",
                money(current_discount)
            )

        else:

            st.metric(
                "Discount",
                "₹0"
            )

    with cart_col3:

        cart_price = max(
            selected["price"] -
            current_discount,
            0
        )

        st.metric(
            "Your Price",
            money(cart_price)
        )

    if st.button(
        "🛒 ADD TO CART",
        type="primary",
        use_container_width=True,
        key="final_add_cart"
    ):

        st.session_state.cart.add_product(
            selected,
            quantity=quantity,
            discount=current_discount
        )

        try:

            st.session_state.analytics.record_cart_event(
                "ADD",
                selected["name"]
            )

        except Exception:
            pass

        st.success(
            f"✅ {selected['name']} added to your cart!"
        )

        st.balloons()


# ============================================================
# CART
# ============================================================

cart_summary = (
    st.session_state.cart.get_summary()
)

if cart_summary["items"]:

    st.divider()

    st.markdown(
        '<div class="section-title">🛒 Your Cart</div>',
        unsafe_allow_html=True
    )

    for item in cart_summary["items"]:

        item_col1, item_col2, item_col3, item_col4 = (
            st.columns([3, 1, 1, 1])
        )

        with item_col1:

            st.write(
                f"### {item['name']}"
            )

            st.write(
                f"Quantity: {item['quantity']}"
            )

        with item_col2:

            st.write(
                "Unit price"
            )

            st.write(
                money(item["price"])
            )

        with item_col3:

            st.write(
                "Discount"
            )

            st.success(
                money(item["discount"])
            )

        with item_col4:

            if st.button(
                "❌ Remove",
                key=f"remove_{item['name']}"
            ):

                st.session_state.cart.remove_product(
                    item["name"]
                )

                try:

                    st.session_state.analytics.record_cart_event(
                        "REMOVE",
                        item["name"]
                    )

                except Exception:
                    pass

                st.rerun()

    st.divider()

    sum1, sum2, sum3 = st.columns(3)

    with sum1:

        st.metric(
            "Subtotal",
            money(
                cart_summary["subtotal"]
            )
        )

    with sum2:

        st.metric(
            "Total Discount",
            money(
                cart_summary["discount"]
            )
        )

    with sum3:

        st.metric(
            "Final Total",
            money(
                cart_summary["total"]
            )
        )

    if st.button(
        "💳 Proceed to Checkout",
        type="primary",
        use_container_width=True
    ):

        st.session_state.checkout = True

        st.rerun()


# ============================================================
# CHECKOUT
# ============================================================

if (
    st.session_state.checkout
    and cart_summary["items"]
    and not st.session_state.order_complete
):

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '💳 Secure Demo Checkout'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        "This is a project demonstration checkout. "
        "No real payment is processed."
    )

    check_left, check_right = st.columns(
        [1.2, 1]
    )

    with check_left:

        st.subheader(
            "📦 Delivery Details"
        )

        customer_name = st.text_input(
            "Full Name",
            key="checkout_name"
        )

        address = st.text_area(
            "Delivery Address",
            key="checkout_address"
        )

        phone = st.text_input(
            "Phone Number",
            key="checkout_phone"
        )

    with check_right:

        st.subheader(
            "💳 Payment Method"
        )

        payment_method = st.radio(
            "Choose payment method",
            [
                "UPI",
                "Credit / Debit Card",
                "Cash on Delivery"
            ],
            key="payment_method"
        )

        if payment_method == "UPI":

            st.text_input(
                "UPI ID",
                placeholder="example@upi",
                key="upi_id"
            )

        elif payment_method == "Credit / Debit Card":

            st.text_input(
                "Card Number",
                placeholder="XXXX XXXX XXXX XXXX",
                key="card_number"
            )

            card1, card2 = st.columns(2)

            with card1:

                st.text_input(
                    "Expiry",
                    placeholder="MM/YY",
                    key="expiry"
                )

            with card2:

                st.text_input(
                    "CVV",
                    type="password",
                    key="cvv"
                )

        else:

            st.success(
                "You will pay when your order is delivered."
            )

    st.divider()

    st.subheader(
        "🧾 Order Summary"
    )

    for item in cart_summary["items"]:

        final_item_price = max(
            item["price"] -
            item["discount"],
            0
        )

        st.write(
            f"**{item['name']}** × "
            f"{item['quantity']} — "
            f"{money(final_item_price * item['quantity'])}"
        )

    st.divider()

    st.markdown(
        f"### 💰 Final Amount: {money(cart_summary['total'])}"
    )

    if st.button(
        "✅ Place Demo Order",
        type="primary",
        use_container_width=True
    ):

        if not customer_name.strip():

            st.error(
                "Please enter your name."
            )

        elif not address.strip():

            st.error(
                "Please enter your delivery address."
            )

        elif not phone.strip():

            st.error(
                "Please enter your phone number."
            )

        else:

            order = (
                st.session_state.analytics.record_order(
                    cart_summary["items"],
                    cart_summary["total"],
                    cart_summary["discount"]
                )
            )

            st.session_state.last_order = order

            st.session_state.order_complete = True

            st.session_state.cart.clear()

            st.rerun()


# ============================================================
# ORDER CONFIRMATION
# ============================================================

if st.session_state.order_complete:

    st.divider()

    st.markdown(
        """
        <div class="success-box">
            <h1>🎉 Order Confirmed!</h1>
            <p>
                Your demo order has been successfully placed.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    order = (
        st.session_state.last_order
    )

    if order:

        st.write(
            f"### 🧾 Order ID: "
            f"#{order.get('order_id', 'N/A')}"
        )

        st.write(
            f"💰 Total Paid: "
            f"**{money(order.get('total', 0))}**"
        )

        st.write(
            f"🎁 Discount: "
            f"**{money(order.get('discount', 0))}**"
        )

        st.write(
            f"🕐 Order Time: "
            f"{order.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}"
        )

    if st.button(
        "🛍️ Continue Shopping",
        use_container_width=True
    ):

        st.session_state.order_complete = False

        st.session_state.checkout = False

        st.session_state.last_order = None

        st.rerun()


# ============================================================
# AGENT DECISION TRACE
# ============================================================

if recommendations:

    st.divider()

    with st.expander(
        "🧠 How the AI Shopper Made the Recommendation"
    ):

        st.write(
            "The shopping agent evaluated:"
        )

        st.write(
            "→ Customer budget"
        )

        st.write(
            "→ Product category"
        )

        st.write(
            "→ Customer requirements"
        )

        st.write(
            "→ Product use cases"
        )

        st.write(
            "→ Product rating"
        )

        st.write(
            "→ Availability"
        )

        st.write(
            "→ Final match score"
        )

        st.success(
            "The interface intentionally displays only "
            "the two strongest matches so the customer "
            "isn't overwhelmed by the entire catalog."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; opacity:0.65;">
        🤖 AI Personal Tech Shopper
        <br>
        Intelligent Recommendations • Negotiation • Cart • Checkout
    </div>
    """,
    unsafe_allow_html=True
)