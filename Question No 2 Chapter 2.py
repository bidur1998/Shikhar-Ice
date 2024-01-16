def separate_and_convert(s):
    # Separate into number and letter substrings
    number_string = ''.join([c for c in s if c.isdigit()])
    letter_string = ''.join([c for c in s if c.isalpha()])

    # Convert even numbers in the number substring to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values_numbers = [ord(chr(num)) for num in even_numbers]

    # Convert upper-case letters in the letter substring to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_values_letters = [ord(char) for char in upper_case_letters]

    return number_string, letter_string, ascii_values_numbers, ascii_values_letters


def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_text = ''

    for char in cryptogram:
        if char.isalpha():
            # Shift each alphabetical character based on the shift key
            decrypted_char = chr((ord(char) - shift_key - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


# Example Scenario 1
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
number_str, letter_str, ascii_numbers, ascii_letters = separate_and_convert(input_string)

print("Number String:", number_str)
print("Letter String:", letter_str)
print("Even Numbers:", ', '.join(map(str, [num for num in number_str if int(num) % 2 == 0])))
print("ASCII Values for Even Numbers:", ', '.join(map(str, ascii_numbers)))
print("ASCII Values for Upper-case Letters:", ', '.join(map(str, ascii_letters)))

# Example Scenario 2 (Decrypting Cryptogram)
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
for shift_key in range(1, 26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift_key)
    print(f"Shift Key = {shift_key}: {decrypted_text}")