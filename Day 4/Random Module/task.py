import random

rand_num = random.randint(1, 10)

rand_num_0_to_1 = random.random()

random_float = random.uniform(1, 10)

"""print(rand_num)

print(rand_num_0_to_1)

print(random_float)"""

coin_flip = float(random.randint(0, 1))
if coin_flip >= .5:
    print("Heads")
else:
    print("Tails")