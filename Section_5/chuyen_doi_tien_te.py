exchange_rates = {
    "USD": 1.0,
    "VND": 25000.0,
    "EUR": 0.9,
    "JPY": 150.0,
    "GBP": 0.78,
    "CNY": 7.2,
    "AUD": 1.55,
    "CAD": 1.35,
    "KRW": 1300.0,
    "THB": 36.0
}

m_in = input("Nhập đơn vị tiền nguồn: ").upper()
m_out = input("Nhập đơn vị tiền đích: ").upper()
money = float(input("Nhập số tiền cần chuyển: "))


if m_in not in exchange_rates or m_out not in exchange_rates:
    print("Bạn ơi, tôi chưa code pro tới vậy 🥲😭")
else:
    usd_value = money / exchange_rates[m_in]
    result = usd_value * exchange_rates[m_out]
    print(f"{money:,.2f} {m_in} = {result:,.2f} {m_out}")
