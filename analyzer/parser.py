import csv
from datetime import datetime
from analyzer.models import LogEvent



def parse_log_file(file_path: str) -> list[LogEvent]:
    events = []
    
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                timestamp = datetime.strptime(
                row["timestamp"], "%Y-%m-%d %H:%M:%S"
                )
                
                event = LogEvent(
                timestamp=timestamp,
                system=row["system"],
                severity=row["severity"],
                message=row["message"],
                )
                
                events.append(event)
                
            except (ValueError, KeyError) as e:
                print(f"Skipping invalid row: {row} ({e})")
                
    return events