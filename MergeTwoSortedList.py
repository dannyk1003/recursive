def main(list1, list2):
    answer = []
    mergeTwoList(list1, list2, answer)
    print(answer)
    


def mergeTwoList(list1, list2, answer):
    if len(list1) == 0:
        answer += list2
        return
    elif len(list2) == 0:
        answer += list1
        return

    if list1[0] > list2[0]:
        list1, list2 = list2, list1
    answer.append(list1[0])
    mergeTwoList(list1[1:], list2, answer)  


list1 = [1,3,4,5]
list2 = [1,3,4,8,10]

main(list1, list2)