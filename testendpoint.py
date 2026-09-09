import requests

frankfurter_rates_url="https://api.frankfurter.dev/v2/1999-01-04"

historical_rates_response=requests.get(frankfurter_rates_url,
                      params=
  {
  "base": "EUR",
  "symbols": "AUD,CAD,CHF,CZK"
  }
) #Data Dictionary
historical_rates=historical_rates_response.json()
print(historical_rates.keys())
print(historical_rates["rates"]["symbols"])

