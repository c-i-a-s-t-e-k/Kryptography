sage: # Odszyfruj szyfrogram S = 92056083186673327707438445422138850995
....: # RSA z kluczem {e, N},
....: # gdzie e = 65537 oraz N = p*q = 340277174544854189285703885855116560303
....: # Klasa RSA implemntująca szyfrowanie i deszyfrownaie
....: from sage.crypto.util import random_blum_prime, ascii_to_bin, bin_to_ascii
....: class RSA:
....:     def __init__(self, p, q):
....:         self.p = p
....:         self.q = q
....:         self.n = p * q
....:         self.phi = (p - 1) * (q - 1)
....:         self.e = 65537 #random_blum_prime(3, self.phi)
....:         self.d = inverse_mod(self.e, self.phi)
....:         self.block_len = len(self.n.bits()) - 1
....:         print(' e= ',self.e,' d= ', self.d)
....:     def get_public_key(self):
....:         return self.e, self.n
....:
....:     def get_private_key(self):
....:         return self.d, self.n
....:
....: # wyznacza długośc bloku szyfrogramu
....:     def get_block_length(self):
....:         return self.block_len
....:
....: # szyfrowanie RSA
....:     def encrypt(self, message):
....:         raw = ascii_to_bin(message)
....:         blocks = (raw[i * self.block_len: (i + 1) * self.block_len]
....:             for i in range(0, ceil(len(raw) / self.block_len)))
....:         cipher = [power(int(str(block), 2), self.e, self.n) for block in blocks]
....:         return cipher
....:
....:     def _get_bin_block(self, block, width):
....:         blen = self.block_len
....:         block = bin(block)[2:]
....:         block = "0" * (width - len(block)) + block
....:         return block
....: # deszyfrownia RSA
....:     def decrypt(self, cipher, msg_len):
....:         blocks = [power(c, self.d, self.n) for c in cipher]
....:         bin_string = ""
....:         for block in blocks[:-1]:
....:             bin_string += self._get_bin_block(block, self.block_len)
....:         bin_string += self._get_bin_block(blocks[-1], msg_len * 8 - len(bin_string))
....:         return bin_to_ascii(bin_string[0 : msg_len * 8])
....:
....:
....: size = 64
....: p = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
....: q = random_blum_prime(2 ** (size-1) +1, 2 ** size -1)
....: #p=43
....: #q=31
....:
....: rsa = RSA(p, q)
....: msg = "ala ma kota"
....: res = rsa.encrypt(msg)
....: print (res, ' zdeszyfrowano ', rsa.decrypt(res, len(msg)))
