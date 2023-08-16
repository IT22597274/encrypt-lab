#include <stdio.h>
#include <string.h>

void encrypt(char *text, int key) {
    for (int i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            int shift = key % 26;
            if (islower(text[i])) {
                text[i] = (((text[i] - 'a' + shift) % 26) + 'a');
            } else {
                text[i] = (((text[i] - 'A' + shift) % 26) + 'A');
            }
        }
    }
}

void decrypt(char *text, int key) {
    for (int i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            int shift = key % 26;
            if (islower(text[i])) {
                text[i] = (((text[i] - 'a' - shift + 26) % 26) + 'a');
            } else {
                text[i] = (((text[i] - 'A' - shift + 26) % 26) + 'A');
            }
        }
    }
}

int main() {
    char plaintext[] ="";
    int key =2;

    printf("Enter the plaintext: ");
    scanf("%s",plaintext);

    encrypt(plaintext, key);
    printf("Encrypted: %s\n", plaintext);

    decrypt(plaintext, key);
    printf("Decrypted: %s\n", plaintext);

    return 0;
}
