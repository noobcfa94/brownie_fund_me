from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3

from scripts.helpful_scripts import deploy_mocks


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fund me acontract

    # if we r on persistent network like rinkeby, use the associated address
    # otherwise , deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        # "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",  # copy from FundeMe address of the priceFeed and put infront
        price_feed_address,  # if pricefeedaddress=0xx  when in development
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )  # add publish source for verifyin ETHERSCAN
    print(f"Contract deployed to {fund_me.address}")
    return fund_me  # to shows that u have run in TEST


def main():
    deploy_fund_me()
