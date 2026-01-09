import csv
from datetime import datetime

def parse_log_file(file_path: str) -> list:
    events = []
    
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                timestamp = datetime.strptime(
                row["timestamp"], "%Y-%m-%d %H:%M:%S"
                )
                
                event = {
                "timestamp": timestamp,
                "system": row["system"],
                "severity": row["severity"],
                "message": row["message"],
                }
                
                events.append(event)
                
            except Exception as e:
                print("Skipping invalid row: {} ({})".format(row,e))
                
    return events