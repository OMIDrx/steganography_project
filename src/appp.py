import random

q = '123456789qwertyuiop'

x = random.choices(q, k=7)
x = './' + ''.join(x) + '.png'

print(str(x))