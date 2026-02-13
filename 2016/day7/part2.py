from pathlib import Path
print("advent of code 2016 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

number_of_valid_ips = 0

def is_ip_valid(ip):
    aba_outside_brackets = []
    bab_inside_brackets = []
    ip_chars = list(ip)
    inside_brakets = False
    for i in range(len(ip_chars)):
        if ip_chars[i]=="[":
            inside_brakets = True
        elif ip_chars[i] == "]":
            inside_brakets = False
        if i < len(ip_chars) -2:
            if "[" not in ip_chars[i:i+3] and "]" not in ip_chars[i:i+3]:
                if ip_chars[i] != ip_chars[i+1] and ip_chars[i]== ip_chars[i+2]:
                    if inside_brakets:
                        bab_inside_brackets += [ip[i:i+3]]
                    else: 
                        aba_outside_brackets += [ip[i:i+3]]
    for aba in aba_outside_brackets:
        bab = aba[1]+aba[0] +aba[1]
        if bab in bab_inside_brackets:
            # print( bab, aba, ip)
            return True
    return False


for line in file:
    if is_ip_valid(line):
        number_of_valid_ips += 1

print("The number of ips that support SSL is ", number_of_valid_ips)