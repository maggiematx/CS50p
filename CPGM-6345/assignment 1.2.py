class Employee:

    def __init__(self,name,salary,project_status):
                 self.hours=hours
                 self.minutes=minutes
                 self.seconds=seconds

    def display_seconds(self):
        total_seconds=self.hours*3600+self.minutes*60+self.seconds
        return total_seconds


def main():
    obj1 = get_status()
    return

def get_status():
    timenow=datetime.now()
    hours=timenow.hour
    minutes=timenow.minute
    seconds=timenow.second

    return Time(hours,minutes,seconds)

if __name__== "__main__":
    main()

