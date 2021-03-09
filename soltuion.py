def filter_list(l):
    filteredL = []
    for element in l:
        if isinstance(element, int):
            filteredL.append(element)
    return filteredL
