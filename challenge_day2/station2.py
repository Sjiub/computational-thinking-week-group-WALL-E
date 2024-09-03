    # challenge japanese weekdays 
# determine the weekday with the provided date format yyyy-mm-dd and translate to japanese
# example data 
# input 2023-01-10 output 火曜日 (Friday)
# Zeller's Congruence baby
""" 
    Sunday＝日曜日（にちようび、nichiyoubi）
    Monday＝月曜日（げつようび、getsuyoubi）
    Tuesday＝火曜日（かようび、kayoubi）
    Wednesday＝水曜日（すいようび、suiyoubi）
    Thursday＝木曜日（もくようび、mokuyoubi）
    Friday＝金曜日（きんようび、kinyoubi）
    Saturday＝土曜日（どようび、doyoubi）
"""
def solution_station_2(date_str):
    # gotta slice the date stringgg
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])

    # Zeller for Gregorian calender
    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100
    weekday_number = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

    japanese_weekdays = ["土曜日", "日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]

    return japanese_weekdays[weekday_number]

print(solution_station_2("2023-01-10"))
