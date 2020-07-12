# champions = ['Corinthians', 'Barcelona', 'Milan', 'Liverpool', 'Real Madrid']

# for champion in champions:
#     print(champion, 'is a World Champion')
#     print('But Palmeiras is not')

# userInput = input('Choose a World Champion: ')

# for item in userInput:
#     print(item)

# for letter in 'ComIT':
#    print('Current Letter :', letter)

# for y in [0, 2, 6, 8]:
#     print("Number:", y)

# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:
#    print('Current fruit :', fruit)

# for index in range(len(fruits)):
#    print('Current fruit :', fruits[index])
   
# nums = [0,2,3,4,6,7,8,9]
# is_even = lambda x: x % 2 == 0
# even_num = filter(is_even, nums)

# for enum in even_num:
#     print(enum)

# string = 'Bruno Verussa Porto Cardoso'

# print(string.strip())
# print(string.replace(' ', '-'))
# print(string.split())
# print('**'.join(string.split()))
# print('*'.join(string))

def recursion_test(num):
    if(num > 0):
        result = num + recursion_test(num -1)
        print(result)
    else:
        result = 0
    return result

recursion_test(10)