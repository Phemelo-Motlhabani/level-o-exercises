def time_converter(minutes):
    if minutes == 0:
        print(f"0 hours, {minutes} minutes")
    elif minutes == 1:
        print(f"0 hours, {minutes} minute")
    elif minutes < 60:
        print(f"0 hours, {minutes} minutes")
    elif minutes == 60:
        print("1 hour, 0 minutes")
    elif minutes == 61:
        print("1 hour, 1 minute")
    elif minutes > 60 and minutes < 120:
        minutes_converter = minutes - 60
        print(f"1 hour, {minutes_converter} minutes")
    elif minutes % 60 == 0 and minutes > 60:
        hours = int(minutes / 60)
        print(f"{hours} hours, 0 minutes")
    elif ((minutes % 60) - 1 == 0) and minutes > 60:
        hours = int((minutes - 1) / 60)
        print(f"{hours} hours, 1 minute")
    else:
        hours = minutes // 60
        minutes_converter = minutes - (hours * 60)
        print(f"{hours} hours, {minutes_converter} minutes")
