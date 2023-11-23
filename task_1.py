import json


# TODO решите задачу
def task() -> float:
    with open('input.json') as f:
        data = json.load(f)

        return round(sum(dict_["score"] * dict_["weight"] for dict_ in data), 3)


print(task())
