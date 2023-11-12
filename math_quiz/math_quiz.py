import random
import math
def randomNumGenerator(lowerNum, upperNum):
    """
    Generates a random number between lowerNum and upperNum.
    """
    lowerNum = math.ceil(lowerNum)
    upperNum = math.ceil(upperNum)
    return random.randint(lowerNum, upperNum)


def randomOperatorGenerator():
    """
    A random operator get choosed..
    """
    return random.choice(['+', '-', '*'])


def printResult(firstNum, secondNum, operator):
    """
    Based on the chosen operator, the result would be p
    """
    problem = f"{firstNum} {operator} {secondNum}"

    if operator == '+':
        result = firstNum + secondNum
    elif operator == '-':
        result = firstNum - secondNum
    else:
        result = firstNum * secondNum
    return problem, result

def math_quiz():
    score = 0
    totalQuestions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(math.floor(totalQuestions)):
        firstNum = randomNumGenerator(1, 10)
        secondNum = randomNumGenerator(1, 5.5)
        operator = randomOperatorGenerator()

        PROBLEM, ANSWER = printResult(firstNum, secondNum, operator)
        print(f"\nQuestion: {PROBLEM}")
        try:
                
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        except:
            print("Wrong input")
    print(f"\nGame over! Your score is: {score}/{math.floor(totalQuestions)}")

if __name__ == "__main__":
    math_quiz()
