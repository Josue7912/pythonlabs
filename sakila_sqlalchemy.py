import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#newTable = sqlalchemy.Table('newTable', metadata,
                       #sqlalchemy.Column('Id', sqlalchemy.Integer()),
                       #sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                       #sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
                       #sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
#              )

#metadata.create_all(engine)
'''INSERT STATEMENT - Adding new information to newly created table:'''

#newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

#query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=60000.00, active=True)
#result_proxy = connection.execute(query)

''' ADDING NEW RECORDS IN BULK TO THE TABLE'''
#newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)
#query = sqlalchemy.insert(newTable)
#new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
               #{'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
#result_proxy = connection.execute(query,new_records)

''' UPDATE STATEMENT - UPDATING RECORDS IN TABLE'''
#newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)
#query = sqlalchemy.update(newTable).values(salary=100000).where(newTable.columns.Id == 1)
#result = connection.execute(query)

''' DELETE STATEMENT - DELETING RECORDS IN TABLE'''
#newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)
#query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 100000)
#results = connection.execute(query)