import MyText  # Import the MyText module

# Sample text
text = "An apple a day keeps the doctor away"

# Call functions from MyText and print results
print(f"Text: {text}")
print(f"Number of words: {MyText.count_words(text)}")

print("Words from the longest to shortest:", ", ".join(MyText.longest_to_shortest(text)))
print("Words ordered alphabetically:", ", ".join(MyText.alphabetically_ordered(text)))