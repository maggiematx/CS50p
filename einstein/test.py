def E_cal():
    E = m * c ** 2
    return E

def main():
    c = 3000000
    m = int(input("what's m: "))
    energy = E_cal
    print("E is:", energy)

if __name__ == "__main__":
    main()
