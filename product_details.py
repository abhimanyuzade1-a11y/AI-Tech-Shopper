from products import products


def show_product(product):
    print()
    print("==============================")
    print("PRODUCT DETAILS")
    print("==============================")
    print("Name:", product["name"])
    print("Brand:", product["brand"])
    print("Category:", product["category"])
    print("Price: ₹", product["price"])
    print("Stock:", product["stock"])

    if "ram" in product:
        print("RAM:", product["ram"])

    if "storage" in product:
        print("Storage:", product["storage"])

    if "processor" in product:
        print("Processor:", product["processor"])

    if "gpu" in product:
        print("GPU:", product["gpu"])

    if "camera" in product:
        print("Camera:", product["camera"])

    print("Use cases:", ", ".join(product["use_cases"]))
    print("==============================")


show_product(products[0])