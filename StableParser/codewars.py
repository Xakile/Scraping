def playbj(name):
    # R or r --> paly bango elif not play bango
    names = []
    for Symbol_start in str(name):
        names.append(Symbol_start)
    if 'r' or 'R' in names[0]:
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name

def lovefunc( flower1, flower2 ):
    #если у одного цветка четное число а у другого не четное то они влюблены
    #flower_one = int(flower1) % 2
    #flower_two = int(flower2) % 2
    #if flower_one == 0 or flower_two == 0:
    #    if flower_one != 0 or flower_two != 0:
    #        result = 'True'
    #    else:
    #       result = 'False'
    #else:
    #    result = 'False'

    return (flower1+flower2)%2 # более простое решение

def make_negative( number ):
    if number < 0:
        number_result = number
    else:
        number_result = number * -1
    
    return print(number_result)

def rps(p1, p2):
    if p1 == p2:
        return print('Draw!')
    win = len(p1) + len(p2)
    if win == 9:
        if p1 == 'paper':
            return print("Player 1 won!")
        else:
            return print("Player 2 won!")
    if win == 12:
        if p1 == 'rock':
            return print("Player 1 won!")
        else:
            return print("Player 2 won!")
    if win == 13:
        if p1 == 'scissors':
            return print("Player 1 won!")
        else:
            return print("Player 2 won!")

def opposite(number):
    return -number

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count = 0
    negative = []
    for i in arr:
        if i > 0:
            count += 1
        if i < 0:
            negative.append(i)
    summ = sum(negative)
    result = [count, summ]
    return result

def hero(bullets, dragons):
    if (dragons*2) - bullets >= 0:
        return True
    else:
        return False

def is_divide_by(number, a, b):
    return (number % a) == (number % b) == 0

def solution(string):
    return string[::-1]

def printer_error(s):
    alpha_good = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    alpha_bed = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    numerator = []
    for i in s:
        if i in alpha_bed:
            numerator.append(i)
    return (str(len(numerator)) +'/'+ str(len(s)))

def digitize(n):
    nums = str(n).replace("",' ').strip().split()
    re = []
    for num in nums:
        re.append(int(num))
    return re[::-1]

def min_max(lst):
    return [min(lst), max(lst)]

def disemvowel(string_):
    #return string_.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').lower()
    return "".join(c for c in string_ if c.lower() not in "aeiou") #лучшие решение

def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result

def filter_list(l):
    return [i for i in l if not isinstance(i, str)]
    #for i in l:
    #    if isinstance(i, int) != True:
    #        l.remove(i)
    #        filter_list(l)
    #        return l

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2
    #return eval("{}{}{}".format(value1, operator, value2))

def series_sum(n):
    result = 0
    for i in range(n):
        result += 1/(1 + 3*i)
    print(str("%.2f" % result))

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
