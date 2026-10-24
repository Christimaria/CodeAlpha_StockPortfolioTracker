
import csv

# Predefined stock prices (example prices in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks and prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "Stock": stock_name,
        "Quantity": quantity,
        "Price per Share": price,
        "Investment Value": investment
    })

    print(f"Added {quantity} shares of {stock_name}.")

print("\n===== Portfolio Summary =====")

if portfolio:
    for item in portfolio:
        print(
            f"{item['Stock']} | "
            f"Quantity: {item['Quantity']} | "
            f"Price: ${item['Price per Share']} | "
            f"Value: ${item['Investment Value']}"
        )

    print(f"\nTotal Investment Value: ${total_investment}")

    # Save the portfolio to a CSV file
    with open("portfolio.csv", "w", newline="") as file:
        fieldnames = [
            "Stock",
            "Quantity",
            "Price per Share",
            "Investment Value"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(portfolio)

    print("Portfolio saved to portfolio.csv")

else:
    print("No stocks were added to the portfolio.")
