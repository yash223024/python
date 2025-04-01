def trapezoid_area():
    a = float(input("Enter the length of first parallel side (a): "))
    b = float(input("Enter the length of second parallel side (b): "))
    h = float(input("Enter the height of the trapezoid (h): "))

    area = 0.5 * (a + b) * h
    print(f"Area of the trapezoid: {area:.2f}")


if __name__ == "__main__":
    trapezoid_area()