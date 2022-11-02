import time

import os

birthdayFile = 'bday.txt'

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
            print('Birthdays Today: ' + line[1]
            + ' ' + line[2] + '')
            time.sleep(60) 

    if flag == 0:
            print( "No Birthdays Today!")

if __name__ == '__main__':
    checkTodaysBirthdays()

#
