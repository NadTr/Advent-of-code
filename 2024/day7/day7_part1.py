from pathlib import Path
print("advent of code 2024 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:       
    file = f.read().splitlines()

def is_calibrated(result, possibilities):
    results = [possibilities[0]]
    for number in possibilities[1:]:
        for j in range(len(results)):
            temp = results[j]
            res1 = results[j] + number
            res2 = results[j] * number
            results[j] = res1
            results.append(res2)
    
    return result if result in results else 0 
            

total_calibration_result = 0

for line in range(len(file)):
    row = file[line].split(":")
    calibrations_numbers = row[1].split()
    for i in range(len(calibrations_numbers)):
        calibrations_numbers[i] = int(calibrations_numbers[i])

    total_calibration_result += is_calibrated(int(row[0]), calibrations_numbers)
        
print("The total calibration result is  " + str(total_calibration_result))
