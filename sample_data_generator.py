import json
import os
import random
from datetime import datetime, timedelta
from config import RAW_DATA_DIR

def generate_sample_trades(start_date, end_date):
    """Generate sample trading data"""
    trades = []
    current_date = start_date
    
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    
    while current_date <= end_date:
        # Generate 1-5 trades per day
        for _ in range(random.randint(1, 5)):
            symbol = random.choice(symbols)
            is_buyer = random.choice([True, False])
            price = {
                'BTCUSDT': random.uniform(30000, 60000),
                'ETHUSDT': random.uniform(1500, 3000),
                'BNBUSDT': random.uniform(200, 400)
            }[symbol]
            
            qty = random.uniform(0.1, 1.0)
            commission = price * qty * 0.001  # 0.1% commission
            
            trade = {
                'symbol': symbol,
                'id': random.randint(1000000, 9999999),
                'orderId': random.randint(1000000, 9999999),
                'price': str(price),
                'qty': str(qty),
                'commission': str(commission),
                'commissionAsset': symbol[-4:],
                'time': int(current_date.timestamp() * 1000),
                'isBuyer': is_buyer,
                'isMaker': random.choice([True, False]),
                'isBestMatch': True
            }
            trades.append(trade)
        
        current_date += timedelta(days=1)
    
    return trades

def generate_sample_futures_trades(start_date, end_date):
    """Generate sample futures trading data"""
    trades = []
    current_date = start_date
    
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    
    while current_date <= end_date:
        # Generate 1-3 futures trades per day
        for _ in range(random.randint(1, 3)):
            symbol = random.choice(symbols)
            side = random.choice(['BUY', 'SELL'])
            price = {
                'BTCUSDT': random.uniform(30000, 60000),
                'ETHUSDT': random.uniform(1500, 3000),
                'BNBUSDT': random.uniform(200, 400)
            }[symbol]
            
            qty = random.uniform(0.1, 2.0)
            commission = price * qty * 0.0004  # 0.04% commission
            pnl = random.uniform(-1000, 1000)
            
            trade = {
                'symbol': symbol,
                'id': random.randint(1000000, 9999999),
                'orderId': random.randint(1000000, 9999999),
                'side': side,
                'price': str(price),
                'qty': str(qty),
                'realizedPnl': str(pnl),
                'commission': str(commission),
                'commissionAsset': 'USDT',
                'time': int(current_date.timestamp() * 1000),
                'positionSide': 'BOTH',
                'isMaker': random.choice([True, False])
            }
            trades.append(trade)
        
        current_date += timedelta(days=1)
    
    return trades

def generate_sample_deposits_withdrawals(start_date, end_date):
    """Generate sample deposit and withdrawal data"""
    transactions = {
        'deposits': [],
        'withdrawals': []
    }
    
    current_date = start_date
    assets = ['BTC', 'ETH', 'USDT', 'BNB']
    
    while current_date <= end_date:
        # Generate deposits (0-2 per day)
        for _ in range(random.randint(0, 2)):
            asset = random.choice(assets)
            amount = {
                'BTC': random.uniform(0.1, 1.0),
                'ETH': random.uniform(1.0, 10.0),
                'USDT': random.uniform(1000, 10000),
                'BNB': random.uniform(5, 50)
            }[asset]
            
            deposit = {
                'coin': asset,
                'amount': str(amount),
                'status': 1,
                'insertTime': int(current_date.timestamp() * 1000),
                'txId': f"0x{random.randint(100000, 999999):x}"
            }
            transactions['deposits'].append(deposit)
        
        # Generate withdrawals (0-1 per day)
        for _ in range(random.randint(0, 1)):
            asset = random.choice(assets)
            amount = {
                'BTC': random.uniform(0.1, 0.5),
                'ETH': random.uniform(1.0, 5.0),
                'USDT': random.uniform(500, 5000),
                'BNB': random.uniform(2, 20)
            }[asset]
            
            fee = {
                'BTC': 0.0001,
                'ETH': 0.005,
                'USDT': 1,
                'BNB': 0.01
            }[asset]
            
            withdrawal = {
                'coin': asset,
                'amount': str(amount),
                'transactionFee': str(fee),
                'status': 1,
                'applyTime': int(current_date.timestamp() * 1000),
                'txId': f"0x{random.randint(100000, 999999):x}"
            }
            transactions['withdrawals'].append(withdrawal)
        
        current_date += timedelta(days=1)
    
    return transactions

def generate_sample_staking(start_date, end_date):
    """Generate sample staking data"""
    staking_records = []
    current_date = start_date
    
    assets = ['BNB', 'ETH']
    
    while current_date <= end_date:
        # Generate staking rewards (0-1 per day)
        for _ in range(random.randint(0, 1)):
            asset = random.choice(assets)
            amount = {
                'BNB': random.uniform(0.1, 1.0),
                'ETH': random.uniform(0.01, 0.1)
            }[asset]
            
            staking_record = {
                'asset': asset,
                'amount': str(amount),
                'time': int(current_date.timestamp() * 1000),
                'apy': str(random.uniform(5, 15)),
                'duration': 30  # 30 days staking period
            }
            staking_records.append(staking_record)
        
        current_date += timedelta(days=1)
    
    return staking_records

def generate_all_sample_data():
    """Generate all sample data"""
    # Create data directory if it doesn't exist
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    
    # Generate data for the past 2 years
    end_date = datetime.now()
    start_date = datetime(2018, 9, 1)
    
    # Generate and save spot trades
    spot_trades = generate_sample_trades(start_date, end_date)
    with open(os.path.join(RAW_DATA_DIR, 'spot_trades.json'), 'w') as f:
        json.dump(spot_trades, f, indent=2)
    
    # Generate and save futures trades
    futures_trades = generate_sample_futures_trades(start_date, end_date)
    with open(os.path.join(RAW_DATA_DIR, 'futures_trades.json'), 'w') as f:
        json.dump(futures_trades, f, indent=2)
    
    # Generate and save deposits and withdrawals
    transactions = generate_sample_deposits_withdrawals(start_date, end_date)
    with open(os.path.join(RAW_DATA_DIR, 'deposits.json'), 'w') as f:
        json.dump(transactions['deposits'], f, indent=2)
    with open(os.path.join(RAW_DATA_DIR, 'withdrawals.json'), 'w') as f:
        json.dump(transactions['withdrawals'], f, indent=2)
    
    # Generate and save staking data
    staking_data = generate_sample_staking(start_date, end_date)
    with open(os.path.join(RAW_DATA_DIR, 'staking.json'), 'w') as f:
        json.dump(staking_data, f, indent=2)

if __name__ == "__main__":
    generate_all_sample_data()