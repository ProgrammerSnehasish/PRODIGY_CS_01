# Python code for Ceasar Cipher.

def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "E" else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Keep spaces and special characters unchanged
            
    return result

if __name__ == "__main__":
    while True:
        print("________Encrypt and Decrypt your message by Ceasar Cipher________")
        message = input("\nEnter message: ")
        shift = int(input("Enter shift value: "))
        mode = input("Choose operation (E for Encrypt, D for Decrypt): ").strip().upper()

        if mode in ["E", "D"]:
            output = caesar_cipher(message, shift, mode)
            print(f"Result: {output}")
        else:
            print("Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.")

        # Ask the user if they want to continue
        choice = input("Do you want to run again? (Y/N): ").strip().upper()
        if choice != "Y":
            print("Exiting program...")
            break
