import cmath


def polar_coordinates(z):
    r, fi = cmath.polar(z)
    return r, fi


if __name__ == '__main__':
    z = complex(input())
    for num in polar_coordinates(z):
        print(num)