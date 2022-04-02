def repeated(a, b):
    new_list = []
    for i in a:
        for x in b:
            if i == x:
                if i in new_list:
                    continue
                else:
                    new_list.append(i)           
    return new_list


def run():
    list_1 = [1, 2, 4, 6, 8, 10, 13, 15]
    list_2 = [2, 4, 6, 10, 10, 2, 14, 15]
    list_3 = repeated(list_1, list_2)
    print(list_3)

if __name__ == '__main__':
    run()