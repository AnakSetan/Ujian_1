def calculate_years(p0,interest,tax,d):
    year = 0
    for item in range(4): 
        if p0 < d:
            p0 = p0 + (p0 * interest/100) + tax
            year += 1
        else :
            break
    return year
print(calculate_years(1000,0.05,0.18,1100))