from pyscript import document, display

def generate_sku(e):

    category = document.getElementById("category").value
    product = document.getElementById("product").value
    quantity = document.getElementById("quantity").value

    category_code = category[:2].upper()
    product_code = product[:3].upper()
    quantity_code = quantity[-3:]

    sku = category_code + product_code + quantity_code

    document.getElementById("sku_result").innerHTML = ""

    display(f"Your SKU: {sku}", target="sku_result")