import re

def main():
    file_path = "words.txt"
    # Finds words using the \w and hyphen one or more times followed by space or punctuation.
    rule = re.compile(r"([-\w]+)([ .,])", re.VERBOSE)
    
    # Load sentence from file
    sentence = load_sentence_from_file("words.txt")
    matches = rule.findall(sentence)
    
    # Extracting words only from the matches
    words = [match[0] for match in matches]
    print(words)

def load_sentence_from_file(file_path):
    sentences = []
    with open(file_path, 'r') as file_reader:
        for line in file_reader:
            cleaned_line = line.strip()
            if cleaned_line != '':
                sentences.append(cleaned_line)
    
    # Combine all lines into a single string
    sentence = ' '.join(sentences)
    return sentence

if __name__ == "__main__":
    main()










