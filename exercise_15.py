text = input('Tip a string: ')

def text_upsidedown(text):
    text = text.split()
    text2 = [word for word in text[::-1]]
    result = " ".join(text2)
    print(result)
    
text_upsidedown(text)