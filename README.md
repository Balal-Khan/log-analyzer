#  Overview
A Python-based log analysis tool that parses system event logs, handles invalid data, and supports filtering and sorting events by severity, system, and time window.

This project simulates real-world industrial control system logs and demonstrates core software engineering concepts such as data modeling, validation, and functional filtering.


# Features
*CSV log parsing with robust error handling  
*Strongly-typed LogEvent data model  
*Handling of invalid timestamps  
*Filter events by:  
    -Severity (INFO, WARN, ERROR)  
    -System (e.g., PLC_1, PLC_2)  
    -Time Window (last N minutes)  
*Sort events chronologically  
*Modular project structure  
 
# Example Usage
'''bash
python main.py

'''bash
python main.py --severity ERROR --system PLC_2

# Project Structure

```text
log-analyzer/
├── main.py
├── analyzer/
│   ├── models.py      # LogEvent data model
│   ├── parser.py      # CSV parsing and validation
│   ├── filters.py     # Filtering and sorting logic
├── sample_logs/
│   └── events.csv


