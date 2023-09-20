def vigenere_encrypt(plain_text, keyword):

    
    # Convert plain text and keyword to uppercase
    plain_text = plain_text.upper()
    keyword = keyword.upper()
    
    # Make the keyword as long as the plain text by repeating it
    long_keyword = ''
    for i in range(len(plain_text)):
        long_keyword += keyword[i % len(keyword)]
    
    cipher_text = ''
    for p, k in zip(plain_text, long_keyword):
        # Only encrypt alphabetic characters
        if p.isalpha():
            c = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
            cipher_text += c
        else:
            cipher_text += p  # Keep non-alphabetic characters unchanged
    
    return cipher_text


def vigenere_decrypt(cipher_text, keyword):

    
    # Convert cipher text and keyword to uppercase
    cipher_text = cipher_text.upper()
    keyword = keyword.upper()
    
    # Make the keyword as long as the cipher text by repeating it
    long_keyword = ''
    for i in range(len(cipher_text)):
        long_keyword += keyword[i % len(keyword)]
    
    plain_text = ''
    for c, k in zip(cipher_text, long_keyword):
        # Only decrypt alphabetic characters
        if c.isalpha():
            p = chr(((ord(c) - ord(k) + 26) % 26) + ord('A'))
            plain_text += p
        else:
            plain_text += c  # Keep non-alphabetic characters unchanged
    
    return plain_text


if __name__ == "__main__":
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    if choice == 'e':
        plain_text = input("Enter the plain text: ")
        keyword = input("Enter the keyword: ")
        encrypted = vigenere_encrypt(plain_text, keyword)
        print(f"Encrypted Text: {encrypted}")
    elif choice == 'd':
        cipher_text = input("Enter the cipher text: ")
        keyword = input("Enter the keyword: ")
        decrypted = vigenere_decrypt(cipher_text, keyword)
        print(f"Decrypted Text: {decrypted}")
    else:
        print("Invalid choice!")