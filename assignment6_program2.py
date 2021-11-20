import random
num1 = random.randint(0,99)
num2 = random.randint(0,99)
num3 = random.randint(0,99)
num4 = random.randint(0,99)
num5 = random.randint(0,99)
num6 = random.randint(0,99)
num7 = random.randint(0,99)
num8 = random.randint(0,99)
num9 = random.randint(0,99)
num10 = random.randint(0,99)
num11 = random.randint(0,99)
num12 = random.randint(0,99)
num13 = random.randint(0,99)
num14 = random.randint(0,99)
num15 = random.randint(0,99)
num16 = random.randint(0,99)
num17 = random.randint(0,99)
num18 = random.randint(0,99)
num19 = random.randint(0,99)
num20 = random.randint(0,99)

OverallScore = 10
score = 0

number1 = float(input(f"1. {num1} + {num2} = "))
if number1 == num1 + num2:
    score = score + 1
else:
    score = score + 0

number2 = float(input(f"2. {num3} + {num4} = "))
if number2 == num3 + num4:
    score = score + 1
else:
    score = score + 0

number3 = float(input(f"3. {num5} + {num6} = "))
if number3 == num5 + num6:
    score = score + 1
else:
    score = score + 0

number4 = float(input(f"4. {num7} + {num8} = "))
if number4 == num7 + num8:
    score = score + 1
else:
    score = score + 0

number5 = float(input(f"5. {num9} + {num10} = "))
if number5 == num9 + num10:
    score = score + 1
else:
    score = score + 0

number6 = float(input(f"6. {num11} + {num12} = "))
if number6 == num11 + num12:
    score = score + 1
else:
    score = score + 0

number7 = float(input(f"7. {num13} + {num14} = "))
if number7 == num13 + num14:
    score = score + 1
else:
    score = score + 0

number8 = float(input(f"8. {num15} + {num16} = "))
if number8 == num15 + num16:
    score = score + 1
else:
    score = score + 0

number9 = float(input(f"9. {num17} + {num18} = "))
if number9 == num17 + num18:
    score = score + 1
else:
    score = score + 0

number10 = float(input(f"10. {num19} + {num20} = "))
if number10 == num19 + num20:
    score = score + 1
else:
    score = score + 0

print(f"Your score is {score}/10.")