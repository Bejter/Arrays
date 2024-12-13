# Function to return the number of words in the text
def count_words(text):
    words = text.split()  # Split the text into a list of words
    return len(words)

# Function to return words ordered from longest to shortest
def longest_to_shortest(text):
    words = text.split()  # Split the text into a list of words
    words.sort(key=len, reverse=True)  # Sort words by length (longest first)
    return words

# Function to return words ordered alphabetically
def alphabetically_ordered(text):
    words = text.split()  # Split the text into a list of words
    words.sort()  # Sort words alphabetically
    return words
