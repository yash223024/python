import math


def spherical_cap_volume():
    r = float(input("Enter the radius of the sphere (r): "))
    h = float(input("Enter the height of the spherical cap (h): "))

    volume = (math.pi / 6) * h * (3 * r ** 2 + h ** 2)
    print(f"Volume of the spherical cap: {volume:.2f}")


if __name__ == "__main__":
    spherical_cap_volume()