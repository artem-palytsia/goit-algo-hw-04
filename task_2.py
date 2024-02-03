def get_cats_info(path):
    try:
        with open('cats_info.txt', 'r', encoding='utf-8') as file:
            lines = file.read()
            cat_info_list = []
            for line in lines.split('\n'):
                line = line.split(',')
                cat_info_list.append({"id":line[0], "name":line[1], "age":line[2]})
        return cat_info_list
    except FileNotFoundError:
        print('File not found')

print(get_cats_info('cats_info.txt'))