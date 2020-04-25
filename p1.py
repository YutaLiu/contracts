from datetime import datetime
from datetime import timedelta
import calendar
def Weekly(cur_time):
    datetime.strptime(cur_time, "%Y%m%d")
    Weekday = datetime.strptime(cur_time, "%Y%m%d").weekday()+1
    if Weekday >= 5 :
        end_date = datetime.strptime(cur_time, "%Y%m%d") + timedelta(days=12-Weekday)
    else :
        end_date = datetime.strptime(cur_time, "%Y%m%d") + timedelta(days=(5-Weekday))
    
    return end_date.strftime("%Y%m%d")

def BiWeekly(cur_time):
    datetime.strptime(cur_time, "%Y%m%d")
    Weekday = datetime.strptime(cur_time, "%Y%m%d").weekday()+1
    if Weekday >= 5 :
        end_date = datetime.strptime(cur_time, "%Y%m%d") + timedelta(days=19-Weekday)
    else :
        end_date = datetime.strptime(cur_time, "%Y%m%d") + timedelta(days=(12-Weekday))
    
    return end_date.strftime("%Y%m%d")


def last_fridays(year,month):

    last_friday = max(week[calendar.FRIDAY]
        for week in calendar.monthcalendar(year, month))
    return ('{:4d}{:02d}{:02d}'.format(year, month, last_friday))

def Quarterly(cur_time):
    
    settle_m = min(list(filter(lambda x: x >= datetime.strptime(cur_time, "%Y%m%d").month, [3,6,9,12])))
    cur_day = datetime.strptime(cur_time, "%Y%m%d")
    end_day = last_fridays(cur_day.year,settle_m)
    if (datetime.strptime(end_day, "%Y%m%d") > datetime.strptime(BiWeekly(cur_time), "%Y%m%d")):
        return end_day
    else :
        if settle_m == 12 :
            return last_fridays(cur_day.year+1,3)
        else : 
            return last_fridays(cur_day.year,settle_m+3)
    

if __name__ == '__main__':
    day = '20191101'
    print (Weekly(day) , BiWeekly(day) , Quarterly(day))
    
    
    