
def main():
    user_input=str(input("Input: ")).lower()
    output=shorted(user_input)
    print(f"Output: {output}")

def shorted(user_input):
    v=["a", "e", "i","o", "u"]
    nv=""
    for c in user_input:
        if c not in v:
            nv += c
    return nv
main()

