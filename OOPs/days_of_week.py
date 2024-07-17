class WeekdayError(Exception):
    pass

class Weeker:
    days_of_week = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
    def __init__(self,day):
        if day not in Weeker.days_of_week:
            raise WeekdayError(f'{day} - Not a valid day format')
        self.Day = day
    
    def __str__(self):
        return self.Day

    def add_days(self,value):
        indx = Weeker.days_of_week.index(self.Day)
        self.Day = Weeker.days_of_week[value%7+indx]

    def subtract_days(self,value):
        indx = Weeker.days_of_week.index(self.Day)
        self.Day = Weeker.days_of_week[indx-value%7]
try:
    day = Weeker('Wed')
    print('Current day -',day)

    day.add_days(15)
    print('After 15 days -',day)
    
    day.subtract_days(13)
    print('Before 13 days -',day)

    day0 = Weeker('Saturday')
except WeekdayError as e:
    print(e)