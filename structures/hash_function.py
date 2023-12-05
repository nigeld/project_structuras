def encrypt(text):
    hashed_text = ""
    for char in text:
        hashed_text += chr(ord(char) + 1)
    hashed_text += hashed_text[::-1].upper()
    
    return hashed_text
