
a = 23
print(type(a))
print(isinstance(a, int))
print(isinstance(a, bool))

# 10진, 2진, 8진, 16진 정수를 리터럴로 사용한다.
b = 0b1101
c = 0o23
d = 0x23

print(a, b, c, d, sep=",")



# python 3.x에서는 int와 long이 합쳐졌다.
# 따라서 표현 범위가 굉장히 크다
e = 2 ** 1024
print(e)
print(type(e))


