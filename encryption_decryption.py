def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypt_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypt_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypt_char = char
        encrypted_text += encrypt_char
    return encrypted_text

# Example usage
text = "Alex"
shift = 9

enc_text = encrypt_text(text, shift)
print("Encrypted:", enc_text)

dec_text = encrypt_text(enc_text, -shift)
print("Decrypted:", dec_text)
