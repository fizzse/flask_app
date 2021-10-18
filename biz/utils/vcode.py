import random


# 6位验证码
def generate_code():
    r = random.randint(1000, 1000000)
    s = '%06d' % r
    return s
