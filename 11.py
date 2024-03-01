import math

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

def calculate_angles(a, b, c):
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C = 180 - A - B
    return A, B, C

angles = calculate_angles(a, b, c)
print(f'Угол А: {round(angles[0], 1)} градусов')
print(f'Угол В: {round(angles[1], 1)} градусов')
print(f'Угол С: {round(angles[2], 1)} градусов')