exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrive_time = arrive_hour * 60 + arrive_minute

diff = arrive_time - exam_time

if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        print(f"{hours}:{minutes:02d} hours after the start")

elif diff >= -30:
    print("On time")
    if diff != 0:
        print(f"{abs(diff)} minutes before the start")

else:
    print("Early")
    if abs(diff) < 60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
