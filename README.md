# Binance Futures Testnet Trading Bot

## Overview

A Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

Features:

* BUY and SELL support
* MARKET and LIMIT orders
* Input validation
* Structured logging
* Exception handling
* Command-line interface using argparse

## Installation

```bash
git clone <repository_url>
cd trading_bot

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Project Structure

trading_bot/

* bot/

  * client.py
  * orders.py
  * validators.py
  * logging_config.py
* logs/
* cli.py
* requirements.txt
* README.md

## Assumptions

* Binance Futures Demo/Testnet account is configured.
* API credentials are stored securely in a `.env` file.
* Supported order types are MARKET and LIMIT.
* Supported sides are BUY and SELL.
