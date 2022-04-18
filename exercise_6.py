from operator import truediv


def is_palindrome(sentence):
    sentence = sentence.replace(' ', '')
    sentence = sentence.upper()
    if sentence == sentence[::-1]:
        return True
    else:
        return False
    

def run():
    word = input('Enter a sentence: ')
    is_palindrome(word)
    if is_palindrome(word):
        print(f'{word} its palindrome')
    else:
        print(f'{word} its not palindrome')

if __name__ == '__main__':
    run()