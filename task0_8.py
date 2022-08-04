def int_to_time(minutes: int):
    hours = minutes // 60
    minutes_converter = minutes - 60
    hr_minutes_converter = minutes - hours * 60
    if minutes == 0:
        return f"{hours} hours, {minutes} minutes"
    elif minutes == 1:
        return f"{hours} hours, {minutes} minute"
    elif minutes < 60:
        return f"{hours} hours, {minutes} minutes"
    elif minutes == 60:
        return f"{hours} hour, {minutes_converter} minutes"
    elif minutes == 61:
        return f"{hours} hour, {minutes_converter} minute"
    elif minutes > 60 and minutes < 120:
        return f"{hours} hour, {minutes_converter} minutes"
    elif minutes % 60 == 0 and minutes > 60:
        return f"{hours} hours, {hr_minutes_converter} minutes"
    elif minutes % 60 == 1 and minutes > 60:
        return f"{hours} hours, {hr_minutes_converter} minute"
    else:
        return f"{hours} hours, {hr_minutes_converter} minutes"
