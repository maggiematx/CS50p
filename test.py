def main():
    calculation()


def calculation():
      x, y,z= input("Expression: ").split(" ")
      x=int(x)
      z=int(z)
      if y=="+":
            print(f"{x+z: .1f}")
      elif y=="-":
            print(f"{x-z: .1f}")
      elif y=="*":
            print(f"{x*z: .1f}")
      elif y=="/" and z!=0:
            print(f"{x/z:.1f}")
      else:
           print("Invalid input.")



if __name__ == "__main__":
    main()
