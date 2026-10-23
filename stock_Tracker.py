prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

total = 0

while True:
    stock = input("Enter stock name (or done): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = prices[stock] * quantity
    total += investment

    print("Investment:", investment)

print("Total investment:", total)