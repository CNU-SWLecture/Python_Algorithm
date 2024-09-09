def dec_to_bin(dec):
    if dec == 0:
        return '0'
    elif dec == 1:
        return '1'
    else:
        return dec_to_bin(dec // 2) + str(dec % 2)
    
def dec_to_oct(dec):
    if dec == 0:
        return '0'
    else:
        return dec_to_oct(dec // 8) + str(dec % 8)

def dec_to_hex(dec):
    hex_digs = '0123456789ABCDEF'
    if dec < 16:
        return hex_digs[dec]
    else:
        return dec_to_hex(dec // 16) + hex_digs[dec % 16]

dec_input = int(input("10진수 입력 --> "))

bin_result = dec_to_bin(dec_input)
oct_result = dec_to_oct(dec_input)
hex_result = dec_to_hex(dec_input)

print('2진수 : ', bin_result)
print('8진수 : ', oct_result)
print('16진수 : ', hex_result)