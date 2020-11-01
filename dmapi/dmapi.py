from requests import codes, get
from time import sleep

VERSION = '0.0.1'
API_BASE_URL = 'https://www.dadosdemercado.com/api/v0'


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
            data=data,
            headers=self._headers(),
        )

        if response.status_code == codes.TOO_MANY_REQUESTS:
            sleep(2 ** retry)
            return self._get(url, data, retry + 1)

        return response.json()

    def companies(self, ):
        url = '/companies'
        return self._get(url)

    def company(self, company_slug):
        url = '/companies/{}'.format(company_slug)
        return self._get(url)

    def financials(self, company_slug, **kwargs):
        url = '/companies/{}/financials'.format(company_slug)
        return self._get(url, data=kwargs)

    def ratios(self, company_slug, **kwargs):
        url = '/companies/{}/ratios'.format(company_slug)
        return self._get(url, data=kwargs)

    def tickers(self):
        url = '/tickers'
        return self._get(url)

    def ticker(self, ticker, **kwargs):
        url = '/tickers/{}'.format(ticker)
        return self._get(url, data=kwargs)

    def price_indexes(self, **kwargs):
        url = '/price_indexes'
        return self._get(url, data=kwargs)

    def selic(self):
        url = '/selic'
        return self._get(url)
