import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):
    new_message = ""
    if direction == "decode":
        shift_amount *= -1

    for c in original_text:
        if c in alphabet:
            new_index = (alphabet.index(c) + shift_amount) % len(alphabet)
            new_message += alphabet[new_index]
        else:
            new_message += c
    print(f"Here's the {direction}d message: {new_message}")

active = True

while active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    caesar(direction, text, shift)

    wants_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if wants_continue != "yes":
        active = False
