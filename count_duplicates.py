import time


def decorator(f1, f2):
    def new_counter(string):
        initial_time = time.time()
        f1(string)
        f1_time = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        f2_time = time.time() - initial_time
        print(f1.__name__ if f1_time < f2_time else f2.__name__)
    return new_counter

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

function = decorator(count_duplicates, letters)
function('aaaBBB')