#given a dic with nested dic and list flatten both

def flatten(data,parent_key='', sep='.'):
    result = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            result.update(flatten(value, new_key, sep))

    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_key = f"{parent_key}{sep}{i}"
            result.update(flatten(value, new_key, sep))

    else:
        result[parent_key] = data

    return result

data = {
    'a':1,
    'b':{'d':2, 'f':4},
    'c':3,
'l':[6,7,8],
}

print(flatten(data))