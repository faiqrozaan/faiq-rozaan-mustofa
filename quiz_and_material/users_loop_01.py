import json 
import csv 
from typing import List, Dict, Any

#1. READ: Membaca langsung dari file JSON 
input_file_json: str = "data/api_response.json"
with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)
raw_items: List[Dict[str, Any]] = payload.get("items")
items: List[Dict[str, Any]] = raw_items if isinstance(raw_items, list) else []

#2. TRANSFORM: Transformasi Data Menggunakan Standard For Loop
active_users: List[Dict[str, Any]] = [] 
for item in items: 
    # [Langkah 2] filter data is_active True 
    if item["is_active"] is True: 
        # [Langkah 3] Format data dictionary baru masukan ke variabel array active_users
        formatted_item: Dict[str, Any] = {
            "user_id": item["user_id"],
            "name": item["name"].upper(),
            "role": item["role"],
            "score": item["score"], 
            "status": "LULUS" if float(item["score"]) >= 80.0 else "TIDAK LULUS"
        }
        active_users.append(formatted_item)

#3. WRITE: Menyimpan ke file CSV
output_path: str = "data/active_users.csv"
headers: List[str] = ["user_id", "name", "role", "score", "status"]
with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() 
    writer.writerows(active_users)
print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")