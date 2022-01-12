import csv
import pandas as pd
import statistics as st
import pygal

dictWeekday ={}
dictWeekend ={}
filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    wr = open("WeekendActivity.csv","w")
    wr.write(str (header[0]) + "," + str (header[1]) + ","+ str (header[2]))
    wr.write("\n")

    n = 0 
    for row in reader :
        interval = int(row[2])
        if(row[0] == "NA"):
            row[0] = 0
            n += 1
        steps = row[0] 
        temp = pd.Timestamp(row[1])
        if temp.dayofweek <5:
            row.append("weekday")
            dictWeekday.setdefault(interval,[])
            dictWeekday[interval].append(int(steps))
        else:
            row.append("weekend")
            dictWeekend.setdefault(interval, [])
            dictWeekend[interval].append(int(steps))
        wr.write(str(row[0]))
        wr.write(str (row[0]) + "," + str (row[1]) + ","+ str (row[2]) + "," + str (row[3]))
        wr.write("\n")

    wr.close

AvgperInterval_weekend = []
AvgperInterval_weekday = []

for i in dictWeekday.keys():
    AvgperInterval_weekday.append(st.mean(dictWeekday.get(i)))

for i in dictWeekend.keys():
    AvgperInterval_weekend.append(st.mean(dictWeekend.get(i)))

hist = pygal.Bar()
hist.title = "Average per interval in the Weekdays"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictWeekday.keys()
hist.add("Average steps",AvgperInterval_weekday)
hist.render_to_file('stepsversion2.svg')

hist = pygal.Bar()
hist.title = "Average per interval in the Weekends"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictWeekend.keys()
hist.add("Average steps",AvgperInterval_weekend)
hist.render_to_file('stepsversion3.svg')
    
print("The total number of missing values is ",n)
print("New dataset created")