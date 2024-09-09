import requests

response = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history/?guccounter=1')
print(response.text[:600])
