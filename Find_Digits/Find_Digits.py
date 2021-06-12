def findDigits(n):
    # Write your code here
    digits = [int(d) for d in str(n)]
    out_lst = [d for d in digits if d != 0 and n % d == 0]
    return len(out_lst)