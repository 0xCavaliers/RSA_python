def sign(message, private_key):
    """使用RSA私钥对数据进行签名"""
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def write_signature_to_file(signature, filename):
    """将签名写入文件"""
    with open(filename, 'w') as f:
        f.write("%X" % signature)  # 将签名以十六进制形式写入文件

# 加载明文
def load_plaintext(filename):
    """从文件中加载明文"""
    with open(filename, 'r') as f:
        plaintext_hex = f.read().strip()  # 读取十六进制表示的明文
        plaintext = int(plaintext_hex, 16)  # 将十六进制转换为整数
    return plaintext

# 加载私钥
def load_private_key(filename):
    """从文件中加载RSA私钥"""
    with open(filename, 'r') as f:
        d_hex = f.readline().strip()  # 读取十六进制表示的私钥参数 d
        n_hex = f.readline().strip()  # 读取十六进制表示的私钥参数 n
        d = int(d_hex, 16)  # 将十六进制转换为整数
        n = int(n_hex, 16)  # 将十六进制转换为整数
    return (d, n)

# 待签名的消息
message = load_plaintext('/content/rsa_plain.txt')

# 从文件中加载私钥
private_key = load_private_key('/content/rsa_prikey.txt')

# 使用私钥对消息进行签名
signature = sign(message, private_key)

# 将签名写入文件
write_signature_to_file(signature, '/content/rsa_sign.txt')

print("数据签名完成并已写入文件 rsa_sign.txt")
