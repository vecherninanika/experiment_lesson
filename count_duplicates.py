def count_duplicates(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])


# найти кол-во дублирующихся букв
def letters(string):
    list_1 = []
    list_2 = []
    res = 0
    for letter in string:
        if letter in list_1 and letter not in list_2:
            res += 1
            list_2.append(letter)
        else:
            list_1.append(letter)
    return res
