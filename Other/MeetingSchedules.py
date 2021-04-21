"""
We are writing a tool to help users manage their calendars. Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.

Each time is expressed as an integer using 24-hour notation, such as 1200 (12:00), 1530 (15:30), or 800 (8:00).

Sample input:

p1_meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

p2_meetings = [
  ( 0, 844),
  ( 930, 1200),
  (1515, 1546),
  (1600, 2400),
]

p3_meetings = [
  ( 845, 915),
  (1515, 1545),
  (1235, 1245),
]

p4_meetings = [
  ( 1, 5),
  (844, 900),
  (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

Expected output:

findAvailableTimes(schedules1)
 => [  844,  845 ],
    [  915,  930 ],
    [ 1200, 1230 ],
    [ 1500, 1515 ],
    [ 1546, 1600 ]

findAvailableTimes(schedules2)
 => [    0,  845 ],
    [  915, 1230 ],
    [ 1500, 1515 ],
    [ 1545, 2400 ]

findAvailableTimes(schedules3)
    [  900,  930 ],
    [ 1200, 1515 ]

n = number of meetings per schedule
s = number of schedules
"""
p1_meetings = [
    (1230, 1300),
    (845, 900),
    (1300, 1500),
]
# 0 - 2400
p2_meetings = [
    (0, 844),
    (930, 1200),
    (1515, 1546),
    (1600, 2400),
]

p3_meetings = [
    (845, 915),
    (1515, 1545),
    (1235, 1245),
]

p4_meetings = [
    (1, 5),
    (844, 900),
    (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

def mintohrs(timeList, last):

    try:
        for i in range(len(timeList)):
            if timeList[i] + 1 != timeList[i+1]:
                output.append((timeList[0], timeList[i]+1))
                timeList = timeList[i+1:]
                break
            else:
                continue

        if output[-1][1] != last:
            mintohrs(timeList, last)
    except:
        if timeList[0] != timeList[-1]:
            output.append((timeList[0], timeList[-1]))

    return output

def findAvailableTimes(schedules):
    timeList = [m for m in range(2401)]
    for p in schedules:
        for time in p:
            for i in range(time[0], time[1]):
                try:
                    timeList.remove(i)
                except:
                    pass

    output = mintohrs(timeList, timeList[-1])
    return output

output = []
print(findAvailableTimes(schedules1))

output = []
print(findAvailableTimes(schedules2))

output = []
print(findAvailableTimes(schedules3))