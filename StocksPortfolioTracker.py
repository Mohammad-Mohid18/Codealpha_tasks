from datetime import datetime

def Menu():
    print("\n" + "=" * 40)
    print("💰 STOCK PORTFOLIO MANAGER".center(40))
    print("=" * 40)
    display_menu = {
            '1': 'Add Stock',
            '2': 'Remove Stock',
            '3': 'View Portfolio',
            '4': 'Exit'
    }
    for key, value in display_menu.items():
        print(f" {key}. {value}")
    print("=" * 40)
    command = input(" Choose your command (1-4): ")
    return command

self_portfolio = {}

def add_stock():
    print("\n" + "➕ ADD STOCK " + "-" * 30)
    symbol = input(" Enter stock symbol (e.g., AAPL): ").upper()
    shares = float(input(" Enter number of shares: "))
    price = float(input(" Enter purchase price per share: $"))

    if symbol in self_portfolio:
            print(f"\n ⚠️  {symbol} already in portfolio. Updating shares.")
            self_portfolio[symbol]['shares'] += shares
    else:
        self_portfolio[symbol] = {
            'shares': shares,
            'purchase_price': price,
            'date_added': datetime.now().strftime('%Y-%m-%d')
        }
    print(f"\n ✅ Added {shares} shares of {symbol} at ${price:.2f}")
    print("-" * 40)

def remove_stock():
    print("\n" + "➖ REMOVE STOCK " + "-" * 30)
    symbol = input(" Enter stock symbol to remove: ").upper()

    if symbol not in self_portfolio:
        print(f"\n ⚠️  {symbol} not found in portfolio")
        print("-" * 40)
        return

    print(f"\n Current shares: {self_portfolio[symbol]['shares']}")
    remove_all = input(" Remove all shares? (y/n): ").lower()
        
    if remove_all == 'y':
        del self_portfolio[symbol]
        print(f"\n ✅ Removed all shares of {symbol}")
    else:
        shares = float(input(" Enter shares to remove: "))
        if shares >= self_portfolio[symbol]['shares']:
            del self_portfolio[symbol]
            print(f"\n ✅ Removed all shares of {symbol}")
        else:
            self_portfolio[symbol]['shares'] -= shares
            print(f"\n ✅ Removed {shares} shares of {symbol}")
    print("-" * 40)

def view_portfolio():
    print("\n" + "=" * 60)
    print("📊 YOUR PORTFOLIO".center(60))
    print("=" * 60)
    
    if not self_portfolio:
        print("\n Your portfolio is empty!".center(60))
        print("=" * 60)
        return
    
    print(f"{' Symbol':<10}{' Shares':>10}{' Price':>15}{' Value':>15}{' Date':>15}")
    print("-" * 60)
    
    for symbol, data in self_portfolio.items():
        value = data['shares'] * data['purchase_price']
        print(
            f" {symbol:<9}"
            f"{data['shares']:>10.2f}"
            f"{data['purchase_price']:>15.2f}"
            f"{value:>15.2f}"
            f"{data['date_added']:>15}"
        )
    
    total = sum(data['shares'] * data['purchase_price'] for data in self_portfolio.values())
    print("-" * 60)
    print(f"{' TOTAL':<10}{'':>10}{'':>15}{total:>15.2f}{'':>15}")
    print("=" * 60)

def main():
    print("\n" + "✨ WELCOME TO STOCK PORTFOLIO TRACKER ✨".center(60))
    while True:
        choice = Menu()
        
        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("\n" + "=" * 40)
            print(" Thank you for using our service! ".center(40))
            print("=" * 40)
            break
        else:
            print("\n ⚠️  Invalid choice. Please try again.")

main()