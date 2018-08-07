import random as random

#QUESTION: A six-sided die is repeatedly rolled until an even number is rolled. Determine the expectation of the sum of the rolled values (including the final even number).

no_trials = 10000
tot = 0

for i in range(no_trials):
    sum_value = 0
    b = True
    while b:
        a = random.randint(1,6)
        if a % 2 == 0:
            b = False
        sum_value += a
    tot += sum_value

average = tot / no_trials
print(average)
print(a)
