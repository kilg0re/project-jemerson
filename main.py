import requests
import sys

cnpj = sys.argv[1]
url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'

response = requests.request('GET', url)

print(response.text)
