def count_words_in_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)