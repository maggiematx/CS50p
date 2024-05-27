def main():
      time=input("What tie is it?")
      if 7<=total_time<=8:
            print("breakfast time")
      elif 12<=total_time<=13:
            print("lunch time")
      elif 18<=total_time<=19:
            print("dinner time")
      else:


def convert(time):
      hours, minutes=time.split(":")
      hours=int(hours)
      minutes=int(minutes)
      total_time=hours+minutes/60


main()

