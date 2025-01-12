def main(text):
    with open(f"books/{text}.txt") as f:
        file_contents = f.read()
    
    # print(file_contents)
    return file_contents

def count_words(words):

    res = len(words.split())
    print(res)
    return res

def count_char(words):
    dictionary = {}
    base = str(words).lower()
    text = list(base)

    for char in text:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    
    print(dictionary)
    return dictionary

def print_report(count, dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")

    for k, v in dictionary.items():
        print(f'''The "{k}" character was found {v} times''')
    print("--- End report ---")

# main("frankenstein")
count_words(main("frankenstein"))
count_char(main("frankenstein"))
print_report(count_words(main("frankenstein")), count_char(main("frankenstein")))