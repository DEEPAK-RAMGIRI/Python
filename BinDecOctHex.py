def print_formatted(number):
    # your code goes here
    spaces = len(bin(number))-2
    for i in range(1,number+1):
        print(f"{i:>{spaces}} {oct(i)[2:]:>{spaces}} {hex(i)[2:].upper():>{spaces}} {bin(i)[2:]:>{spaces}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)