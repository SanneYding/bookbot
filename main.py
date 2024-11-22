def main():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        print("--- Begin report of frankenstein ---")
        num_word= count_words(file_contents)
        print(num_word, "words found in the document")
        letters = count_characters(file_contents)
        print("There are ", letters)

def count_words(text):
      words = text.split()
      return len(words)

def sort_on(dict):
     return dict["num"]

def count_characters(text):
    lowered_text = text.lower()
    num_letters = dict()
    for character in lowered_text:
        if character in num_letters:
            num_letters[character] += 1
        else:
            num_letters[character]=1
    new_list = list()
    for char in num_letters:
         if char.isalpha():
            char_dict = {"char": char, "num": num_letters[char]}
            new_list.append(char_dict)
    new_list.sort(reverse=True, key=sort_on)
    for entry in new_list:
         print(f"The '{entry['char']}' character was found {entry['num']} times")
    


      



main()