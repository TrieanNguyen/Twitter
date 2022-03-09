from time import sleep
from datetime import datetime, timedelta
import os
import csv

def WriteToCSV(header, data, pathToFile):
    with open(pathToFile, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

def ExecTerminalCommand(command):
    os.system(command)

def GeneralFromTime():
    now = datetime.now() + timedelta(hours=7)

    hourDayMonth = now.strftime("%H%d%m")
    minuteSecond = now.strftime("%M%S")

    #h = "0" + h

    #hourDayMonth = h + "0609"
    #minuteSecond = "0000"
    path = 'data/' + now.strftime("%Y/%m/%d/%H/")

    #path = 'data/' + "2021/09/07/" + h + "/"

    fileName = minuteSecond + '.csv'

    data = [
            ['101' + hourDayMonth, 'Mary Jane ' + hourDayMonth, 'Female', 30],
            ['102' + hourDayMonth, 'Peter Parker ' + hourDayMonth, 'Male', 29]
    ]

    return data, minuteSecond, path, fileName


def SleepUntilNextHour():
    sleep(3600 - datetime.now().second - datetime.now().minute * 60)


if __name__ == "__main__":

    header = ['Id', 'Name', 'Gender', 'Age']
    
    data, minute_second, path, fileName = GeneralFromTime()

    ExecTerminalCommand('mkdir -p ' + path)

    WriteToCSV(header, data, path + fileName)

    ExecTerminalCommand('/usr/local/hadoop/bin/hdfs dfs -mkdir -p /' + path)

    ExecTerminalCommand('/usr/local/hadoop/bin/hdfs dfs -put ' + path + fileName + ' ' + '/' + path)
