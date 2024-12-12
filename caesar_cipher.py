def caesar_cipher(text,shift,mode):
    if mode.lower() == 'decrypt':
        shift = -shift
    
    result = []
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')
            j = chr((ord(i) - start + shift) % 26 + start)
            result.append(j)
        else:
            result.append(i)
        
    return ''.join(result)

def main():
    print("Welcome to the Caesar Cipher Program !")
    while True:
        mode = input("Enter 'encrypt' or 'decrypt' or 'exit' :   ").strip().lower()
        if mode == 'exit':
            print("Thank You!")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid Choice.Please choose 'encrypt' or 'decrypt' ")
            continue

        text = input("Enter your message:         ").strip()
        try:
            shift = int(input("Enter the shift value(integer):").strip())
        except ValueError:
            print("shift value must be an integer.Please enter again")
            continue

        result = caesar_cipher(text,shift, mode)
        print(f"The {mode}ed message is: {result}\n")

if __name__ == "__main__":
    main()