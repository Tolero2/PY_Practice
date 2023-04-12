

import json
from collections import _OrderedDictItemsView


table_name = ['employees.txt', 'salaries.txt',
    'dept_emp.txt', 'dept_manager.txt', 'titles.txt', 'departments.txt']
#insert order preference/ all table values defined in this Dict must exist in the list of file names from the directory in use.
insertOrder = {}
insertOrder[1] = "employees"
insertOrder[2] = "salaries"
insertOrder[3] = "dept_manager"
insertOrder[4] = "dept_emp"
insertOrder[5] = "departments"
insertOrder[6] = "titles"

# serialize tableName to hold table_name list in the insert order preference
tableName = {}

for table in table_name:
    for keyOrder in insertOrder:
        if (f"{insertOrder[keyOrder]}.txt" == table):
            tableName[keyOrder] = f"{insertOrder                     [keyOrder]}.txt"

print(tableName)
counter = 1
for i in range(1, len(insertOrder)+1, 1):
    print(tableName[counter])
    counter = counter + 1