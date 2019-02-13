# Currency converter

## Description

- CLI and web API application for currency converting an amount of money
- Rates are based on [Rates API](https://ratesapi.io/)
- Supported currencies are from [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)
- Currency symbols are from [Forex-python package](https://github.com/MicroPyramid/forex-python/blob/master/forex_python/raw_data/currencies.json)
- Used external packages: Forex-python, Flask 
## Parameters
- `amount` - amount which we want to convert (float)
- `input_currency` - input currency - 3 letters code or currency symbol
- `output_currency` - requested/output currency - 3 letters code or currency symbol (optional)

## Functionality
- If `output_currency` parameter is missing, convert to all known currencies

## Output
- JSON with following structure.
```
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```
## Examples

### CLI
- 3 letters code:
```
$ python currency_converter.py --amount 142.4 --input_currency CZK --output_currency EUR
{
    "input": {
        "amount": 142.4, 
        "currency": "CZK"
    }, 
    "output": {
        "EUR": 5.51
    }
}
```
- Currency symbol:
```
$ python currency_converter.py --amount 104.23 --input_currency € --output_currency £
{
    "input": {
        "amount": 104.23, 
        "currency": "EUR"
    }, 
    "output": {
        "GBP": 91.41
    }
}
```
- Ambiguous currency symbol:
```
$ python currency_converter.py --amount 114.63 --input_currency $ --output_currency EUR
{
    "1.input": {
        "amount": 114.63, 
        "currency": "AUD"
    }, 
    "1.output": {
        "EUR": 71.98
    }, 
    "2.input": {
        "amount": 114.63, 
        "currency": "CAD"
    }, 
    "2.output": {
        "EUR": 76.57
    }, 
    "3.input": {
        "amount": 114.63, 
        "currency": "MXN"
    }, 
    "3.output": {
        "EUR": 5.27
    }
}
```
- Missing `output_currency` parameter:
```
$ python currency_converter.py --amount 45.25 --input_currency USD
{
    "input": {
        "amount": 45.25, 
        "currency": "USD"
    }, 
    "output": {
        "AUD": 63.8, 
        "BGN": 78.35, 
        "BRL": 168.3, 
        "CAD": 59.97, 
        "CHF": 45.59, 
        "CNY": 306.36, 
        "CZK": 1036.35, 
        "DKK": 298.93, 
        "EUR": 40.06, 
        "GBP": 35.13, 
        "HKD": 355.14, 
        "HRK": 296.75, 
        "HUF": 12730.17, 
        "IDR": 636599.72, 
        "ILS": 164.69, 
        "INR": 3196.7, 
        "ISK": 5471.98, 
        "JPY": 4995.29, 
        "KRW": 50843.36, 
        "MXN": 870.85, 
        "MYR": 184.5, 
        "NOK": 392.37, 
        "NZD": 67.16, 
        "PHP": 2357.76, 
        "PLN": 173.29, 
        "RON": 189.93, 
        "RUB": 2965.8, 
        "SEK": 419.51, 
        "SGD": 61.43, 
        "THB": 1416.31, 
        "TRY": 237.81, 
        "ZAR": 622.99
    }
}
```
### API
- For using web API type `python api_currency_converter.py` 
```
http://localhost:5000/currency_converter?amount=123.67&input_currency=CZK&output_currency=EUR
{
  "input": {
    "amount": 123.67, 
    "currency": "CZK"
  }, 
  "output": {
    "EUR": 4.79
  }
}
```
```
http://localhost:5000/currency_converter?amount=77.41&input_currency=€&output_currency=£
{
    "input": {
        "amount": 77.41, 
        "currency": "EUR"
    }, 
    "output": {
        "GBP": 67.89
    }
}
```
## Credits
- Author: Tomas Bernat (tom.bernat@centrum.cz)
- Created: 12.2.2019

