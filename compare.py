from products import products


def compare_products(product1, product2):

    print("======================================")
    print("         PRODUCT COMPARISON")
    print("======================================")

    print()
    print("Feature        |", product1["name"], "|", product2["name"])
    print("--------------------------------------")

    print(
        "Price          | ₹",
        product1["price"],
        "| ₹",
        product2["price"]
    )

    if "ram" in product1 and "ram" in product2:
        print(
            "RAM            |",
            product1["ram"],
            "|",
            product2["ram"]
        )

    if "storage" in product1 and "storage" in product2:
        print(
            "Storage        |",
            product1["storage"],
            "|",
            product2["storage"]
        )

    if "processor" in product1 and "processor" in product2:
        print(
            "Processor      |",
            product1["processor"],
            "|",
            product2["processor"]
        )

    if "gpu" in product1 and "gpu" in product2:
        print(
            "GPU            |",
            product1["gpu"],
            "|",
            product2["gpu"]
        )

    if "battery" in product1 and "battery" in product2:
        print(
            "Battery        |",
            product1["battery"],
            "|",
            product2["battery"]
        )

    print("======================================")


laptops = [
    product for product in products
    if product["category"] == "Laptop"
]

compare_products(laptops[0], laptops[1])