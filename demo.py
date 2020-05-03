from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

accountID = "101-009-14596339-001"
access_token = '02b2ada0401a30b2bad21668ae7e0ec2-545d6baa42608e924a1b59bf1dd4278f'

api = API(access_token=access_token, environment="practice")

params = { "instruments": "USD_JPY" }

instrument = accounts.AccountInstruments(accountID=accountID, params=params)
api.request(instrument) 

account = accounts.AccountSummary(accountID)
api.request(account)

params = {
  "count": 5,
  "granularity": "M5"
}
candles = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
api.request(candles)


