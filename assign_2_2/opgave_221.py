import random

for seed in [ 0, 1, 0 ]:
    print("Seed is: {}".format(seed))
    randomer = random.Random(seed)
    for i in range(10):
        print('{0:8.6f} '.format(randomer.random()), end='')
        print()


# in de output zie je dat bij dezelfde seedwaarde, dezelfde random getallen worden gegenereerd. Niet alleen het eerste getal, maar de hele serie is identiek: reproduceerbaarheid is hier de eigenschap.


