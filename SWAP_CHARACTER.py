# HackerRank.com presents "Pythonist 2".

def swap_case(str):
    str=list(str)
    ln = len(str)

    # Conversion according to ASCII values
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':

            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) - 32)

        elif str[i] >= 'A' and str[i] <= 'Z':

            # Convert lowercase to uppercase
            str[i] = chr(ord(str[i]) + 32)

    str = ''.join(str)
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
