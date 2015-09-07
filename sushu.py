#coding=utf-8


def is_prime(n):
    list_num = []
    for i in xrange(2,n):
        for num in range(2, int(sqrt(0)) + 1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == (int(sqrt(n))):
                list_num.append
    return list_num

print is_prime(100)