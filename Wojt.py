s = 'azcbobobegghaklbeggj'
a = 0
b = 2
x = 0

def isInAlphabeticalOrder(substr):
    return substr==''.join(sorted(substr))

for i in range(len(s) - 1):
    if isInAlphabeticalOrder(s[a:b]):
        if len(s[a:b]) > x:
            x = len(s[a:b])
            longOrdered = s[a:b]
        b += 1
    else:
        a = b - 1; b += 1

print('Longest substring in alphabeticowels:', longOrdered)