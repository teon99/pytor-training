
def count_word(word, c):
    count = 0
    for char in word:
        if char == c:
            count += 1
    return count