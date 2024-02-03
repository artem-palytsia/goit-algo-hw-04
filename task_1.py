def total_salary(path):
    try:
        with open('salary_file.txt', 'r', encoding='utf-8') as fh:
            list = fh.read()
            salary_list = []      
            for line in list.split('\n'):
                line = line.split(',')
                salary_list.append(int(line[1]))

            total_salary = 0
            for el in salary_list:
                total_salary += el
            average_salary = int(total_salary/len(salary_list))
        return f'Total salary is {total_salary}. Average salary is {average_salary}'
    except FileNotFoundError:
        print('File not found')
print(total_salary('salary_file.txt'))


