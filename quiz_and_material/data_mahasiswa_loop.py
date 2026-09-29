import json 
import csv
from typing import List, Dict, Any 

# Variabel Path Data JSON Yang akan dibaca 
input_file_json: str = "data/api_response.json"

# Membaca File JSON 
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)
raw_items: List[Dict[str, Any]] = payload.get("items")
items: List[Dict[str, Any]] = raw_items if isinstance(raw_items, list) else []

# Transformasi Data JSON - Menggunakan Perulangan For Loop
active_users: List[Dict[str, Any]] = []
for item in items:
    if item["is_active"] is True:
      formatted_items: Dict[str, Any] = {
         "user_id": item["user_id"],
         "name": item["name"].upper(),
         "role": item["role"],
         "score": item["score"],
         "status": "LULUS" if float(item["score"]) >= 80.0 else "TIDAK LULUS"
      }
      active_users.append(formatted_items)

# Menyimpan ke File CSV 
output_path: str = "data/actives_users.csv"
headers: List[str] = list(active_users[0].keys())
with open(output_path, mode="w", encoding="utf-8", newline="") as file:
   writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
   writer.writeheader()
   writer.writerows(active_users)
print(f"""[SUCCESS] Data berhasil disimpan di: {output_path}""")