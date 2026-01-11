from analyzer.parser import parse_log_file
from analyzer.filters import(
    filter_by_severity,
    filter_last_n_minutes,
    sort_by_timestamp,
)



def main():
    events = parse_log_file("sample_logs/events.csv")
    
    error_events = filter_by_severity(events, "ERROR")
    print(f"ERROR events: {len(error_events)}")
    
    
    recent_events = filter_last_n_minutes(events, minutes=60)
    print(f"Events in last 60 minutes: {len(recent_events)}")
    
    
    sorted_events = sort_by_timestamp(events)
    
    for event in sorted_events:
        print(event)



if __name__ == "__main__":
    main()