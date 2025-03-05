def get_word_count(string):
    count = len(string.split())
    return count

def get_character_count(string):
    new_string = string.lower()
    each_count={}
    done = []
    for i in new_string:
        if i not in done and i.isalpha():
            done.append(i)
            count = new_string.count(i)
            each_count[i] = count
    return each_count

def sort_on(dict):
    return dict["count"]

def convert_to_list(dictionary):
    new_list=[]
    for item in dictionary:
        new_dict = {"character":item, "count":dictionary[item]}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    