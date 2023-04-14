
##LOGIC 1

# table_name = ['employees.txt', 'salaries.txt',
#     'dept_emp.txt', 'dept_manager.txt', 'titles.txt', 'departments.txt']
# #insert order preference/ all table values defined in this Dict must exist in the list of file names from the directory in use.
# insertOrder = {}
# insertOrder[1] = "employees"
# insertOrder[2] = "dept_manager"
# insertOrder[3] = "departments"
# insertOrder[4] = "salaries"
# insertOrder[5] = "departments"
# insertOrder[6] = "titles"

# # serialize tableName to hold table_name list in the insert order preference
# tableName = {}

# for table in table_name:
#     for keyOrder in insertOrder:
#         if (f"{insertOrder[keyOrder]}.txt" == table):
#             tableName[keyOrder] = f"{insertOrder                     [keyOrder]}.txt"
# #return the list of table names in the insert order preference as a list variable
# counter = 1 # counter to help reorder the dict values using key matching()
# orderedTableName = []
# for i in range(1, len(insertOrder)+1, 1):
#     orderedTableName.append(tableName[counter])
#     counter = counter + 1
# print(orderedTableName)


##LOGIC 2
