print("advent of code 2017 day 1")

with open('./input.txt') as f:
    file = f.read()

def add_captcha(line):
    result = 0
    for i in range(len(line)):
        digit = line[i]
        next_digit = line[i+1] if i < len(line) - 1 else line[0]
        if digit == next_digit:
            result += int(digit)
        # print(line, digit, next_digit, result)

    return result

captcha_sum = add_captcha(file)

print("The solution of the captcha is", captcha_sum)