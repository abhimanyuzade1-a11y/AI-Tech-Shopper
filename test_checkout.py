from products import products
from cart import ShoppingCart

from checkout import (
    create_order,
    process_payment,
    show_order
)


# Create cart

cart = ShoppingCart()


# Add products

cart.add_product(
    products[0]
)

cart.add_product(
    products[1]
)


# Create order

order = create_order(
    cart
)


# Process payment

order = process_payment(
    order
)


# Show order

show_order(
    order
)