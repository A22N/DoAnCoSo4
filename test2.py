import random


# def generateLargePrime(keysize):
#     """
#         trả về số nguyên tố ngẫu nhiên cảu các bit với keysize đúng kích thước
#     """

#     while True:
#         num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
#         if (isPrime(num)):
#             return num


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


# def isPrime(n):
#     """
#         lấy n nếu là số nguyên tố
#         chạy lại rabinMiller nếu ko chắc
#     """

#     # 0, 1, - các số đéo phải số nguyên tố
#     if n < 2:
#         return False

#     # nếu trong lowPrimes
#     if n in lowPrimes:
#         return True

#     # nếu số nguyên tố thấp thì chia n
#     for prime in lowPrimes:
#         if n % prime == 0:
#             return False

#     # tìm c sao cho c * 2 ^ r = n - 1
#     c = n - 1  # nếu c chẵn thì méo chia hết cho 2
#     while c % 2 == 0:
#         c /= 2  # làm cho c lẻ

#     # chứng minh không phải số nguyên tố 128 lần
#     for i in range(128):
#         if not rabinMiller(n, c):
#             return False

#     return True


def generateKeys(keysize=1024):
    d = 6194595167263017367
    N = 8162538439577164469
    # # lấy p và q và là số nguyên tố
    # p = generateLargePrime(keysize)
    # q = generateLargePrime(keysize)

    # # print(f"p: {p}")
    # # print(f"q: {q}")

    # N = p * q  # RSA Modulus (mô đun của RSA)
    # phiN = (p - 1) * (q - 1)  # bí mật dùng để tạo khóa bí mật

    # # chọn d
    # # d là chìa khóa bí mật bởi e và phiN, e * d (mod phiN) = 1
    # d = modularInv(e, phiN)

    return d, N


# def isCoPrime(p, q):
#     """
#         trả về Đúng nếu gcd(p, q) là 1
#          tương đối nguyên tố
#     """

#     return gcd(p, q) == 1


# def gcd(p, q):
#     """
#         euclidean algorithm to find gcd of p and q
#     """

#     while q:
#         p, q = q, p % q
#     return p


# def egcd(a, b):
#     s = 0
#     old_s = 1
#     t = 1
#     old_t = 0
#     r = b
#     old_r = a

#     while r != 0:
#         quotient = old_r // r
#         old_r, r = r, old_r - quotient * r
#         old_s, s = s, old_s - quotient * s
#         old_t, t = t, old_t - quotient * t

#     # return gcd, x, y
#     return old_r, old_s, old_t


# def modularInv(a, b):
#     gcd, x, y = egcd(a, b)

#     if x < 0:
#         x += b

#     return x


class RSA(object):

    def __init__(self, keysize=1024):
        self.keysize = keysize
        self.d, self.N = generateKeys(self.keysize)

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
    msg = "4338925795335007509 2250885545973950306 1315998609886226794"
    rsa = RSA(keysize=32)
    dec = rsa.decrypt(cipher=msg)

    print(f"dec: {dec}")
