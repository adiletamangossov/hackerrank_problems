width = int(input())
sign = "H"

for row in range(width):
    print((sign * row).rjust(width - 1) + sign + (sign * row).ljust(width - 1))

for row in range(width + 1):
    print((sign * width).center(width * 2) +
          (sign * width).center(width * 6))

for row in range((width + 1) // 2):
    print((sign * width * 5).center(width * 6))

for row in range(width + 1):
    print((sign * width).center(width * 2) +
          (sign * width).center(width * 6))

for row in range(width):
    print(((sign * (width - row - 1)).rjust(width) + sign +
          (sign * (width - row - 1)).ljust(width)).rjust(width * 6))
