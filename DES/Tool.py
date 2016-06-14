"""
class Tool:
    def __int__(self, flag=None):
        self.flag = flag
        self.binary_list = []
        self.hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                         '0100': '4', '0101': '5', '0110': '6','0111': '7',
                        '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
                         '1100': 'c', '1101': 'd', '1110': 'e','1111': 'f'}

        # for calculation of 8-bit list for every character
        for n in range(256):
            b = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(0, 8):
                if n % 2:
                    b[7 - i] = 1
                n = n // 2
            self.binary_list.append(b)

    def to_binary(self, s):
        return self.binary_list[s]

    def left_shift(self, sub_key, n):
        for i in range(n):
            sub_key.append(sub_key.pop(0))
        return sub_key

    def bin_to_hex(self, s):
        return self.hex_dict[s]
"""
hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
            '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

hex_revesred_dict = {v: k for k, v in hex_dict.items()}

binary_list = []
bin_to_text_dict = {}

for n in range(256):
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        if n % 2:
            b[7 - i] = 1
        n = n // 2
    binary_list.append(b)

k = 0
for i in binary_list:
    string = ''
    for j in i:
        string += str(j)
    bin_to_text_dict[string] = chr(k)
    k += 1


def to_binary(s):
    return binary_list[s]


def left_shift(sub_key, n):
    for i in range(n):
        sub_key.append(sub_key.pop(0))
    return sub_key

def right_shift(sub_key, n):
    for i in range(n):
        r = []
        r.append(sub_key[len(sub_key) - 1])
        r.extend(sub_key)
        sub_key = r[:len(sub_key)]
    return sub_key


def bin_to_hex(s):
    return hex_dict[s]

def bin_to_text(s):
    return bin_to_text_dict[s]

def hex_to_bin(s):
    return hex_revesred_dict[s]
