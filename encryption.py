def encrypt(message, public_key):
    """使用RSA公钥加密数据"""
    n, e = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

def write_encrypted_message_to_file(encrypted_message, filename):
    """将加密后的消息写入文件"""
    with open(filename, 'w') as f:
        f.write("%X" % encrypted_message)  # 将加密后的消息以十六进制形式写入文件

# 加载明文
def load_plaintext(filename):
    """从文件中加载明文"""
    with open(filename, 'r') as f:
        n = int(f.readline(), 16)
    return n

# 加载公钥
def load_public_key(filename):
    """从文件中加载RSA公钥"""
    with open(filename, 'r') as f:
        n = int(f.readline(), 16)
        e = int(f.readline(), 16)
    return (n, e)

# 待加密的消息
message = load_plaintext('/content/rsa_plain.txt')

# 从文件中加载公钥
public_key = load_public_key('/content/rsa_pubkey.txt')

# 使用公钥加密消息
encrypted_message = encrypt(message, public_key)

# 将加密后的消息写入文件
write_encrypted_message_to_file(encrypted_message, '/content/rsa_cipher.txt')

print("数据加密完成并已写入文件 rsa_cipher.txt")
