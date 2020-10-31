# Dados de Mercado

This is a Python Client for
[Dados de Mercado](https://www.dadosdemercado.com/)'s API.

## Installation

```
pip3 install dmapi
```

## Usage

You will need a token to access the API endpoints. Go to the
[documentation page](https://www.dadosdemercado.com/api) (in portuguese)
to generate one.

### Usage example

```python
from dmapi import DMAPI

dm = DMAPI(token='c8cad35b0376c8f6bcb46614f80d9443')  # Set your token here

print(dm.companies())
```

### Available calls

Please refer to the [documentation](https://www.dadosdemercado.com/api)
for more details on the parameters available on each call.

- `dm.companies()`
- `dm.company(company_slug)`
- `dm.financials(company_slug, [type, offset, limit])`
- `dm.ratios(company_slug, [type, offset, limit, market])`
- `dm.tickers()`
- `dm.ticker(ticker, [from_date, to_date])`
- `dm.price_indexes([from_date, to_date])`
- `dm.selic()`
