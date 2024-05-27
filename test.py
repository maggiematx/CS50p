def main():
      time=input("What tie is it?")
      total_time=convert(time)
      if 7<=total_time<=8:
            print("breakfast time")
      elif 12<=total_time<=13:
            print("lunch time")
      elif 18<=total_time<=19:
            print("dinner time")
      else:
            pass

def convert(time):
      hours, minutes=time.split(":")
      hours=int(hours)
      minutes=int(minutes)
      total_time=hours+minutes/6
      return total_time


main()

