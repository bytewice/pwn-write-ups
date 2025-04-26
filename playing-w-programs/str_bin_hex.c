#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Converte string de caracteres para string de bits
char* str_to_bits(const char* str) {
    size_t len = strlen(str);
    char* bits = malloc(len * 8 + 1); // 8 bits por caractere + \0
    bits[0] = '\0';

    for (size_t i = 0; i < len; i++) {
        for (int j = 7; j >= 0; j--) {
            strcat(bits, ((str[i] >> j) & 1) ? "1" : "0");
        }
    }

    return bits;
}

// Converte string de bits para string de caracteres
char* bits_to_str(const char* bits) {
    size_t len = strlen(bits) / 8;
    char* str = malloc(len + 1);

    for (size_t i = 0; i < len; i++) {
        char byte = 0;
        for (int j = 0; j < 8; j++) {
            byte <<= 1;
            byte |= (bits[i * 8 + j] == '1') ? 1 : 0;
        }
        str[i] = byte;
    }
    str[len] = '\0';

    return str;
}

// Converte string de caracteres para hexadecimal (sem espaços)
char* str_to_hex(const char* str) {
    size_t len = strlen(str);
    char* hex = malloc(len * 2 + 1); // 2 dígitos por caractere + \0
    hex[0] = '\0';

    for (size_t i = 0; i < len; i++) {
        sprintf(hex + i * 2, "%02X", (unsigned char)str[i]);
    }

    return hex;
}

// Converte string hexadecimal para string de caracteres
char* hex_to_str(const char* hex) {
    size_t len = strlen(hex) / 2;
    char* str = malloc(len + 1);

    for (size_t i = 0; i < len; i++) {
        sscanf(hex + i * 2, "%2hhX", &str[i]);
    }
    str[len] = '\0';

    return str;
}

char* hex_to_bit(const char* hex) {
    char* temp_str = hex_to_str(hex);       // Hex -> texto original
    char* bits = str_to_bits(temp_str);     // Texto -> bits
    free(temp_str);                         // Liberar o intermediário
    return bits;
}

char* bits_to_hex(const char* bits) {
    char* temp_str = bits_to_str(bits);     // Bits -> texto original
    char* hex = str_to_hex(temp_str);       // Texto -> hex
    free(temp_str);                         // Liberar o intermediário
    return hex;
}


// Exemplo de uso
int main() {
    
    char* sample = "crxtrkwn";
    sample = str_to_hex(sample);
    printf("From Bits: %s\n", sample);
    
    //liberar o ponteiro
    free(sample);

    return 0;
}
