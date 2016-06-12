from DES import Tool
class Massage:
    def __init__(self, text_bits=None):
        if text_bits:
            self.text_bits = text_bits
        else:
            self.text_bits = []

        self.left_block = []
        self.right_block = []

        self.IP = [
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7,
            56, 48, 40, 32, 24, 16, 8, 0,
            58, 50, 42, 34, 26, 18, 10, 2,
            0, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6
        ]

        self.FP = [
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25,
            32, 0, 40, 8, 48, 16, 56, 24
        ]

        self.E = [
            31, 0, 1, 2, 3, 4,
            3, 4, 5, 6, 7, 8,
            7, 8, 9, 10, 11, 12,
            11, 12, 13, 14, 15, 16,
            15, 16, 17, 18, 19, 20,
            19, 20, 21, 22, 23, 24,
            23, 24, 25, 26, 27, 28,
            27, 28, 29, 30, 31, 0
        ]

        self.S = [
            # S1
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
             0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
             4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
             15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

            # S2
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
             3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
             0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
             13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

            # S3
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
             13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
             13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
             1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

            # S4
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
             13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
             10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
             3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

            # S5
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
             14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
             4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
             11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

            # S6
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
             10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
             9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
             4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

            # S7
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
             13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
             1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
             6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

            # S8
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
             1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
             7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
             2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]

        self.P = [
            15, 6, 19, 20, 28, 11,
            27, 16, 0, 14, 22, 25,
            4, 17, 30, 9, 1, 7,
            23, 13, 31, 26, 2, 8,
            18, 12, 29, 5, 21, 10,
            3, 24
        ]

    def apply_IP(self, block=None):
        if block:
            r = []
            r.extend(block)
            for i in range(0, 64):
                r[i] = block[self.IP[i]]
            return r

        else:
            if len(self.text_bits) != 64:
                print("error in apply_IP\n")
                exit()
            r = []
            r.extend(self.text_bits)
            for i in range(0, 64):
                r[i] = self.text_bits[self.IP[i]]
            self.text_bits = r

    def apply_FP(self, block=None):
        if block:
            r = []
            r.extend(block)
            for i in range(0, 64):
                r[i] = block[self.FP[i]]
            return r

        else:
            if len(self.text_bits) != 64:
                print("error in apply_IP\n")
                exit()
            r = []
            r.extend(self.text_bits)
            for i in range(0, 64):
                r[i] = self.text_bits[self.FP[i]]
            self.text_bits = r

    def e_box(self, block):
        tmp = []
        for i in range(48):
            tmp.append(block[self.E[i]])
        return  tmp

    def s_box(self, block):
        tmp = []
        tmp.extend(block)
        r = []
        for i in range(0, 48, 6):
            j = i + 6
            r.append(tmp[i:j])

        tmp.clear()
        for i in range(0, 8):
            raw = 1 * r[i][0] + 2 * r[i][5]
            col = 1 * r[i][1] + 2 * r[i][2] + 4 * r[i][3] + 8 * r[i][4]
            res = self.S[i][raw * 16 + col - 1]
            res_bin = Tool.to_binary(res)
            tmp.extend(res_bin[4:])
        return tmp

    def p_box(self, block):
        r = []
        r.extend(block)
        for i in range(32):
            r[i] = block[self.P[i]]
        return r


    def iterate(self, left_block, right_block, keys):
        for j in range(0, 16):
            tmp = []
            tmp.extend(right_block)
            right_block = self.e_box(right_block)

            for i in range(48):
                right_block[i] ^= keys[j][i]

            right_block = self.s_box(right_block)
            right_block = self.p_box(right_block)

            for i in range(32):
                right_block[i] ^= left_block[i]

            left_block = []
            left_block.extend(tmp)

        return left_block, right_block



    def encrypt(self, start, end, keys, text_bits=None):
        block = []
        if text_bits:
            for i in range(start, end):
                block.append(text_bits[i])
        else:
            for i in range(start, end):
                block.append(self.text_bits)

        block = self.apply_IP(block)
        left_block = block[0:32]
        right_block = block[32:64]

        left_block, right_block = self.iterate(left_block, right_block, keys)

        block = []
        block.extend(right_block)
        block.extend(left_block)

        block = self.apply_FP(block)

        cipher_block = ''
        for i in block:
            cipher_block += str(i)
        return cipher_block