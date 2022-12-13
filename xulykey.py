import random
import textract
# from frame import Ui_MainWindow
# modulo là N

# số nguyên tố nhỏ hơn 1000
lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
             449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def generateLargePrime(keysize):
    """
        trả về số nguyên tố ngẫu nhiên cảu các bit với keysize đúng kích thước
    """

    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num


def rabinMiller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)  # a^d%n
    if x == 1 or x == n - 1:
        return True

    # bình phương x
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    # không phải là số nguyên tố
    return False


def isPrime(n):
    """
        lấy n nếu là số nguyên tố
        chạy lại rabinMiller nếu ko chắc
    """

    # 0, 1, - các số đéo phải số nguyên tố
    if n < 2:
        return False

    # nếu trong lowPrimes
    if n in lowPrimes:
        return True

    # nếu số nguyên tố thấp thì chia n
    for prime in lowPrimes:
        if n % prime == 0:
            return False

    # tìm c sao cho c * 2 ^ r = n - 1
    c = n - 1  # nếu c chẵn thì méo chia hết cho 2
    while c % 2 == 0:
        c /= 2  # làm cho c lẻ

    # chứng minh không phải số nguyên tố 128 lần
    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True


def generateKeys(keysize=1024):
    e = d = N = 0

    # lấy p và q và là số nguyên tố
    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    # print(f"p: {p}")
    # print(f"q: {q}")

    N = p * q  # RSA Modulus (mô đun của RSA)
    phiN = (p - 1) * (q - 1)  # bí mật dùng để tạo khóa bí mật

    # chọn e
    # e là số nguyên tố cùng với phiN & 1 < e <= phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break

    # chọn d
    # d là chìa khóa bí mật bởi e và phiN, e * d (mod phiN) = 1
    d = modularInv(e, phiN)

    return p, q, e, d, N


def isCoPrime(p, q):
    """
        trả về Đúng nếu gcd(p, q) là 1
         tương đối nguyên tố
    """

    return gcd(p, q) == 1


def gcd(p, q):
    """
        euclidean algorithm to find gcd of p and q
    """

    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t


def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


class RSA(object):

    def __init__(self, keysize=1024):
        self.keysize = keysize
        self.p, self.q, self.e, self.d, self.N = generateKeys(self.keysize)

    def encrypt(self, msg):
        cipher = ""

        for c in msg:
            m = ord(c)
            cipher += str(pow(m, self.e, self.N)) + " "

        return cipher

    def decrypt(self, cipher):
        msg = ""

        parts = cipher.split()
        for part in parts:
            if part:
                c = int(part)
                msg += chr(pow(c, self.d, self.N))

        return msg


if __name__ == "__main__":
    print("Hợp đồng điện tử")
    # msg = textract.process("D:\Ki_1_nam_3\DoAn/hop_dong.docx")
    msg = input("msg:")
    rsa = RSA(keysize=32)
    enc = rsa.encrypt(msg=msg)
    dec = rsa.decrypt(cipher=enc)

    print(f"Message: {msg}")
    print(f"p: {rsa.p}")
    print(f"q: {rsa.q}")
    print(f"e: {rsa.e}")
    print(f"d: {rsa.d}")
    print(f"N: {rsa.N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")
