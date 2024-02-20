#!/usr/bin/env python3
import random

test_seed = int(input("enter your seed: "))
random.seed(test_seed)

seed_HT = random.randint(0, 1)
if seed_HT == 0:
    print("Heads")
elif seed_HT == 1:
    print("Tails")
else:
    print("enter some value")
