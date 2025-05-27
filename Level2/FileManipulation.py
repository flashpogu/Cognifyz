"""Write a Python program that reads a text
file and counts the occurrences of each
word in the file. Display the results in
alphabetical order along with their
respective counts."""

def count_words_in_file(file_path):
    word_count = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().strip('.,!?";:()[]{}')  # Normalize the word
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return {}

    return dict(sorted(word_count.items()))

def display_word_counts(word_count):
    if not word_count:
        print("No words found.")
        return
    
    print("Word counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
        
def main():
    file_path = input("Enter the path to the text file: ")
    word_count = count_words_in_file(file_path)
    display_word_counts(word_count)

if __name__ == "__main__":
    main()

