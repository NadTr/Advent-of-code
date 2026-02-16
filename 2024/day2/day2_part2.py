from pathlib import Path
print("advent of code 2024 day 2")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:    
    file = f.read().splitlines()

number_of_safe_reports = 0

def is_report_safe(report, safety_number):
    if abs(report[1] - report[0]) > 0:
        sign = "+" if report[1] > report[0] else "-"
        for i in range(len(report)-1):
            result = report[i + 1] - report[i] if sign == "+" else report[i] - report[i + 1]
            if result > 0 and result < 4:
                continue
            else :
                if safety_number == 1:
                    return 0
                else:
                    new_report1 = report[:i]+report[i+1:]
                    new_report2 = report[:i + 1]+report[i+2:]
                    new_report3 = report[:i -1]+report[i:]
                    return is_report_safe(new_report1, 1) + is_report_safe(new_report2, 1)+ is_report_safe(new_report3, 1)
        
        return 1
    else:
        return 0 if safety_number == 1 else is_report_safe(report[1:], 1)
        

for line in file:
    report = line.split()
    for i in range(len(report)):
        report[i] = int(report[i])
    number_of_safe_reports +=  1 if is_report_safe(report, 0) >=1  else 0

print("The total of safe reports is ", number_of_safe_reports)
