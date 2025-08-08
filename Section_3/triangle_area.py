height = float(input("Please provide the length of the altitude of a vertex (called A): "))
base = float(input("Please provide the length of the base (opposite side of vertex A): "))

def area_calc(tri_h,tri_b):
    area = float(tri_h * tri_b / 2)
    print(f'The area of the given triangle is approximately {area:.5f}')

area_calc(height,base)
