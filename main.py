alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?!' "
message_to_send = "Hello fictional cryptography " \
                  "enthusiast pen pal Vishal!"
translated_message = ""

for letter in message_to_send:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value - 10) % 26]
    else:
        translated_message += letter
print(translated_message)
