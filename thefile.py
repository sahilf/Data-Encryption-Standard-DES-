def conversion_text(p, var):
    # conversion of hexadecimal to binary if var=1  and vice-versa if var=0
    d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    res = ""
    if var == 1:
        for i in p:
            res += d[i]
    else:
        for i in range(0, len(p), 4):
            for key, value in d.items():
                if p[i:i + 4] == value:
                    res += key
    return res


def initialpermutaion(b):
    # initial_permutation
    mat = [58, 60, 62, 64, 57, 59, 61, 63]
    ip_result = ""
    for i in mat:
        temp = i
        while temp > 0:
            ip_result += b[temp - 1]
            temp -= 8
    return ip_result


def parity_drop(b):
    # parity_drop for key(64bits to 56bits)
    res = ""
    mat = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    for i in mat:
        res += b[i - 1]
    return res


def shifting_operation_enc(key, rounds):
    # left circular shift of key for encyption
    res = ""
    if rounds in [1, 2, 9, 16]:
        shifts = 1
    else:
        shifts = 2
    res = key[shifts:] + key[0:shifts]
    return res


def shifting_operation_dec(key, rounds):
    # left circular shift of key for decryption
    res = ""
    d = {1: 28, 2: 27, 3: 25, 4: 23, 5: 21, 6: 19, 7: 17, 8: 15, 9: 14, 10: 12, 11: 10, 12: 8, 13: 6, 14: 4, 15: 2,
         16: 1}
    shifts = d[rounds]
    res = key[shifts:] + key[0:shifts]
    return res


def key_generation(key):
    # generate key for each round(48bits)
    res = ""
    mat = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
           55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    for i in mat:
        res += key[i - 1]
    return res


def expansion_box(p):
    # convert the right half of permuted text to 48 bits (initially it was 32 bits)
    res = ""
    mat = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    for i in mat:
        res += p[i - 1]
    return res


def whitener(p, k):
    # to perform xor operation
    res = ""
    for i in range(0, len(p)):
        res += str(int(p[i]) ^ int(k[i]))
    return res


def sbox(p):
    # All the eight sboxes
    res = ""
    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    sbox_num = 1
    for i in range(0, 48, 6):
        t = p[i:i + 6]
        row = int(t[0] + t[5], 2)
        col = int(t[1:5], 2)
        if sbox_num == 1:
            match = S1[row][col]
        elif sbox_num == 2:
            match = S2[row][col]
        elif sbox_num == 3:
            match = S3[row][col]
        elif sbox_num == 4:
            match = S4[row][col]
        elif sbox_num == 5:
            match = S5[row][col]
        elif sbox_num == 6:
            match = S6[row][col]
        elif sbox_num == 7:
            match = S7[row][col]
        else:
            match = S8[row][col]
        sbox_num += 1
        temp1 = bin(match).replace('0b', '')
        temp2 = '0' * (4 - len(temp1)) + temp1
        res += temp2
    return res


def perm_box(p):
    # straight permutation box
    res = ""
    mat = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
           11, 4, 25]
    for i in mat:
        res += p[i - 1]
    return res


def inverse_permutation(p):
    # final permutation box
    res = ""
    mat = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13,
           53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
    for i in mat:
        res += p[i - 1]
    return res


def algorithm_des(plain_text, org_key, enc):
    # Here if enc=1 encryption happens  and if enc=0 decryption happens

    bin_plain_text = conversion_text(plain_text, 1)  # converttobin
    bin_org_key = conversion_text(org_key, 1)  # converttobin
    ip_text = initialpermutaion(bin_plain_text)

    print("After Initial Permutation:", conversion_text(ip_text, 0))

    left_half_text = ip_text[0:32]  # dividing initially permuted textt into two halves
    right_half_text = ip_text[32:64]

    parity_key = parity_drop(bin_org_key)  # convert 64 bit to 56bit
    left_key = parity_key[0:28]
    right_key = parity_key[28:56]
    for rounds in range(1, 17):
        if enc == 1:
            shifted_left_key = shifting_operation_enc(left_key, rounds)  # leftshift
            shifted_right_key = shifting_operation_enc(right_key, rounds)  # rightshift
            left_key = shifted_left_key
            right_key = shifted_right_key
        else:
            shifted_left_key = shifting_operation_dec(left_key, rounds)  # leftshift
            shifted_right_key = shifting_operation_dec(right_key, rounds)  # rightshift

        round_key = key_generation(shifted_left_key + shifted_right_key)  # generate key of 48 bit length

        print("Round" + str(rounds) + " key :", conversion_text(round_key, 0))

        expanded_right_plain_text = expansion_box(
            right_half_text)  # convert right_half of plin text to 48 bits (original 32 bts)

        xor_result = whitener(expanded_right_plain_text, round_key)  # perform the xor

        mixer_result = sbox(xor_result)

        straight_perm_result = perm_box(mixer_result)

        temp = right_half_text

        right_half_text = whitener(straight_perm_result, left_half_text)

        left_half_text = temp
        if rounds == 16:
            temp2 = left_half_text
            left_half_text = right_half_text
            right_half_text = temp2
        print("After Round" + str(rounds) + " ", conversion_text(left_half_text, 0),
              conversion_text(right_half_text, 0))

    final_result = inverse_permutation(left_half_text + right_half_text)
    return conversion_text(final_result, 0)


plain_text = '123456ABCD132536'
org_key = 'AABB09182736CCDD'

print("Encryption Part :")
cipher_text = algorithm_des(plain_text, org_key, 1)
print("Cipher text: ", cipher_text)

print()

print("Decryption Part :")
plain_text = algorithm_des(cipher_text, org_key, 0)
print("Plain text:", plain_text)
