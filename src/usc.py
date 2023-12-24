class UniShiftCipher:
    def __init__(self):
        pass
    def encrypt(self, text):
        while True:
            try:
                shift = int(input("Enter the shift value (1-26): "))
                if 1 <= shift <= 26:
                    break #break if the input is valid shift equal or higher than 1 and less or equal to 26
                else:
                    print("Bad input. Shift must be in between 1 and 26.")
            except ValueError:
                print("Invalid input. Enter a valid integer.")

        encrypted_message = ""

        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - start + shift) % 26 + start)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        
        return encrypted_message

#------------------------------------------------------------------------|
#encryption_test_case                                                    |
#if __name__ == "__main__":                                              |
#    cipher = UniShiftCipher()                                           |
#    text_to_encrypt = input("Enter the text to encrypt: ")              |
#    encrypted_text = cipher.encrypt(text_to_encrypt)                    |
#    print(f"Encrypted text: {encrypted_text}")                          |
#------------------------------------------------------------------------|

    def decrypt(self, text, shift):
        pass