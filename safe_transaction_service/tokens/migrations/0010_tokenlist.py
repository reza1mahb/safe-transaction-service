# Generated by Django 4.1.3 on 2023-01-24 12:31
from django.db import migrations, models

from gnosis.eth import EthereumNetwork

from safe_transaction_service.utils.ethereum import get_ethereum_network

TOKEN_LIST_BY_NETWORK = {
    EthereumNetwork.MAINNET: (
        "https://tokens.coingecko.com/uniswap/all.json",
        "Coingecko",
    ),
    EthereumNetwork.POLYGON: (
        "https://api-polygon-tokens.polygon.technology/tokenlists/polygonTokens.tokenlist.json",
        "Official",
    ),
    EthereumNetwork.OPTIMISM: (
        "https://static.optimism.io/optimism.tokenlist.json",
        "Official",
    ),
    EthereumNetwork.GNOSIS: ("https://tokens.honeyswap.org/", "HoneySwap"),
    EthereumNetwork.BINANCE_SMART_CHAIN_MAINNET: (
        "https://tokens.pancakeswap.finance/pancakeswap-extended.json",
        "PancakeSwap",
    ),
    EthereumNetwork.AURORA_MAINNET: ("https://aurora.dev/tokens.json", "Official"),
    EthereumNetwork.OPBNB_TESTNET: (
        "https://github.com/bnb-chain/opbnb-bridge-tokens/blob/main/opbnb.tokenlist.json",
        "OPBNB",
    ),
}


def add_default_token_lists(apps, schema_editor):
    ethereum_network = get_ethereum_network()

    token_list = TOKEN_LIST_BY_NETWORK.get(ethereum_network)
    if token_list:
        url, description = token_list
        TokenList = apps.get_model("tokens", "TokenList")
        TokenList.objects.create(url=url, description=description)


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0009_token_token_spam_idx"),
    ]

    operations = [
        migrations.CreateModel(
            name="TokenList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(unique=True)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.RunPython(
            add_default_token_lists, reverse_code=migrations.RunPython.noop
        ),
    ]
