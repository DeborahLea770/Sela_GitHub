# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    lst_ex1 = [3, 7, 2]
    lst1_ex1 = [item * '*' for item in lst_ex1]
    print(lst1_ex1)

    lst1_ex2 = ["a", "b", "c"]
    lst2_ex2 = ["x", "y", "z"]
    lst_res = []
    for i in range(len(lst1_ex2)):
        lst_res.append(str(lst1_ex2[i] + lst2_ex2[::-1][i]))
    print(lst_res)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
