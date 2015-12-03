rawText = 'alma\nrepa\n'
list_ = ['alma', 'repa']

def raw_text_to_list(text):
    list_ = text.split('\n')
    return [string for string in list_ if string != '']

def list_to_raw_text(list_):
    return "\n".join('1. ' + str(i) for i in list_)

print(raw_text_to_list(rawText))
print(repr(list_to_raw_text(list_)))
