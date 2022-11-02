encrypt = input(" Enter text to encrypt: \n")

encrypted_text = ''
for c in encrypt:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
    
print(encrypted_text)

print("\n")
