import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(name_file, separate=",") -> list[dict]:
    listadd = []
    with open(name_file) as f:
        for s in f:
            listadd.append(s.rstrip().split(separate))
        diction = [dict(zip(listadd[0], s)) for s in listadd[1:]]
    return diction


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
