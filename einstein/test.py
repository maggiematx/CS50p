def E_cal(m,c):
    E=m*c**2
    return E

def main():
    c=30000000
    m=int(input("what's m?"))
    Energy=E_cal(m,c)
    print("E is:" , Energy)
