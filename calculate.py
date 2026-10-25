def calculate_total(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > 300:
        amount = amount * 0.90  # 10% discount

    total = amount * 1.05  # Add 5% GST
    return round(total, 2)