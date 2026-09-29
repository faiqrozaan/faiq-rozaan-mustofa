import json 
import csv 
from typing import List, Dict, Any

#1. READ: Membaca langsung dari file JSON 
input_file_json: str = "data/api_response.json"
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)
raw_items: List[Dict[str, Any]] = payload.get("items")
items: List[Dict[str, Any]] = raw_items if isinstance(raw_items, list) else []

#2. TRANSFORM: Transformasi menggunakan filter dan lambda 
filtered_items: List[Dict[str, Any]] = filter(lambda item: item["is_active"] is True, items)

# [Langkah 1] Maping data 
transformed_items: map = map(
    lambda item: {
        "user_id": item["user_id"],
        "name": item["name"].upper(),
        "role": item["role"],
        "score": item["score"],
        "status": "LULUS" if float(item["score"]) >= 80.0 else "TIDAK LULUS"
    }, 
    filtered_items
)
# [Langkah 2] Convert map object to list 
active_users: List[Dict[str, Any]] = list(transformed_items)

#3. WRITE: Menyimpan ke file CSV
output_path: str = "data/active_users.csv"
headers: List[str] = list(active_users[0].keys())

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() 
    writer.writerows(active_users)
print(f"[SUCCESS] Data berhasil disimpan di: {output_path}") 

