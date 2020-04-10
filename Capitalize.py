def isalnum1(num):
    solve = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    solve2 = list(solve)
    if num==solve2:
        return True
    else:
        for i in range(0, len(num)):
            if num[i].isalnum:
                if num[i]=='#' or num[i]=='@' or num[i]=='$' or num[i]=='%' or num[i]=='^' or num[i]=='&' or num[i]=='*':
                    return False
                return True
    return False


def isalpha1(num):
    for i in range(0, len(num)):
        if num[i].isalpha():
            return True
    return False


def isdigit1(num):
    for i in range(0, len(num)):
        if num[i].isdigit():
            return True
    return False


def islower1(num):
    for i in range(0, len(num)):
        if num[i].islower():
            return True
    return False


def isupper1(num):
    for i in range(0, len(num)):
        if num[i].isupper():
            return True
    return False


if __name__ == '__main__':

    s1 = input()
    s=list(s1)
    print(isalnum1(s))
    print(isalpha1(s))
    print(isdigit1(s))
    print(islower1(s))
    print(isupper1(s))
