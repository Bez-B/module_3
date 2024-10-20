data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    s=0
    for i in args:
        if isinstance(i, int):
            s += i
        elif isinstance(i, str):
            s += len(i)
        elif isinstance(i, list):
            s += calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            s += calculate_structure_sum(*i)
        elif isinstance(i, set):
            s += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for keys, value in i.items():
                s += calculate_structure_sum(keys) + calculate_structure_sum(value)
    return s

result = calculate_structure_sum(data_structure)
print(result)
