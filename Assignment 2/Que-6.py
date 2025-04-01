def rectangular_parallelepiped_area():
    a = float(input("Enter length (a): "))
    b = float(input("Enter width (b): "))
    c = float(input("Enter height (c): "))

    surface_area = 2 * (a * b + a * c + b * c)
    print(f"Total surface area of the rectangular parallelepiped: {surface_area:.2f}")


if __name__ == "__main__":
    rectangular_parallelepiped_area()