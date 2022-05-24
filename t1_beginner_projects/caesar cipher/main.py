import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_value, shift_value, direction_value):
    output_text = ""
    if direction_value == "decode":
        shift_value *= -1
    for i in text_value:
        if i in alphabet:
            index_of_text = alphabet.index(i)
            output_text += alphabet[shift_value + index_of_text]
        else:
            output_text += i
    print(f"The {direction_value}d text is {output_text}")


stop = False
while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift %= 26
    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if restart == "no":
        stop = True
        print("Goodbye.")
