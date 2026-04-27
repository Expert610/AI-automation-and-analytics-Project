# 2. Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"] (Marks 3)
# Create a dictionary that maps each word to its corresponding length.
# Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5})

words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_lenght = {word: len(word) for word in words }

print(word_lenght)