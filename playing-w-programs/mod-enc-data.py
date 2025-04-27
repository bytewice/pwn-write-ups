#------------------------------------------------------------------
#          MODIFYING ENCODED DATA
#          CODE USED FOR THE CHALLENGE, HOPE IT CAN BE USEFUL :)
#------------------------------------------------------------------

def str_to_bits(s: str) -> str:
    return ''.join(f"{ord(c):08b}" for c in s)

def bits_to_str(bits: str) -> str:
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def str_to_hex(s: str) -> str:
    return ''.join(f"{ord(c):02X}" for c in s)

def hex_to_str(hex_str: str) -> str:
    chars = [chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)]
    return ''.join(chars)

def hex_to_bit(hex_str: str) -> str:
    temp_str = hex_to_str(hex_str)
    return str_to_bits(temp_str)

def bits_to_hex(bits: str) -> str:
    temp_str = bits_to_str(bits)
    return str_to_hex(temp_str)

def reverse_string(s):
    return s[::-1]

# Exemplo de uso
if __name__ == "__main__":

    latin1_str = b"\xdcr\x9dn\x14W\xab\xbe"
    correct_password = b"\xdcr\x9dn\x14W\xab\xbe"
    
    # Passo 1: codifica como string usando latin-1
    latin1_str = correct_password.decode("latin-1")
    
    # Passo 2: transforma cada caractere em seu valor hexadecimal
    hex_str = ''.join(f"{ord(c):02x}" for c in latin1_str)
    
    # Passo 3: inverte a string
    reversed_hex_str = hex_str[::-1]

    print(reversed_hex_str)
