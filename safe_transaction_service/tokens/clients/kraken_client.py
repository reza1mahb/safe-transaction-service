import logging

from .base_client import BaseHTTPClient
from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class KrakenClient(BaseHTTPClient):
    def _get_price(self, symbol: str) -> float:
        url = f"https://api.kraken.com/0/public/Ticker?pair={symbol}"
        try:
            response = self.http_session.get(url, timeout=self.request_timeout)
            api_json = response.json()
            error = api_json.get("error")
            if not response.ok or error:
                logger.warning("Cannot get price from url=%s", url)
                raise CannotGetPrice(str(api_json["error"]))

            result = api_json["result"]
            for new_ticker in result:
                price = float(result[new_ticker]["c"][0])
                if not price:
                    raise CannotGetPrice(f"Price from url={url} is {price}")
                return price
        except (ValueError, IOError) as e:
            raise CannotGetPrice from e

    def get_ada_usd_price(self) -> float:
        return self._get_price("ADAUSD")

    def get_avax_usd_price(self) -> float:
        """
        :return: current USD price for AVAX
        :raises: CannotGetPrice
        """
        return self._get_price("AVAXUSD")

    def get_dai_usd_price(self) -> float:
        """
        :return: current USD price for DAI
        :raises: CannotGetPrice
        """
        return self._get_price("DAIUSD")

    def get_ether_usd_price(self) -> float:
        """
        :return: current USD price for Ethereum
        :raises: CannotGetPrice
        """
        return self._get_price("ETHUSD")

    def get_matic_usd_price(self):
        """
        :return: current USD price for MATIC
        :raises: CannotGetPrice
        """
        return self._get_price("MATICUSD")

    def get_ewt_usd_price(self) -> float:
        """
        :return: current USD price for Energy Web Token
        :raises: CannotGetPrice
        """
        return self._get_price("EWTUSD")

    def get_algo_usd_price(self):
        """
        :return: current USD price for Algorand
        :raises: CannotGetPrice
        """
        return self._get_price("ALGOUSD")

    def get_btc_usd_price(self):
        """
        :return: current USD price for Algorand
        :raises: CannotGetPrice
        """
        return self._get_price("BTCUSD")

    def get_eth_usd_price(self):
        """
        :return: current USD price for Algorand
        :raises: CannotGetPrice
        """
        return self._get_price("ETHUSD")
