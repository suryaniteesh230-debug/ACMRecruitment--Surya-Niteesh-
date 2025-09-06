def word_frequency(filename):
    with open(filename, "r") as file:
        text = file.read()
    # Convert text to lowercase and split into words
    words = text.lower().split()
    # Count frequencies
    freq = {}
    for word in words:
        # remove punctuation around the word
        word = word.strip(".,!?;:\"'()[]{}")
        if word:
            freq[word] = freq.get(word, 0) + 1
    # BONUS: Sort by frequency (highest first), then alphabetically
    sorted_freq = dict(sorted(freq.items(), key=lambda x: (-x[1], x[0])))
    return sorted_freq
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    # Count frequencies
    frequencies = word_frequency(input_file)
    # Write results to output file
    with open(output_file, "w") as f:
        for word, count in frequencies.items():
            f.write(f"{word} → {count}\n")
    # Also print to terminal
    for word, count in frequencies.items():
        print(f"{word} → {count}")
