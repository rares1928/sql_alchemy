import requests


async def functie1(n):
    url = "https://random-data-api.com/api/v2/banks?size=1&is_xml=true"
    response = requests.get(url)
    for i in range(n):
        print(response.json()['bank_name'])


async def functie2(n):
    url = "https://random-data-api.com/api/v2/beers?size=1&is_xml=true"
    response = requests.get(url)
    for i in range(n):
        print(response.json()['name'])


async def main(n):
    await functie1(n)
    await functie2(n)

main(5)