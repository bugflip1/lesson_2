famous_words = "seven years ago..."

new_words = "Four score and " + famous_words

word_filler = "{} " + famous_words

print(f'Four score and {famous_words}')
print(word_filler.format('Four score and'))
print(new_words)