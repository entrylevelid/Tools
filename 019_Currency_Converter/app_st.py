import streamlit as st
import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            rates = data["rates"]
            rate = rates.get(to_currency.upper())

            if rate:
                converted = amount * rate
                return f"📈 Rate: 1 {from_currency.upper()} = {rate:.4f} {to_currency.upper()}\n💰 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
            else:
                return f"❌ Currency code '{to_currency}' not found."
        else:
            return "❌ Failed to fetch exchange rates."
    except Exception as e:
        return f"⚠️ An error occurred: {e}"

def main():
    st.title("💱 Currency Converter")
    from_currency = st.text_input("Enter source currency (e.g., USD):", "USD")
    to_currency = st.text_input("Enter target currency (e.g., EUR):", "IDR")
    amount = st.number_input("Enter amount to convert:", min_value=0.0, step=0.01)
    
    if st.button("Convert"):
        result = convert_currency(from_currency, to_currency, amount)
        st.write(result)

if __name__ == "__main__":
    main()
