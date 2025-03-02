import os
from collections import Counter

def gather_strings(directory):
    strings = []

    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().split()
                    strings.extend(content)
            except Exception as e:
                print(f"Couldn't read {file_path}: {e}")
    
    return strings

def count_occurrences(strings):
    return {word: count for word, count in Counter(strings).items() if count > 2}

def display_counts(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_counts:
        print(f"{word}: {count}")

def main():
    directory = input("Enter the directory path to scan: ")
    strings = gather_strings(directory)
    word_counts = count_occurrences(strings)
    display_counts(word_counts)

if __name__ == '__main__':
    main()
