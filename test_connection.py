from bot.orders import place_limit_order

try:
    result = place_limit_order(
        symbol="BTCUSDT",
        side="SELL",
        quantity=0.001,
        price=120000
    )

    print("LIMIT ORDER SUCCESS")
    print(result)

except Exception as e:
    print("LIMIT ORDER FAILED")
    print(e)