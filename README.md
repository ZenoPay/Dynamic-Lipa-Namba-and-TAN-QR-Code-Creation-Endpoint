

# 🚀 ZenoPay API – Dynamic Lipa Namba and TAN QR Code Creation Endpoint

Easily create payment orders and generate a **Dynamic TAN QR Code** for your customers using ZenoPay’s API.

---

## 🔗 Endpoint

**POST**
`https://zenoapi.com/api/payments/orders/create/`

---

## 🔐 Authentication

Include your **API Key** in the request headers:

```bash
x-api-key: YOUR_API_KEY
```

---

## 📥 Request Body (JSON)

| Field         | Type   | Required | Description                                |
| ------------- | ------ | -------- | ------------------------------------------ |
| `order_id`    | string | ✅        | Unique ID for the order (from your system) |
| `buyer_email` | string | ✅        | Email address of the buyer                 |
| `buyer_name`  | string | ✅        | Full name of the buyer                     |
| `buyer_phone` | string | ✅        | Buyer’s phone number (local format)        |
| `amount`      | float  | ✅        | Amount to be charged                       |

---

## 🧾 Example Request

### 💻 cURL

```bash
curl -X POST https://zenoapi.com/api/payments/orders/create/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "order_id": "85-psdsld-sadsadsdsd8",
    "buyer_email": "john@example.com",
    "buyer_name": "John Joh",
    "buyer_phone": "0600930493",
    "amount": 1000
  }'
```

---

### 🐍 Python (requests)

```python
import requests

url = "https://zenoapi.com/api/payments/orders/create/"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "YOUR_API_KEY"
}
payload = {
    "order_id": "85-psdsld-sadsadsdsd8",
    "buyer_email": "john@example.com",
    "buyer_name": "John Joh",
    "buyer_phone": "0600930493",
    "amount": 1000
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

---

## ✅ Sample Success Response

```json
{
    "status": "SUCCESS",
    "resultcode": "000",
    "message": "Order created successfully.",
    "order_id": "85-psdsld-sadsa8",
    "payment_gateway_url": "https://tz.selcom.online/paymentgw/checkout/Y25rdC9QYlllak1kcnhwZ2hyWHlKa0lGYlJKeHhTQ1YzWUg0bDhBbzY1b0VycWpYU3d3UGVvRjc2Mzk3OGxnaGc0aU40aFZVUExRTA==/",
    "tanqr_number": "63803046"
}
```

### 🧩 Field Explanation

| Field                 | Description                                          |
| --------------------- | ---------------------------------------------------- |
| `status`              | Status of the API request (e.g. `SUCCESS`, `FAILED`) |
| `resultcode`          | Transaction result code (`000` = success)            |
| `message`             | Message describing the result                        |
| `order_id`            | The unique order ID provided in the request          |
| `payment_gateway_url` | Redirect URL for customer payment                    |
| `tanqr_number`        | The generated TAN QR number for the transaction      |

---

## ❗ Error Response Example

```json
{
  "status": "FAILED",
  "resultcode": "401",
  "message": "Invalid API Key."
}
```

---

## 🧠 Notes

* Make sure your `order_id` is **unique** for every transaction.
* `amount` should be provided in **Tanzanian Shillings (TZS)**.
* The `payment_gateway_url` can be opened in a browser or embedded in a mobile/web view for user payment.
* You can use the `tanqr_number` to generate or display a **QR code** dynamically in your application.

---

## 📘 GitHub README Example

```md
# 💳 ZenoPay API – Order Creation & TAN QR Code

This guide helps you integrate with ZenoPay’s payment API to create orders and generate dynamic TAN QR codes.

## 🔗 Endpoint

**POST** `https://zenoapi.com/api/payments/orders/create/`

### 🔐 Headers

```

x-api-key: YOUR_API_KEY
Content-Type: application/json

````

### 📥 Request Example

```json
{
  "order_id": "ORDER-12345",
  "buyer_email": "user@example.com",
  "buyer_name": "Jane Doe",
  "buyer_phone": "0652449389",
  "amount": 1500
}
````

### 📤 Success Response

```json
{
  "status": "SUCCESS",
  "resultcode": "000",
  "message": "Order created successfully.",
  "order_id": "ORDER-12345",
  "payment_gateway_url": "https://tz.selcom.online/paymentgw/checkout/.../",
  "tanqr_number": "63803046"
}
```

---

## 💬 Support

Need help?
📧 Email: [support@zenoapi.com](mailto:support@zenoapi.com)
💬 WhatsApp: [ZenoPay Pro Assistant](https://wa.me/255xxxxxxxxx)

---

## 📜 License

MIT License © ZenoPay

```
