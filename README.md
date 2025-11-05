

# 🚀 ZenoPay API – Dynamic Lipa Namba and TAN QR Code Creation Endpoint

ZenoPay enables you to **receive payments in Tanzania** via **Mobile Money** and **Banks** using dynamic **Lipa Namba** and **TAN QR Codes**.
This API lets you instantly create a payment order, generate a **Dynamic TAN QR**, and receive **real-time payment notifications** via webhooks.

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

| Field          | Type   | Required | Description                                                        |
| -------------- | ------ | -------- | ------------------------------------------------------------------ |
| `order_id`     | string | ✅        | Unique ID for the order (from your system)                         |
| `buyer_email`  | string | ✅        | Email address of the buyer                                         |
| `buyer_name`   | string | ✅        | Full name of the buyer                                             |
| `buyer_phone`  | string | ✅        | Buyer’s phone number (local format)                                |
| `amount`       | float  | ✅        | Amount to be charged in Tanzanian Shillings (TZS)                  |
| `redirect_url` | string | ❌        | URL where the customer will be redirected after completing payment |
| `webhook_url`  | string | ❌        | Your backend endpoint to receive real-time payment notifications   |
| `metadata`     | object | ❌        | Any extra data you want to attach and receive back in the webhook  |

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
    "amount": 1000,
    "redirect_url": "https://merchant.example.com/payment-success",
    "webhook_url": "https://merchant.example.com/api/payment-webhook",
    "metadata": {
      "product_name": "Zeno Subscription Plan",
      "customer_id": "CUST-1029"
    }
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
    "amount": 1000,
    "redirect_url": "https://merchant.example.com/payment-success",
    "webhook_url": "https://merchant.example.com/api/payment-webhook",
    "metadata": {
        "product_name": "Zeno Subscription Plan",
        "customer_id": "CUST-1029"
    }
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

---

### 🧩 Response Field Description

| Field                 | Description                               |
| --------------------- | ----------------------------------------- |
| `status`              | API response status (`SUCCESS`, `FAILED`) |
| `resultcode`          | API result code (`000` = success)         |
| `message`             | Description of the result                 |
| `order_id`            | The order ID you provided                 |
| `payment_gateway_url` | Redirect URL for customer checkout        |
| `tanqr_number`        | The generated TAN QR Code number          |

---

## 🌍 Redirect URL Example

After payment completion, the customer will be redirected to your provided `redirect_url` (if set), with query parameters:

```
https://merchant.example.com/payment-success?order_id=85-psdsld-sadsa8&status=SUCCESS&reference=1003020496
```

Use this to confirm order completion or show a success screen to your customer.

---

## 🌐 Webhook Notification (Payment Callback)

When a payment is completed, ZenoPay sends a `POST` request to your `webhook_url` with the following payload.

### 📬 Example Webhook Payload

```json
{
  "order_id": "677e43274d7cb",
  "payment_status": "COMPLETED",
  "reference": "1003020496",
  "amount": 1000,
  "currency": "TZS",
  "payment_method": "M-Pesa",
  "timestamp": "2025-11-05T12:45:23+03:00",
  "metadata": {
    "product_name": "Zeno Premium Subscription",
    "customer_id": "CUST-1029"
  }
}
```

---

### 🧩 Webhook Field Description

| Field            | Description                                             |
| ---------------- | ------------------------------------------------------- |
| `order_id`       | The unique order reference you sent during creation     |
| `payment_status` | Payment status (`COMPLETED`, `FAILED`, `PENDING`)       |
| `reference`      | ZenoPay or partner gateway transaction reference        |
| `amount`         | Amount paid                                             |
| `currency`       | Currency used (TZS)                                     |
| `payment_method` | Payment method (e.g., `M-Pesa`, `Airtel Money`, `Bank`) |
| `timestamp`      | ISO timestamp of transaction                            |
| `metadata`       | Any custom data you included during creation            |

---

### ✅ Expected Response from Your Server

Your webhook endpoint should return an HTTP **200 OK** response to confirm successful receipt:

```json
{
  "status": "received"
}
```

If your server doesn’t respond or returns a non-200 status, ZenoPay may retry the webhook after a short interval.

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

* Always use **unique `order_id`** values per transaction.
* The `webhook_url` must accept **HTTPS POST requests** and return HTTP 200.
* The `redirect_url` is optional but enhances user experience.
* Use `tanqr_number` to display the **TAN QR** dynamically on your app or site.
* All amounts are in **Tanzanian Shillings (TZS)**.

---

## 📘 GitHub README Example

```md
# 💳 ZenoPay API – Dynamic Lipa Namba & TAN QR Code Creation

Integrate ZenoPay into your website or app to receive payments via Mobile Money and Banks in Tanzania.

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
  "amount": 1500,
  "redirect_url": "https://merchant.example.com/payment-success",
  "webhook_url": "https://merchant.example.com/api/payment-webhook",
  "metadata": {
    "plan": "Premium",
    "customer_id": "CUST-1092"
  }
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

### 🌐 Webhook Notification

```json
{
  "order_id": "ORDER-12345",
  "payment_status": "COMPLETED",
  "reference": "1003020496",
  "amount": 1500,
  "payment_method": "Airtel Money",
  "metadata": {
    "plan": "Premium"
  }
}
```

---

## 💬 Support

📧 Email: [support@zenoapi.com](mailto:support@zenoapi.com)
💬 WhatsApp: [ZenoPay Pro Assistant](https://wa.me/255793166166)
🌐 Website: [https://zenopay.com](https://zenopay.com)

---

## 📜 License

MIT License © ZenoPay

```
