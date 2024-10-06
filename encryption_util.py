from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f'{iv}:{ct}'

def decrypt(data, key):
    iv, ct = data.split(':')
    cipher = AES.new(key, AES.MODE_CBC, iv=base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(ct)), AES.block_size)
    return pt.decode('utf-8')
