import mysql.connector
from datetime import date, datetime, timedelta, time


def timeIntoDatetime(yesterday, timeText):
    datesplit = list(map(int, timeText.split(':')))
    if datesplit[0] > 14:
        # Yesterday
        return datetime.combine(yesterday, time(datesplit[0], datesplit[1]))
    else:
        # Today
        return datetime.combine(yesterday + timedelta(days=1),
                                time(datesplit[0], datesplit[1]))


def formatDayDate(dateText):
    dateSplit = list(map(int, dateText.split('/')))
    if len(dateSplit) == 2:
        # day and month
        date = datetime(year=datetime.now().year,
                        month=dateSplit[1],
                        day=dateSplit[0]).date()
    elif len(dateSplit) == 3:
        # day, month and year
        date = datetime(year=dateSplit[2],
                        month=dateSplit[1],
                        day=dateSplit[0]).date()
    else:
        raise Exception("This date is not possible")
    return date


def formatBinary(informationText):
    return True if int(informationText) == 1 else False


try:
    conn = mysql.connector.connect(user='nightLogger',
                                   password='nightLogger123',
                                   host='192.168.1.2',
                                   database='homeData')
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

cursor = conn.cursor()

add_night = ("INSERT INTO nightSlept (person, date, timeStart, timeFinish, "
             "generalFeeling,  howTiredByNight, howTiredByMorning, alcohol, "
             "chocolateCoffeeSimilar, tea, water, protractedComputerUse, "
             "redshiftOn, holidayBefore, holidayAfter, usedSleepCycle) VALUES "
             "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
             "%s, %s, %s, %s, %s, %s);")

user = 1
yesterday = (date.today() - timedelta(days=1)) if input(
    "Is it today? ") == 'y' else formatDayDate(input("When then? "))
data = (user,
        yesterday,
        timeIntoDatetime(yesterday, input("When did you go to bed? ")),
        timeIntoDatetime(yesterday, input("When did you wake up? ")),
        int(input("From 0 to 5, general feeling? ")),
        int(input("From 0 to 5, how tired before going to sleep? ")),
        int(input("From 0 to 5, how tired by morning? ")),
        int(input("From 0 to 5, any alcohol involved? ")),
        int(input("From 0 to 5, did you consume any chocolate or coffee? ")),
        int(input("From -5 to 5, any tea (negative is calming tea, "
                  "positive is stimulant tea)? ")),
        int(input("From 0 to 5, how much water before going to sleep? ")),
        int(input("From 0 to 5, was the use of computer protracted? ")),
        int(input("From 0 to 5, how much of it was with redshift on? ")),
        formatBinary(input("Binary, was yesterday holiday? ")),
        formatBinary(input("Binary, is today holiday? ")),
        formatBinary(input("Binary, did you use the sleepCycle to wake up? ")))

print(data)

try:
    cursor.execute(add_night, data)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

conn.commit()
cursor.close()
conn.close()
