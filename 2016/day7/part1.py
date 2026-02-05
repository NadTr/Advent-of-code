print("advent of code 2016 day 7")

with open('./input.txt') as f:
    file = f.read().splitlines()

number_of_valid_ips = 0

def is_ip_valid(ip):
    ip_chars = list(ip)
    inside_brakets = False
    one_ip_valid = False
    for i in range(len(ip_chars)):
        if ip_chars[i]=="[":
            inside_brakets = True
        elif ip_chars[i] == "]":
            inside_brakets = False
        if i < len(ip_chars) -3:
            if "[" not in ip_chars[i:i+4] and "]" not in ip_chars[i:i+4]:
                if ip_chars[i] != ip_chars[i+1] and ip_chars[i]+ip_chars[i+1] == ip_chars[i+3]+ip_chars[i+2]:
                    if inside_brakets:
                        if "]" in ip_chars[i:]:
                            print("ip not valid", i, i+4, ip[i:i+4])
                            return False
                        else: 
                            one_ip_valid = True
                            print("ip not have end ]", ip[i:])
                    else:
                        print("found one abba not inside brakets", ip[i:i+4], ip)
                        one_ip_valid = True
    return one_ip_valid


for line in file:
    if is_ip_valid(line):
        number_of_valid_ips += 1

print("The number of ips that supprt TLS is ", number_of_valid_ips)