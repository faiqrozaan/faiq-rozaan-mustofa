import json 
import csv 
from typing import List, Dict, Any

input_file_json: str = "data/raw_products.json"
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)
raw_products: List[Dict[str, Any]] = payload.get("products")
products: List[Dict[str, Any]] = raw_products if isinstance(raw_products, list) else [] 

active_users: List[Dict[str, Any]] = [
    {
        "item_code": item["item_code"],
        "name": item["name"].upper(),
        "price": item["price"],
        "stock": item["stock"],
        "status": "High Stock" if float(item["stock"]) >= 20 else "Low  Stock"
    }
    for item in products
    if item["is_available"] is True
]

output_path: str = "data/products_lc.csv"
headers: List[str] = list(active_users[0].keys())

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() 
    writer.writerows(active_users)
print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")