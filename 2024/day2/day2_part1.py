print("advent of code 2024 day 2")

global number_of_safe_reports
number_of_safe_reports = 0

def is_report_safe(report):
    if abs(report[1] - report[0]) > 0:
        sign = "+" if report[1] > report[0] else "-"
        for i in range(len(report)-1):
            result = report[i + 1] - report[i] if sign == "+" else report[i] - report[i + 1]
            # print("result : ", result)
            if result > 0 and result < 4:
                continue
            else :
                return 0
        return 1
    else:
        return 0
    

with open('./day2.txt') as f:
    file = f.read().splitlines()

for line in file:
    report = line.split()
    for i in range(len(report)):
        report[i] = int(report[i])
    print(report)
    number_of_safe_reports += is_report_safe(report)


# print(left_col, right_col)
print("The total of safe reports is " + str(number_of_safe_reports))
