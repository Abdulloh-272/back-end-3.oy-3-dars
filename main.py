def get_min_max(*args):
    min_value = min(args)
    max_value = max(args)
    return f"min={min_value}, max={max_value}"

result = get_min_max(2, 5, 7, 3, 4, 5)
print(result)

def get_one_str(*args):
    return ' '.join(args)

result = get_one_str("My", "name", "is", "Alex")
print(result)

def get_lengths(*args):
    return [len(word) for word in args]

result = get_lengths('apple', 'banana', 'cherry')
print(result)


def print_key_value_pairs(**kwargs):
    for key, value in kwargs.items():
        print(f"'{key}': {value}")

print_key_value_pairs(name='Ali', age=25)
