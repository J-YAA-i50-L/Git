def is_correct_mobile_phone_ru(nomer):
    if 11 == len(nomer):
        if nomer[0] == '8':
            return 'YES'
        else:
            return 'NO'
    if 12 == len(nomer):
        if nomer[:2] == '+7':
            return 'YES'
        else:
            return 'NO'
    elif len(nomer) > 12:
        if nomer[0] == '8':
            if (len(nomer) == 13 and nomer.find('(') == 1 and nomer.find(')') == 5
               and nomer.count('(') == 1 and nomer.count(')') == 1):
                return 'YES'
            elif (len(nomer) == 15 and nomer.count('-') == 2 and nomer.count(' ') == 2
                  and len(nomer[1:6].strip()) == 3 and nomer[9] == '-' and nomer[12] == '-'):
                return 'YES'
            else:
                return 'NO'
        if nomer[:2] == '+7':
            if (len(nomer) == 14 and nomer.find('(') == 2 and nomer.find(')') == 6
               and nomer.count('(') == 1 and nomer.count(')') == 1):
                return 'YES'
            elif (len(nomer) == 16 and nomer.count('-') == 2 and nomer.count(' ') == 2
                  and len(nomer[2:7].strip()) == 3 and nomer[10] == '-' and nomer[13] == '-'):
                return 'YES'
            else:
                return 'NO'
    else:
        return 'NO'


print(is_correct_mobile_phone_ru(input()))
