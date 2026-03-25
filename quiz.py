import math, random, numpy

scores = []
score = 0

def question():
    div = False
    random_num = random.randint(1, 50)
    if random_num <= 10 and random_num > 1:
        x = 6
        random_num_2 = random.randint(2, 6)
        factorial = random.randint(5, 10)
    elif random_num <= 20:
        x = 4
        random_num_2 = random.randint(5, 20)
    else:
        random_num_2 = random.randint(1, 50)
        x = 2
        random_num *= 2
        random_num_2 *= 2
    if random_num % random_num_2 == 0:
        x += 1
        div = True
    
    question = random.randint(1, x)

    if question == x and div:
        answer = random_num / random_num_2
        selection = input(f"what is {random_num} divided by {random_num_2}? ")
        points = 2
    elif question == 1:
        answer = random_num + random_num_2
        selection = input(f"what is {random_num} + {random_num_2}? ")
        points = 1
    elif question == 2:
        answer = random_num - random_num_2
        selection = input(f"what is {random_num} - {random_num_2}? ")
        points = 1
    elif question == 3:
        answer = random_num * random_num_2
        selection = input(f"what is {random_num} X {random_num_2}? ")
        points = 2
    elif question == 4:
        answer = random_num
        selection = input(f"what is the square root of {random_num ** 2}? ")
        points = 3
    elif question == 5:
        answer = random_num ** random_num_2
        selection = input(f"what is {random_num} to the power of {random_num_2}? ")
        points = 3
    elif question == 6:
        answer = math.factorial(factorial)
        selection = input(f"what is {factorial} factorial? ")
        points = 3
    
    try:
        selection = int(selection)
    except:
        input("that isnt even a number")
        points = 0
    else:
        if selection == answer:
            input(f"correct! +{points} points")
        else:
            input(f"incorrect, the answer is {answer}")
            points = 0
    
    return points

playing = True
while playing:
    score = 0
    for i in range(0, 5):
        score += question()
    scores.append(score)
    print(f"your final score for that round was {score}")
    continues = ""
    while continues != "Y" and continues != "N":
        continues = input("would you like to continue? Y/N: ")
        continues = continues.upper()
    if continues == "N":
        playing = False

scores = numpy.array(scores)
print(f"your highest score was {numpy.max(scores)}")
print(f"your lowest score was {numpy.min(scores)}")
print(f"your average score was {round(numpy.mean(scores), 2)}")
    