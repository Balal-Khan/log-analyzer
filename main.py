from analyzer.parser import parse_log_file



def main():
    events = parse_log_file("sample_logs/events.csv")
    
    print(f"Parsed {len(events)} valid events")
    
    for event in events:
        print(event)

if __name__ == "__main__":
    main()