from products import products
from cart import ShoppingCart


cart = ShoppingCart()


# Add first product

cart.add_product(
    products[0]
)


# Add second product

cart.add_product(
    products[1]
)


# Show cart

cart.show_cart()


# Remove first product

cart.remove_product(
    products[0]["name"]
)


# Show cart again

cart.show_cart()