def plusone(digits):
    n= len(digits)
    for  i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = =
    return [1] + digits
s= [1, 2, 3]
print(plusone(s))
