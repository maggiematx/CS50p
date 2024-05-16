# c
c=300000000

# askign what's m
m=int(input("What's m?"))

# fomula to calculate E
E=m*c**2
#print E
print(E)


def E_cal():
    E=m*c**2
return E

def main():
    c = 3000000
    m = int(input("Enter the mass in kilograms: "))
    energy = E_cal(m, c)
    print("The equivalent energy in Joules is:", energy)

    if __name__ == "__main__":
    main()
