tolerance = 0.000001
def newton(x, estimate):
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference > tolerance:
        estimate = newton(x, estimate)
    return estimate

def main():
    while True:
        import math
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        print("The program's estimate is", newton(x,1))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
