# Coded by: https://t.me/CryptoResearchLab

import requests

ETH_ENDPOINT = "https://mint.fun/api/mintfun/profile/{}/offer-count/1"
OP_ENDPOINT = "https://mint.fun/api/mintfun/profile/{}/offer-count/10"
BASE_ENDPOINT = "https://mint.fun/api/mintfun/profile/{}/offer-count/8453"


def check_address_for_nfts(address, endpoint):
    url = endpoint.format(address)
    response = requests.get(url)
    return response.json().get("totalOffers", None)


def process_addresses(file_path):
    with open(file_path, 'r') as file:
        addresses = file.read().splitlines()

    for address in addresses:
        total_offers_eth = check_address_for_nfts(address, ETH_ENDPOINT)
        total_offers_op = check_address_for_nfts(address, OP_ENDPOINT)
        total_offers_base = check_address_for_nfts(address, BASE_ENDPOINT)

        if any((total_offers_eth, total_offers_op, total_offers_base)):
            print(f"| {address} | ETH TOTAL OFFERS: {total_offers_eth}"
                  f" | OP TOTAL OFFERS: {total_offers_op}"
                  f" | BASE TOTAL OFFERS: {total_offers_base} |")


if __name__ == "__main__":
    file_path = "addresses.txt"
    process_addresses(file_path)
