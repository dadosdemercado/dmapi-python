from requests import get
from time import sleep

VERSION = '1.0.0'
API_BASE_URL = 'https://api.dadosdemercado.com.br/v1'


class DMAPI:

    def __init__(self, token):
        self.api_base = API_BASE_URL
        self.token = token

    def _build_url(self, url):
        return self.api_base + url

    def _headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.token),
        }

    def _get(self, url, data={}, retry=0):
        response = get(
            self._build_url(url),
            params=data,
            headers=self._headers(),
        )

        if response.status_code == 429:
            sleep(2 ** retry)
            return self._get(url, data, retry + 1)

        return response.json()

    def companies(self, ):
        url = '/companies'
        return self._get(url)

    def company(self, cvm_code):
        url = '/companies/{}'.format(cvm_code)
        return self._get(url)

    def balances(self, cvm_code, **kwargs):
        url = '/companies/{}/balances'.format(cvm_code)
        return self._get(url, data=kwargs)

    def incomes(self, cvm_code, **kwargs):
        url = '/companies/{}/incomes'.format(cvm_code)
        return self._get(url, data=kwargs)

    def cash_flows(self, cvm_code, **kwargs):
        url = '/companies/{}/cash_flows'.format(cvm_code)
        return self._get(url, data=kwargs)

    def ratios(self, cvm_code, **kwargs):
        url = '/companies/{}/ratios'.format(cvm_code)
        return self._get(url, data=kwargs)

    def market_ratios(self, cvm_code, **kwargs):
        url = '/companies/{}/market_ratios'.format(cvm_code)
        return self._get(url, data=kwargs)

    def dividends(self, cvm_code, **kwargs):
        url = '/companies/{}/dividends'.format(cvm_code)
        return self._get(url, data=kwargs)

    def splits(self, cvm_code, **kwargs):
        url = '/companies/{}/splits'.format(cvm_code)
        return self._get(url, data=kwargs)

    def tickers(self):
        url = '/tickers'
        return self._get(url)

    def indexes(self):
        url = '/indexes'
        return self._get(url)

    def quotes(self, ticker, **kwargs):
        url = '/tickers/{}/quotes'.format(ticker)
        return self._get(url, data=kwargs)

    def estimates(self, index, **kwargs):
        url = '/macro/{}/estimates'.format(index)
        return self._get(url, data=kwargs)

    def yield_curves(self):
        url = '/macro/yield_curves'
        return self._get(url)
