from bot.client import client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"MARKET order request: symbol={symbol}, side={side}, quantity={quantity}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET order response: {response}")
        return response

    except Exception as e:
        logger.error(f"MARKET order failed: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT order request: symbol={symbol}, side={side}, quantity={quantity}, price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT order response: {response}")
        return response

    except Exception as e:
        logger.error(f"LIMIT order failed: {str(e)}")
        raise