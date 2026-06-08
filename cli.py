import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order_input


def print_order_response(response):
    print("\nOrder Response Details")
    print("-" * 30)
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Symbol       : {response.get('symbol')}")
    print(f"Status       : {response.get('status')}")
    print(f"Side         : {response.get('side')}")
    print(f"Type         : {response.get('type')}")
    print(f"Quantity     : {response.get('origQty')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Price        : {response.get('price')}")
    print("Success      : Order placed successfully")


def main():
    parser = argparse.ArgumentParser(description="Simplified Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair, example: BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", required=False, type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        symbol, side, order_type, quantity, price = validate_order_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Request Summary")
        print("-" * 30)
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":
            print(f"Price    : {price}")
            response = place_limit_order(symbol, side, quantity, price)
        else:
            response = place_market_order(symbol, side, quantity)

        print_order_response(response)

    # except Exception as e:
    #     print("\nOrder Failed")
    #     print("-" * 30)
    #     print(f"Error: {e}")
    except ValueError as e:
        print(f"Validation Error: {e}")

    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    main()