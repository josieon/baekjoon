hour, minute = map(int, input().split())
"""
if(minute < 45):
    hour -= 1
    minute += 60
if(hour < 0):
    hour += 24
print(hour, minute-45)
"""
hour = (hour + (minute - 45) // 60) % 24
minute = (minute - 45) % 60
print(hour, minute)