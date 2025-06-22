def sort_on(items):
    return items["num"]

def get_num_words(book_contents):
    book_words = book_contents.split()
    return len(book_words)

def count_characters(book_contents):
    character_dict = {}

    for c in book_contents:
        c = c.lower()

        if c not in character_dict:
            character_dict[c] = 0
        
        character_dict[c] += 1

    return character_dict

def sort_dictionary(character_dict):
    sorted_dict = []

    for key, value in character_dict.items():
        new_dict = { "char": key, "num": value }
        sorted_dict.append(new_dict)
    
    sorted_dict.sort(reverse=True, key=sort_on)
    
    return sorted_dict
