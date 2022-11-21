def strip_punctuation_ru(data):
    blok = [',', '.', ';', ':', '(', ')', '{', '}', '!', '?']
    now_strok = ''
    data = data.replace(' - ', ' ')
    for count, elem in enumerate(data):
        if elem not in blok:
            now_strok += elem
        elif elem in blok and len(data) > 1 and data[count + 1] != ' ':
            now_strok += ' '
    return now_strok.strip()
