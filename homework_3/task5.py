from forex_python.bitcoin import BtcConverter
bit_conv = BtcConverter()   

from datetime import datetime

bought_year=int(input('Please enter Year when you bought Bitcoin - '))
bought_month=int(input('Please enter Month when you bought Bitcoin - '))
bought_day=int(input('Please enter Day when you bought Bitcoin - '))

bought_date = datetime(bought_year,bought_month,bought_day)

bought_amount = int(input('Please Enter Amount you paid In USD- '))


bitcoin_price_now_usd=bit_conv.get_latest_price('USD')  





customers_profit_loss = bitcoin_price_now_usd - bought_amount


if customers_profit_loss > 0:
    print('Wow your Profit is -',customers_profit_loss)
elif customers_profit_loss < 0:
    print('Unfortunately your Loss is -',customers_profit_loss)    
else: 
    print('Your Profit is zero but so is the Loss')  