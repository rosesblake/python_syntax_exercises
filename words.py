#step two

def print_upper_words(list, must_start_with):
    """capitalize each word in the list that starts with E and print"""
    res = []
    for word in list:
        for start_letter in must_start_with:
            if word[0].capitalize() == start_letter.capitalize():
                res.append(word.upper())
    return res

