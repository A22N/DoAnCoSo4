def generateKeys(keysize=1024):
    d = 6194595167263017367
    N = 8162538439577164469
    return d, N


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
