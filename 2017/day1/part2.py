print("advent of code 2017 day 1")

with open('./input.txt') as f:
    file = f.read()

def add_captcha(line):
    result = 0
    half = len(line) // 2
    for i in range(len(line)):
        digit = line[i]
        next_digit = line[i+ half] if i < half else line[i-half]
        if digit == next_digit:
            result += int(digit)
    return result

captcha_sum = add_captcha(file)

print("The solution of the captcha is", captcha_sum)