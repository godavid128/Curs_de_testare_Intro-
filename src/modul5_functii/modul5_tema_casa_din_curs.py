# TODO printam studentul cu max grade e maria,
#  sa schimbam lista de dict sa fie trasmisa din exterior, lista sa fie trasm ca argument la get_max_sc0re
# def get_max_score(**a):
#   # max_g = max(a, b)
#   #   return max(max_g)
#
#     maxg = int(0
#     for s in a:
#         if s > a:
#             maxg += 1
#     print(maxg)
#
# get_max_score(ion=5, maria=7)
#
# def function(**karg):
#     karg = []
#     ans = []
#     for key, value in kargs.items():
#         ans.append([key, value])
#     return ans
#
#
# object = function(First="Python", Second="Functions", Third="Tutorial")
# print(object)

# def student(**a):
#     if i in a:
#         maxi = max(a)
#         i += 1
#     return maxi
#
# print(student('ion': 5, 'maria': 7))
#
# maxim = {'ion': 5, 'maria': 7}
# maxa_value = max(maxim)
# print(maxa_value)

# Function to get sum of digits

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 66
print(getSum(n))
