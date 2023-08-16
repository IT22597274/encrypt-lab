need = str(input("What do you need (E-encrypt/D-decrypt): "))
key  = int(input("What is Your Key: "))

if (need == "E"):
    plain = str(input("What is Your Plain Text: "))
    encryptext = ""

    for char in plain:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encryptext += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else :
                encryptext += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encryptext += char
    print (encryptext)

elif (need == "D"):
    cihyper = str(input("What is Your cihyper Text: "))
    decrypyext = ""

    for char in cihyper:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypyext += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else :
                decrypyext += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypyext += char
    print (decrypyext)

else:
    printf("error")


