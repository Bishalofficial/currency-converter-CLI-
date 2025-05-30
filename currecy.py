import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)  # DEBUG LINE
        if "result" in data:
            return round(data["result"], 2)
        else:
            return None
    else:
        print("API connection failed.")
        return None
try:
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (INR/USD/EUR): ").strip().upper()
    to_curr = input("To currency (INR/USD/EUR): ").strip().upper()

    converted = convert_currency(from_curr, to_curr, amount)

    if converted is not None:
        print(f"{amount} {from_curr} = {converted} {to_curr}")
    else:
        print("Conversion failed or invalid input.")

except ValueError:
    print("Please enter a valid number for the amount.")