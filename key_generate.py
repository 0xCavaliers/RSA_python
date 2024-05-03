import random
from sympy import mod_inverse

def generate_prime(bits):
    """生成一个指定位数的素数"""
    while True:
        num = random.getrandbits(bits)
        if num > 1 and is_prime(num):
            return num

def is_prime(num, rounds=20):
    """检查一个数是否为素数"""
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False

    # Miller-Rabin素数检测算法
    s = 0
    d = num - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in range(rounds):
        a = random.randint(2, num - 1)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

def generate_keypair(bits):
    """生成RSA密钥对"""
    # 生成两个大素数
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    # 计算n和φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # 选择e，满足1 < e < φ(n)，且e与φ(n)互质
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # 计算d，即e的模反元素
    d = mod_inverse(e, phi)

    # 返回公钥和私钥
    return ((p, q, n, e, d))

def gcd(a, b):
    """计算a和b的最大公约数"""
    while b != 0:
        a, b = b, a % b
    return a

def write_key_to_file(key, filename):
    """将密钥写入文件"""
    with open(filename, 'w') as f:
        for item in key:
            f.write("%X\n" % item)

# 测试
bits = 1024
key = generate_keypair(bits)

# 将生成的素数 p、q，以及 n、e、d 分别写入文件
write_key_to_file(key[:3], 'p.txt')
write_key_to_file(key[0:2] + (key[2],), 'q.txt')
write_key_to_file([key[2]], 'n.txt')
write_key_to_file([key[3]], 'e.txt')
write_key_to_file([key[4]], 'd.txt')

print("密钥写入完成")
