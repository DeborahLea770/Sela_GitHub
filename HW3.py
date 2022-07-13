def split_male_female(data_set_f):
    data_set_male = {}
    data_set_female = {}
    for item in data_set_f.keys():
        if data_set_f[item]["sex"] == "male":
            data_set_male[item] = data_set_f[item]
        else:
            data_set_female[item] = data_set_f[item]
    return data_set_male, data_set_female


def find_median_average(data_set_f):
    sum1 = 0
    avg = 0
    median = 0
    age = []
    for item in data_set_f.values():
        sum1 += item["age"]
        age.append(item["age"])
    age.sort()
    avg = sum1 / len(data_set_f)
    if len(data_set_f) % 2 == 1:
        median = age[int((len(data_set_f) / 2))]
    else:
        median = age[int(len(data_set_f) / 2) - 1] + age[int(len(data_set_f) / 2)]
        median = median / 2
    avg = round(avg, 2)
    return avg, median


def print_value_above(data_set_f, num=-1):
    for key, value in data_set_f.items():
        if value["age"] > num:
            print(key, value)

def main():
    data_set_male2 = {}
    data_set_female2 = {}
    avg1 = 0
    median1 = 0

    data_set = {
        324271256: {"name": "tal", "age": 0, "sex": "female"},
        206910424: {"name": "dan", "age": 21, "sex": "male"},
        206910425: {"name": "levy", "age": 21, "sex": "male"},
        206910426: {"name": "lea", "age": 23, "sex": "female"},
        206910427: {"name": "shire", "age": 26, "sex": "female"},
        206910428: {"name": "debora", "age": 64, "sex": "female"},
        206910429: {"name": "shire", "age": 13, "sex": "female"}
    }


   data_set_male2, data_set_female2 = split_male_female(data_set)
   avg1, median1 = find_median_average(data_set)
   print_value_above(data_set, 18)

if __name__ == '__main__':
    main()
