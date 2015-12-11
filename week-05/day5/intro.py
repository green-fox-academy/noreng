def get_names(array):
    return list(map(lambda x: x['name'] , array))

def filter_names(list_):
    return list(filter(lambda name: name.startswith('J'), get_names(list_)))

def filter_names_list_compreh(list_):
    return [person['name'] for person in list_ if person['name'][0] == 'J']
