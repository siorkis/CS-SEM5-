import math
import random
import decimal


class RSA:
    # primes = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    modulo = 0
    public_exp = 0
    secret_exp = 0
    eiler_value = 0

    @staticmethod
    def gcd(p, q):
        while q != 0:
            p, q = q, p % q
        return p

    def coprime(self, eiler_val):
        RSA.public_exp = 17
        while self.gcd(eiler_val, RSA.public_exp) != 1:
            RSA.public_exp += 1
        print(RSA.public_exp, "It's your public key")

    @staticmethod
    def secret_e(public_exponent, eiler_val):
        RSA.secret_exp = (eiler_val + 1) / public_exponent
        print(RSA.secret_exp, "It's your secret key")

    @staticmethod
    def str_to_num(message):
        message = message.upper()
        output = ''
        for char in message:
            output += str(ord(char))
        return output

    @staticmethod
    def public_first(list_primes):
        p = random.choice(list_primes)
        q = random.choice(list_primes)

        if p == q:
            while True:
                q = random.choice(list_primes)
                if q != p:
                    break

        RSA.modulo = p * q
        RSA.eiler_value = (p - 1)*(q - 1)
        # return modulo, eiler_value

    def encryption(self, msg):
        msg = int(msg)
        self.public_first(RSA.primes)
        self.coprime(RSA.eiler_value)

        self.secret_e(RSA.public_exp, RSA.eiler_value)

        message = pow(msg, RSA.public_exp)
        message = math.fmod(message, RSA.modulo)

        return message

    @staticmethod
    def decryption(encrypted):
        private_key = float(input("Enter your secret key\n"))

        if private_key != RSA.secret_exp:
            return "Wrong private key"
        # decimal.getcontext().prec = 1000
        # message = decimal.Decimal(0)
        # message = decimal.Decimal(encrypted) ** decimal.Decimal(private_key)
        # print(message)
        # message = decimal.Decimal(message) % decimal.Decimal(RSA.modulo)

        message = pow(encrypted, private_key)
        message = math.fmod(message, RSA.modulo)
        return message

