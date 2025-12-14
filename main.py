
# Stock Prices
stock_prizes = {
    "TMPV": 347.20,
    "RELIANCE": 1554,
    "TCS": 3220.10,
    "ULTRACEMCO": 11730,
    "M&M": 3679.10,
    "ETERNAL": 297.85
}

def calculate_investment():
    total_investment = 0
    portfolio = {}

    print("\nWelcome to the Stock Portfolio Tracker!\n")
    print("Enter the stock symbol (e.g., ETERNAL, TCS, RELIANCE), and quantity (number of shares).")

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prizes:
            print(f"Sorry, we don't have data for {stock}")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Invalid quantity!")
        
        if quantity <= 0:
            print("Quantity less than minimum purchase amount.")

        stock_value = stock_prizes[stock] * quantity
        total_investment += stock_value
        portfolio[stock] = {"Quantity": quantity, "Value": stock_value}
    return portfolio, total_investment

def display_portfolio(portfolio, total_investment):
    print("\nPortfolio Summary:")
    for stock, details in portfolio.items():
        print(f"{stock}: {details['Quantity']} shares, Total Value: {details['Value']:,.2f} Rs.")
    print(f"\nTotal investment value: {total_investment:,.2f} Rs.")

def save_to_file(portfolio, total_investment):
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary: \n")
        for stock,details in portfolio.items():
            file.write(f"{stock}: {details['Quantity']} shares, Total Value: {details['Value']:,.2f} Rs.\n")
        file.write(f"\nTotal investment value: {total_investment:,.2f} Rs.\n")
    print("Portfolio saved to 'portfolio.txt'")


portfolio, total_investment = calculate_investment()
display_portfolio(portfolio, total_investment)
save_to_file(portfolio, total_investment)