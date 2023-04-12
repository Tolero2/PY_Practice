table_name = ['employees.txt', 'url_dumpReader.py', 'salaries2.txt', 'salaries3.txt', 'salaries1.txt',
    'dept_emp.txt', '.ipynb_checkpoints', 'dept_manager.txt', 'objects.sql.txt', 'titles.txt', 'departments.txt']

insertOrder = ["employees", "departments",
    "dept_manager", "salaries", "dept_emp", "titles"]

       # relist table_name properly


for i in range (0, len(table_name) + 1, 1) :
    tableName = [] *len(table_name)
    counter = 0
    # for inOrder in insertOrder:
    print(table_name[counter])
    for i in table_name:
        if (f"{insertOrder[counter]}.txt" == i):
                print( insertOrder[counter])
                tableName.append(insertOrder[counter])
                                    
        counter += 1

print(tableName)
