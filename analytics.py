# =========================================================
# AI PERSONAL TECH SHOPPER
# MERCHANT ANALYTICS ENGINE
# =========================================================

import json
import os
from datetime import datetime


ANALYTICS_FILE = "analytics_data.json"


# =========================================================
# ANALYTICS MANAGER
# =========================================================

class AnalyticsManager:

    def __init__(self):

        self.data = {

            "orders": [],

            "recommendations": [],

            "cart_events": [],

            "negotiations": [],

            "product_views": []

        }

        self.load()


    # =====================================================
    # LOAD DATA
    # =====================================================

    def load(self):

        if not os.path.exists(
            ANALYTICS_FILE
        ):

            return


        try:

            with open(

                ANALYTICS_FILE,

                "r",

                encoding="utf-8"

            ) as file:

                loaded_data = json.load(file)


            if isinstance(
                loaded_data,
                dict
            ):

                self.data.update(
                    loaded_data
                )


        except Exception:

            pass


    # =====================================================
    # SAVE DATA
    # =====================================================

    def save(self):

        with open(

            ANALYTICS_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.data,

                file,

                indent=4

            )


    # =====================================================
    # TIMESTAMP
    # =====================================================

    def timestamp(self):

        return datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )


    # =====================================================
    # RECORD PRODUCT VIEW
    # =====================================================

    def record_product_view(

        self,

        product_name

    ):

        self.data[
            "product_views"
        ].append({

            "product":
                product_name,

            "timestamp":
                self.timestamp()

        })


        self.save()


    # =====================================================
    # RECORD RECOMMENDATION
    # =====================================================

    def record_recommendation(

        self,

        product_name

    ):

        self.data[
            "recommendations"
        ].append({

            "product":
                product_name,

            "timestamp":
                self.timestamp()

        })


        self.save()


    # =====================================================
    # RECORD CART EVENT
    # =====================================================

    def record_cart_event(

        self,

        event,

        product_name

    ):

        self.data[
            "cart_events"
        ].append({

            "event":
                event,

            "product":
                product_name,

            "timestamp":
                self.timestamp()

        })


        self.save()


    # =====================================================
    # RECORD NEGOTIATION
    # =====================================================

    def record_negotiation(

        self,

        product_name,

        discount

    ):

        self.data[
            "negotiations"
        ].append({

            "product":
                product_name,

            "discount":
                discount,

            "timestamp":
                self.timestamp()

        })


        self.save()


    # =====================================================
    # RECORD ORDER
    # =====================================================

    def record_order(

        self,

        order_items,

        total,

        discount=0

    ):

        order = {

            "order_id":
                len(
                    self.data["orders"]
                ) + 1,

            "items":
                order_items,

            "total":
                total,

            "discount":
                discount,

            "timestamp":
                self.timestamp()

        }


        self.data[
            "orders"
        ].append(

            order

        )


        self.save()


        return order


    # =====================================================
    # TOTAL ORDERS
    # =====================================================

    def total_orders(self):

        return len(

            self.data[
                "orders"
            ]

        )


    # =====================================================
    # TOTAL REVENUE
    # =====================================================

    def total_revenue(self):

        return sum(

            order.get(
                "total",
                0
            )

            for order in self.data[
                "orders"
            ]

        )


    # =====================================================
    # TOTAL DISCOUNTS
    # =====================================================

    def total_discounts(self):

        return sum(

            order.get(
                "discount",
                0
            )

            for order in self.data[
                "orders"
            ]

        )


    # =====================================================
    # PRODUCTS SOLD
    # =====================================================

    def products_sold(self):

        total = 0


        for order in self.data[
            "orders"
        ]:

            for item in order.get(
                "items",
                []
            ):

                total += item.get(

                    "quantity",

                    1

                )


        return total


    # =====================================================
    # AVERAGE ORDER VALUE
    # =====================================================

    def average_order_value(self):

        orders = self.total_orders()


        if orders == 0:

            return 0


        return (

            self.total_revenue()

            /

            orders

        )


    # =====================================================
    # TOP PRODUCTS
    # =====================================================

    def top_products(

        self,

        limit=5

    ):

        product_sales = {}


        for order in self.data[
            "orders"
        ]:

            for item in order.get(
                "items",
                []
            ):

                name = item.get(

                    "name",

                    "Unknown"

                )


                quantity = item.get(

                    "quantity",

                    1

                )


                product_sales[name] = (

                    product_sales.get(
                        name,
                        0
                    )

                    +

                    quantity

                )


        sorted_products = sorted(

            product_sales.items(),

            key=lambda item:
                item[1],

            reverse=True

        )


        return sorted_products[
            :limit
        ]


    # =====================================================
    # TOP RECOMMENDED PRODUCTS
    # =====================================================

    def top_recommendations(

        self,

        limit=5

    ):

        recommendations = {}


        for item in self.data[
            "recommendations"
        ]:

            product = item.get(

                "product",

                "Unknown"

            )


            recommendations[product] = (

                recommendations.get(
                    product,
                    0
                )

                +

                1

            )


        return sorted(

            recommendations.items(),

            key=lambda item:
                item[1],

            reverse=True

        )[:limit]


    # =====================================================
    # CART EVENT COUNT
    # =====================================================

    def cart_event_count(

        self,

        event_name

    ):

        return sum(

            1

            for event in self.data[
                "cart_events"
            ]

            if event.get(
                "event"
            ) == event_name

        )


    # =====================================================
    # NEGOTIATION COUNT
    # =====================================================

    def negotiation_count(self):

        return len(

            self.data[
                "negotiations"
            ]

        )


    # =====================================================
    # SUMMARY
    # =====================================================

    def get_summary(self):

        return {

            "total_orders":
                self.total_orders(),

            "total_revenue":
                self.total_revenue(),

            "total_discounts":
                self.total_discounts(),

            "products_sold":
                self.products_sold(),

            "average_order_value":
                self.average_order_value(),

            "recommendations":
                len(
                    self.data[
                        "recommendations"
                    ]
                ),

            "negotiations":
                self.negotiation_count(),

            "cart_additions":
                self.cart_event_count(
                    "ADD"
                ),

            "cart_removals":
                self.cart_event_count(
                    "REMOVE"
                ),

            "top_products":
                self.top_products(),

            "top_recommendations":
                self.top_recommendations()

        }


# =========================================================
# DEMO DATA
# =========================================================

def create_demo_data():

    analytics = AnalyticsManager()


    # Avoid adding demo data repeatedly

    if analytics.total_orders() > 0:

        return analytics


    analytics.record_product_view(

        "ApexBook Pro 15"

    )


    analytics.record_product_view(

        "Titan Gaming 16"

    )


    analytics.record_product_view(

        "ZenBook Creator 15"

    )


    analytics.record_recommendation(

        "ApexBook Pro 15"

    )


    analytics.record_recommendation(

        "ApexBook Pro 15"

    )


    analytics.record_recommendation(

        "Titan Gaming 16"

    )


    analytics.record_cart_event(

        "ADD",

        "ApexBook Pro 15"

    )


    analytics.record_cart_event(

        "ADD",

        "HyperMouse G1"

    )


    analytics.record_negotiation(

        "ApexBook Pro 15",

        3000

    )


    analytics.record_order(

        [

            {

                "name":
                    "ApexBook Pro 15",

                "quantity":
                    1

            },

            {

                "name":
                    "HyperMouse G1",

                "quantity":
                    1

            }

        ],

        74298,

        3200

    )


    analytics.record_order(

        [

            {

                "name":
                    "Titan Gaming 16",

                "quantity":
                    1

            }

        ],

        79999,

        0

    )


    return analytics


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    analytics = create_demo_data()


    summary = analytics.get_summary()


    print()

    print(
        "=========================================="
    )

    print(
        "        📊 MERCHANT ANALYTICS"
    )

    print(
        "=========================================="
    )

    print()


    print(

        "Total Orders:",

        summary[
            "total_orders"
        ]

    )


    print(

        "Total Revenue:",

        f"₹{summary['total_revenue']:,}"

    )


    print(

        "Products Sold:",

        summary[
            "products_sold"
        ]

    )


    print(

        "Average Order Value:",

        f"₹{summary['average_order_value']:,.2f}"

    )


    print(

        "Total Discounts:",

        f"₹{summary['total_discounts']:,}"

    )


    print(

        "Recommendations:",

        summary[
            "recommendations"
        ]

    )


    print(

        "Negotiations:",

        summary[
            "negotiations"
        ]

    )


    print()

    print(
        "Top Products:"
    )


    for product, quantity in summary[
        "top_products"
    ]:

        print(

            f"  {product}: "
            f"{quantity} sold"

        )


    print()

    print(
        "Top Recommended Products:"
    )


    for product, count in summary[
        "top_recommendations"
    ]:

        print(

            f"  {product}: "
            f"{count} recommendations"

        )


    print()

    print(
        "=========================================="
    )