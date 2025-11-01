import requests

baseUrl = "https://zenoapi.com/api"

url = "{baseUrl}/payments/orders/create/"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "YOUR_API_KEY"
}
payload = {
    "order_id": "85ghxdsKLKJKkdnkjknkjhsdsdsddsdkjnLJLKls8",
    "buyer_email": "john@example.com",
    "buyer_name": "John Joh",
    "buyer_phone": "0652449389",
    "amount": 1000,
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
