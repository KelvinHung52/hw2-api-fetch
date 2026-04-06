import requests
import json

url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

result = {
    "base_code": data.get("base_code"),
    "time_last_update_utc": data.get("time_last_update_utc"),
    "rates": {
        "TWD": data.get("rates", {}).get("TWD"),
        "JPY": data.get("rates", {}).get("JPY"),
        "KRW": data.get("rates", {}).get("KRW"),
        "EUR": data.get("rates", {}).get("EUR")
    }
}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("API 資料已成功儲存到 output.json")