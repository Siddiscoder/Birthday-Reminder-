decrypt = input(" Enter text to decrypt: \n")

plain_text = ''
for c in decrypt:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2

print(plain_text)
