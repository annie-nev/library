def slice_words(word_list: list[str], max_char_count: int):
    sliced_word_list = []
    for word in word_list:
        new_word = word[:max_char_count]
        sliced_word_list.append(new_word)
    return sliced_word_list

