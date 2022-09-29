test = ['a', 'b', 'c']

def Perm(element):
    s = []
    if len(element) == 1:
        return [element]
    else:
        for i in range(len(element)):
            print('i=', i)
            element[i], element[0] = element[0], element[i]
            temp = Perm(element[1:])
            print('temp = ', temp)
            for j in temp:
                print('j=', j)
                s.append([element[0]] + j)
                print('s=', s)
            element[0], element[i] = element[i], element[0]
    return s




Perm(test)


