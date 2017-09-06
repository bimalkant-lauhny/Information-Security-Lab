print("This program implements Rotor Machine Cipher.")
print("Select option:")
print("1. Encrypt a message")
print("2. Decrypt a message")
print("Enter 1 or 2:")
option = int(input())

def encryption_function(key, val):
    if (val == ' '):
        return val
    return chr(((ord(val) - 97 + key) % 26) + 97)

def decryption_function(key, val):
    if (val == ' '):
        return val
    return chr(((ord(val) - 97 - key) % 26) + 97)

if (option == 1):
    print("Enter a message to encrypt (a-z only):")
    message = input()
    print("Enter 3 keys to encrypt (integer only):")
    keys = (input()).split(' ')
    keys = [int(i) for i in keys]
    print(keys)
    message = list(message)
    encrypted_message = []
    for i in range(0, len(message)):
        encrypted_message.append(encryption_function(keys[0], message[i]))
    message = ''.join(encrypted_message)
    message = list(message)
    encrypted_message = []
    for i in range(0, len(message)):
        encrypted_message.append(encryption_function(keys[1], message[i]))
    message = ''.join(encrypted_message)
    message = list(message)
    encrypted_message = []
    for i in range(0, len(message)):
        encrypted_message.append(encryption_function(keys[2], message[i]))
    encrypted_message = ''.join(encrypted_message)
    print("Encrypted Message: " + encrypted_message)

elif (option == 2):
    print("Enter a message to decrypt (a-z only):")
    encrypted_message = input()
    print("Enter 3 keys to decrypt (integer only):")
    keys = (input()).split(' ')
    keys = [int(i) for i in keys]
    encrypted_message = list(encrypted_message)
    message = []
    for i in range(0, len(encrypted_message)):
        message.append(decryption_function(keys[2], encrypted_message[i]))
    message = ''.join(message)
    encrypted_message = list(message)
    message = []
    for i in range(0, len(encrypted_message)):
        message.append(decryption_function(keys[1], encrypted_message[i]))
    message = ''.join(message)
    encrypted_message = list(message)
    message = []
    for i in range(0, len(encrypted_message)):
        message.append(decryption_function(keys[0], encrypted_message[i]))
    message = ''.join(message)
    print("Decrypted Message: " + message)

else:
    print("Invalid Option!")