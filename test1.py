import pyodbc


con = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};\
        SERVER=LAPTOP-46CK9SKG; Database=Socket_Account;\
            UID=nguyenan123; PWD=123;')
print("ok")
