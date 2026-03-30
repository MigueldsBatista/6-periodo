
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet_map = {
    letter: index for index, letter in enumerate(alphabet)
}

def shift_letter(text: str, offset: int):
    result = ''
    for letter in text:
        if letter == ' ':
            result += ' '
            continue
        
        current_index = alphabet_map.get(letter)
        new_index = current_index - offset
        
        normalized = new_index % len(alphabet)
        result += alphabet[normalized]
    
    return result


text = "Hzn oerir erivfnb fboer pevcgbtensvn".upper()

for i in range(len(alphabet)):
    result = shift_letter(text, i)
    print(f"Shift {i}: ", result)
    
# Shift 13: UMA BREVE REVISAO SOBRE CRIPTOGRAFIA