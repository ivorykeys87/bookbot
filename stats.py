def get_word_count(string):
    count = len(string.split())
    return count

def get_character_count(string):
    new_string = string.lower()
    each_count={}
    done = []
    for i in new_string:
        if i not in done:
            done.append(i)
            count = new_string.count(i)
            each_count[i] = count
    return each_count

