class UniShiftCipher:
    def __init__(self):
        pass

    def encrypt(self, text, shift, rotation=0, output=None, output_format=None):

        if not isinstance(shift, int):
            raise ValueError('Invalid input. Enter a valid integer')
        if 1 < shift > 26:
            raise Exception('Bad input. Shift must be in between 1 and 26')

        encrypted_text = ""

        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - start + shift) % 26 + start)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char

        return encrypted_text

    # ------------------------------------------------------------------------|
    # encryption_test_case                                                    |
    # if __name__ == "__main__":                                              |
    #    cipher = UniShiftCipher()                                            |
    #    text_to_encrypt = input("Enter the text to encrypt: ")               |
    #    encrypted_text = cipher.encrypt(text_to_encrypt)                     |
    #    print(f"Encrypted text: {encrypted_text}")                           |
    # ------------------------------------------------------------------------|

    def decrypt(self, text, shift, rotation=0, output=None, output_format=None):
        if not isinstance(shift, int):
            raise ValueError("Invalid Input, please enter a valid integer value")
        if not 1 <= shift <= 26:
            raise ValueError("Bad input, the shift has only 26 possibilities (1-26)")
        
        decrypt_text = ""

        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord ('A')
                decrypt_char = chr((ord(char) - start - shift) % 26 + start)
                decrypt_text += decrypt_char
            else:
                decrypt_text += char
        return decrypt_text