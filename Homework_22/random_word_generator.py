# написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
# Слова мають бути унікальні. Max int = 10_000.

###pip install random-word

from random_word import RandomWords

def random_word_generator(quantity=1):
    if type(quantity) != int or quantity < 1:
        return 'Quantity should be integer greater than 0'
    words = []
    while quantity > 0:
        word = RandomWords().get_random_word()
        if word not in words:
            yield word
            words.append(word)
            quantity -= 1