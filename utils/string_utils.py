def slice_words(word_list: list[str], max_char_count: int) -> list[str]:
    """
    Goes over a list of words and slices each one to have fewer characters than max_char_count
    :param word_list: List of words from one row in csv file
    :param max_char_count: maximum characters for each word
    :return: a list of sliced strings
    """
    sliced_word_list = []
    for word in word_list:
        new_word = word[:max_char_count]
        sliced_word_list.append(new_word)
    return sliced_word_list

