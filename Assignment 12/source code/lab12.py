import time

class Clock:
    def __init__(self, hours, minutes, seconds, clockType = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clockType = clockType
        if clockType:
            self.clockAddon = 'am' if self.hours < 13 else 'pm'
            if self.clockAddon == 'pm':
                self.hours -= 12

    def clockFix(self, num):
        if len(num) == 1:
            num = '0' + num
        return num

    def tick(self):
        self.seconds += 1
        check = False
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
            check = True
        if self.clockType:
            if self.hours == 12 and check:
                self.clockAddon = 'am' if self.clockAddon == 'pm' else 'pm'
            if self.hours == 13:
                self.hours = 1
        else:
            if self.hours == 24:
                self.hours = 0

    def __str__(self):
        hours = self.clockFix(str(self.hours))
        minutes = self.clockFix(str(self.minutes))
        seconds = self.clockFix(str(self.seconds))
        if self.clockType:
            return hours +':' + minutes +":" + seconds +" " + self.clockAddon
        else:
            return hours + ':' + minutes + ":" + seconds

hours   = int(input('What is the current hour ==>'))
minutes = int(input('What is the current minute ==>'))
seconds = int(input('What is the current second ==>'))

clock = Clock(hours, minutes, seconds, 1)
while True:
    print(clock)
    clock.tick()
    time.sleep(1)