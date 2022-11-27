import random

for seed in [ 0, 1, 0 ]:
    print("Seed is: {}".format(seed))
    randomer = random.SystemRandom(seed)
    for i in range(10):
        print('{0:8.6f} '.format(randomer.random()), end='')
        print()

# alle randomgetallen zijn nu verschillend. Waar komt dit door?
# Voor deze opgave wordt random.SystemRandom(seed) gebruikt terwijl bij de voorgaande random.Random(seed) wordt gebruikt
# In de pyhton documentatie van SystemRandom (https://docs.python.org/3/library/random.html#random.SystemRandom) staat dat SystemRandom gebruik maakt van os.urandom(). Deze generator is niet reproduceerbaar terwijl de Random(seed) dat wel is.


