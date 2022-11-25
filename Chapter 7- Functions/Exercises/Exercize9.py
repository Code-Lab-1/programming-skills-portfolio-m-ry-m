#create a recursive function to calculate the sum of numbers from 0 to 10
def ad(num):
    if num:
        return num + ad(num - 1)
    else:
        return 0

res = ad(10)
print(res)