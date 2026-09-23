def calculate_subtotal(unit_price, quantity):
    return unit_price * quantity


def calculate_total_items(item_quantities):
    total_items = 0
    for item in item_quantities:
        total_items += item
    return total_items


def calculate_discounted_price(subtotal, total_items):
    # Diskon ditentukan dari total jumlah barang, bukan dari harga subtotal.
    if total_items > 100:
        return subtotal * 0.9
    else:
        return subtotal * 0.95


def calculate_shipping_cost(is_member, shipping_fee):
    if is_member:
        return 0
    else:
        return shipping_fee


def calculate_order_total(unit_price, quantity, item_quantities, is_member, shipping_fee):
    subtotal = calculate_subtotal(unit_price, quantity)
    total_items = calculate_total_items(item_quantities)
    price_after_discount = calculate_discounted_price(subtotal, total_items)
    shipping_cost = calculate_shipping_cost(is_member, shipping_fee)

    return price_after_discount + shipping_cost


result_1 = calculate_order_total(10000, 5, [40, 70], True, 0)
result_2 = calculate_order_total(15000, 3, [10, 20], False, 12000)

print("Result 1:", result_1)
print("Result 2:", result_2)