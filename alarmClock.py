import datetime as dt
import calendar as cl
import subprocess as sb
import os
import time

def check_for_player():
    try:
        sb.Popen(["mpg123","-?"],stdout=sb.PIPE,stderr=sb.PIPE)
    except:
        try:
            print("You must install an additional program for the correct operation of this (sound playback). After 10 seconds, the installation will start.")
            time.sleep(5)
            for i in range(10):
                print(i)
                time.sleep(1)
            os.system("apt-get install mpg123")
            time.sleep(3)
        except:
            print("Unexpected error.\nAborting.")
            exit()
        print("Starting the AlarmClock")

def set_day():
    days=[]
    counter=0
    for i in cl.day_name:
        counter+=1
        print(str(counter)+' - '+str(i))
        days.append(i)
    while(True):
        day=int(input('select the day on which you want to set the alarm: '))
        if day>7 or day<=0:
            print("\nThere are only 7 days in a week! Try again.\n\n\n")
            continue
        else:
            day-=1
        return day+1

def set_time(day):
    while(True):
        check = dt.datetime.timetuple(dt.datetime.now())
        hour=int(input("enter the hour you want to set the alarm: "))
        if day == (check[6]+1):
            if hour>=24 or hour<check[3]:
                print('\nYou can choose an hour from '+str(check[3])+' to 23. Try again.\n\n\n')
                continue
        elif hour>=24 or hour<0:
            print("\nHours can be from 0 to 23. Try again.\n\n\n")
            continue
        while(True):
            check = dt.datetime.timetuple(dt.datetime.now())
            minute=int(input('enter the minute you want to set the alarm: '))
            if day == (check[6]+1) and hour == check[3]:
                if minute>60 or minute<=check[4]:
                    print('\nYou can choose a minute from '+str(check[4]+1)+' to 59. Try again.\n\n\n')
                    continue
                else:
                    break
            elif minute<60 and minute>=0:
                break
            else:
                print("\nMinutes can be from 0 to 59. Try again\n\n\n")
                continue
        return hour , minute

def set_clock_time(day,hour,minute):
    a=0
    a=dt.datetime.timetuple(dt.datetime.today())[6]+1
    if a > day:
        a=7-a+day
    else:
        a=day-a
    day=a
    Year,Month,Day = (dt.datetime.timetuple(dt.datetime.today()))[:3]
    Day+=day
    if Day>(cl.monthrange(Year,Month)[1]):
        Day-=cl.monthrange(Year,Month)[1]
        Month+=1
        if Month>12:
            Month=1
            Year+=1
    date=dt.datetime(Year,Month,Day,hour,minute,0,0)
    return date

def set_music():
    music=[]
    counter=1
    try:
        music=os.listdir('./Music')
    except OSError:
        print("There is no \"Music\" here! Make it!")
        exit()
    print("Variants:")
    for i in music:
        print(str(counter)+' - '+i)
        counter+=1
    while(True):
        the_choice = int(input("Choose the variant you want: "))
        if the_choice > len(music) or the_choice <= 0:
            print("You can choose only from 1 to "+str(len(music))+". Try again")
            continue
        else:
            return music[the_choice-1]

def set_clock(music,timer):
    try:
        time.sleep(timer)
        os.system('mpg123 ./Music/'+music)
        print("Are you woked up? ;P")
        exit()
    except KeyboardInterrupt:
        print('Why are we stopping here?')
        exit(0)

def main():
    check_for_player()
    while(True):
        try:
            try:
                day = set_day()
                hour , minute = set_time(day)
                mus=set_music()
                smth = (set_clock_time(day,hour,minute)-dt.datetime.today()).total_seconds()
                set_clock(mus,smth)
            except ValueError:
                print('You entered incorrect data. \nPlease start again.\n')
                continue
        except:
            print("\nUnexpected error.\nAborting.")
            exit()

if __name__ == '__main__':
    main()
    exit()
