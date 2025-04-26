#---------------------------------------------------------
#     TRANSLATOR USADO NO CHALLENGE HEX-ENCODING UTF-8
#---------------------------------------------------------

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

# Exemplo de uso
if __name__ == "__main__":

    original = "🏊 📐 😽 🆓" .encode("utf-8")
    original = original.decode("l1")
    original = str_to_hex(original)
    original = original.encode("utf-8")
    print(original)
