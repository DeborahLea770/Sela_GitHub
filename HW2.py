# 1
s = "vghdtydddvvghghgh"
d = {}
for item in s:
    d[item] = d.get(item, 0) + 1
print(f"dic={d}")
revers_key = {}
for items in sorted(d.keys()):
    if revers_key.get(d[items]) is None:
        revers_key[d[items]] = []
    revers_key[d[items]].append(items)
for keys in sorted(new_dic.keys()):
    print(keys, "-", new_dic[keys])
# 2
lst1 = [11, 7, 6,8]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]
dict_lists = {"lst1": lst1, "lst2": lst2, "lst3": lst3}
items = {}
numbers = ""
new_lst = []
list_none_dup = []
none_dup_lst = ""
for keys in dict_lists:
    for value in dict_lists[keys]:
        if dict_lists[keys].count(value) > 1 and str(value) not in numbers:
            numbers += str(value) + " and "
    items[keys] = (numbers[0:-5:1])
    numbers = ""
for keys in items.keys():
    if items[keys] != "":
        print(keys, "- includes the values " + items[keys], "more than once")
    else:
        none_dup_lst += keys + " and "
        list_none_dup += dict_lists[keys]

for end_number in list_none_dup:
    if list_none_dup.count(end_number) > 1 and end_number not in new_lst:
        new_lst.append(end_number)
if len(new_lst) == 0:
    print(None)
else:
    print("common values (of", none_dup_lst[0:-5:1] + ") are", new_lst)

# 3
lst5 = [31, 99, 3, 1943]
lst6 = []
for item in lst5:
    while item > 0:
        if item % 10 not in lst6:
            lst6.append(item % 10)
        item = int(item / 10)

sort_order = "asc"
if sort_order == "asc":
    lst6.sort()
    print(lst6)
sort_order = "desc"
if sort_order == "desc":
    lst6.reverse()
    print(lst6)
