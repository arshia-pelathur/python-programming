class Timer:
    def __init__(self,hours,minutes,seconds):
        self.hour = hours
        self.mins = minutes
        self.secs = seconds
    
    def __str__(self):
        time = get_time()
        temp = update(time)
        return ':'.join(temp)
    
    def next_seconds(self):
        self.secs +=1

    def previous_seconds(self):
        self.secs -=1

def get_time():
    return [str(part) for part in [obj.hour,obj.mins,obj.secs]]         # returns a list of hours, minutes and seconds

def update(time):
    value = []
    for part in time:
        if int(part)<10:
            value.append('0'+str(part))
        else:
            value.append(str(part))
    return value

obj = Timer(1,5,46)
setattr(obj,'final_time',obj.__str__())

print('Current time: ',obj)
obj.next_seconds()
print('After 1 second: ',obj)
obj.previous_seconds()
print('Previous second: ',obj)

