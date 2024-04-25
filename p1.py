I = list(map(int, input().split()))

S = I[0] ** 2  # area for square
C = 3.14 * (I[1] ** 2)  # area for circle

print("SQUARE" if S > C else "CIRCLE")
