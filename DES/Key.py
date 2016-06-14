from DES import Tool
from DES.Message import Massage
class Key:
    def __init__(self, flag):
        self.flag = flag
        self.all_key = []
        self.key = []
        self.one_grp = []
        self.two_grp = []
        self.text_bits = []
        self.sub_key_1 = [
            56, 48, 40, 32, 24, 16, 8,
            0, 57, 49, 41, 33, 25, 17,
            9, 1, 58, 50, 42, 34, 26,
            18, 10, 2, 59, 51, 43, 35
        ]

        self.sub_key_2 = [
            62, 54, 46, 38, 30, 22, 14,
            6, 61, 53, 45, 37, 29, 21,
            13, 5, 60, 52, 44, 36, 28,
            20, 12, 4, 27, 19, 11, 3
        ]

        self.condense = [
            13, 16, 10, 23, 0, 4,
            2, 27, 14, 5, 20, 9,
            22, 18, 11, 3, 25, 7,
            15, 6, 26, 19, 12, 1,
            40, 51, 30, 36, 46, 54,
            29, 39, 50, 44, 32, 47,
            43, 48, 38, 55, 33, 52,
            45, 41, 49, 35, 28, 31
        ]

    def encrypt(self, plaintext, key_text):
        self.all_key = []
        self.generate_keys(key_text, 0)
        if not self.all_key:
            print('generate_keys func error!\n')
            exit()
        self.get_bits(plaintext)
        self.add_pads_if_necessary()

        final_cipher = ''
        message = Massage(self.text_bits)
        for i in range(0, len(self.text_bits), 64):
            final_cipher += message.encrypt(i, i + 64, self.all_key, self.text_bits)

        hex_cipher = ''
        i = 0
        while i < len(final_cipher):
            hex_cipher += Tool.bin_to_hex(final_cipher[i:i+4])
            i += 4
        return hex_cipher


    def decrypt(self, cipher, key_text):
        self.all_key = []
        self.generate_keys(key_text, 0)
        if not self.all_key:
            print('generate_keys func error!\n')
            exit()

        self.text_bits = []
        ciphertext = ''
        for i in cipher:
            ciphertext += Tool.hex_to_bin(i)
        for i in ciphertext:
            self.text_bits.append(int(i))

        self.add_pads_if_necessary()
        self.all_key.reverse()
        bin_mess = ''
        message = Massage(self.text_bits)
        for i in range(0, len(self.text_bits), 64):
            bin_mess += message.encrypt(i, i + 64, self.all_key, self.text_bits)

        i = 0
        text_mess = ''
        while i < len(bin_mess):
            text_mess += Tool.bin_to_text(bin_mess[i:i+8])
            i = i + 8

        return text_mess.rstrip('\x00')

    def generate_keys(self, key_text, flag):
        self.key = []
        for i in key_text:
            self.key.extend(Tool.to_binary(ord(i)))
        self.one_grp = []
        self.two_grp = []
        for i in range(28):
            self.one_grp.append(self.key[self.sub_key_1[i]])
        for i in range(28):
            self.two_grp.append(self.key[self.sub_key_2[i]])

        if flag == 0:
            for i in range(0, 16):
                if i in [0, 1, 8, 15]:
                    self.one_grp = Tool.left_shift(self.one_grp, 1)
                    self.two_grp = Tool.left_shift(self.two_grp, 1)
                else:
                    self.one_grp = Tool.left_shift(self.one_grp, 2)
                    self.two_grp = Tool.left_shift(self.two_grp, 2)
                all = []
                all.extend(self.one_grp)
                all.extend(self.two_grp)
                tmp = []
                for i in range(48):
                    tmp.append(all[self.condense[i]])
                self.all_key.append(tmp)

        elif flag != 0:
            for i in range(0, 16):
                if i == 0:
                    pass
                elif i in [1, 8, 15]:
                    self.one_grp = Tool.right_shift(self.one_grp, 1)
                    self.two_grp = Tool.right_shift(self.two_grp, 1)
                else:
                    self.one_grp = Tool.right_shift(self.one_grp, 2)
                    self.two_grp = Tool.right_shift(self.two_grp, 2)
                all = []
                all.extend(self.two_grp)
                all.extend(self.one_grp)
                tmp = []
                for i in range(48):
                    tmp.append(all[self.condense[i]])
                self.all_key.append(tmp)


    def get_bits(self, plaintext):
        self.text_bits = []
        for i in plaintext:
            r = Tool.to_binary(ord(i))
            for j in range(0, 8):
                self.text_bits.append(r[j])

    def add_pads_if_necessary(self):
        num = len(self.text_bits) % 64
        if num:
            for i in range(64 - num):
                self.text_bits.append(0)