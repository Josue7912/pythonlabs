'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''
import sqlalchemy
import pprint

mytables = None
while mytables not in ("1","2","3"):

    mytables = input(f''' MYSQL TABLES
     1) Create Cars, Animals & Films tables
     2) Create Cars & Animals tables
     3) Create Cars table
    Choose which option you'd like to execute from the following options: ''')

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

'''OPTIONS SELECTED FROM MENU'''

if mytables == "1":
    Cars = sqlalchemy.Table('cars', metadata,
                            sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                            sqlalchemy.Column('model', sqlalchemy.String(255), nullable=False),
                            sqlalchemy.Column('year', sqlalchemy.Float(), default=1900.0),
                            sqlalchemy.Column('speed', sqlalchemy.Float())
              )
    Animals = sqlalchemy.Table('animals', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                       sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('country', sqlalchemy.String(255), nullable=False),
              )
    Films = sqlalchemy.Table('films', metadata,
                               sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                               sqlalchemy.Column('title', sqlalchemy.String(255), nullable=False),
                               sqlalchemy.Column('year', sqlalchemy.Float(), default=1900.0),
               )

    metadata.create_all(engine)

    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)

    car_model = input(f"Input model of the car: ")
    car_year = float(input(f"Input year of the car: "))
    car_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.insert(Cars).values(model=car_model, year=car_year, speed=car_speed)
    result_proxy = connection.execute(query)

    Animals = sqlalchemy.Table('animals', metadata, autoload=True, autoload_with=engine)

    animal_name = input(f"Input name of the animal: ")
    animal_country = input(f"Input country of the animal: ")

    query = sqlalchemy.insert(Animals).values(name=animal_name, country=animal_country)
    result_proxy = connection.execute(query)

    Films = sqlalchemy.Table('films', metadata, autoload=True, autoload_with=engine)

    film_name = input(f"Input name of the film: ")
    film_year = input(f"Input year of the film: ")

    query = sqlalchemy.insert(Films).values(title=film_name, year=film_year)
    result_proxy = connection.execute(query)

elif mytables == "2":
    Cars = sqlalchemy.Table('cars', metadata,
                            sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                            sqlalchemy.Column('model', sqlalchemy.String(255), nullable=False),
                            sqlalchemy.Column('year', sqlalchemy.Float(), default=1900.0),
                            sqlalchemy.Column('speed', sqlalchemy.Float())
              )
    Animals = sqlalchemy.Table('animals', metadata,
                       sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                       sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                       sqlalchemy.Column('country', sqlalchemy.String(255), nullable=False),
              )

    metadata.create_all(engine)

    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)

    car_model = input(f"Input model of the car: ")
    car_year = float(input(f"Input year of the car: "))
    car_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.insert(Cars).values(model=car_model, year=car_year, speed=car_speed)
    result_proxy = connection.execute(query)

    Animals = sqlalchemy.Table('animals', metadata, autoload=True, autoload_with=engine)

    animal_name = input(f"Input name of the animal: ")
    animal_country = input(f"Input country of the animal: ")

    query = sqlalchemy.insert(Animals).values(name=animal_name, country=animal_country)
    result_proxy = connection.execute(query)

elif mytables == "3":
    Cars = sqlalchemy.Table('cars', metadata,
                   sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                   sqlalchemy.Column('model', sqlalchemy.String(255), nullable=False),
                   sqlalchemy.Column('year', sqlalchemy.Float(), default=1900.0),
                   sqlalchemy.Column('speed', sqlalchemy.Float())
          )
    metadata.create_all(engine)

    '''ADD DATA TO THE TABLES'''
    Cars = sqlalchemy.Table('Cars', metadata, autoload=True, autoload_with=engine)

    car_model = input(f"Input model of the car: ")
    car_year = float(input(f"Input year of the car: "))
    car_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.insert(Cars).values(model=car_model, year=car_year, speed=car_speed)
    result_proxy = connection.execute(query)


# UPDATE DATA ON TABLES
updatetables = input(f''' UPDATE MYSQL TABLES
 1) Update Cars, Animals & Films tables
 2) Update Cars & Animals tables
 3) Update Cars table
Choose which option you'd like to execute from the following options: ''')

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

if updatetables == "1":

    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)

    newcar_year = float(input(f"Input year of the car: "))
    newcar_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.update(Cars).values(year=newcar_year, speed=newcar_speed).where(Cars.columns.year < 2000)
    result_proxy = connection.execute(query)

    Animals = sqlalchemy.Table('animals', metadata, autoload=True, autoload_with=engine)

    newanimal_country = input(f"Input country of the animal: ")

    query = sqlalchemy.insert(Animals).values(country=newanimal_country).where(Animals.columns.Id == 1)
    result_proxy = connection.execute(query)

    Films = sqlalchemy.Table('films', metadata, autoload=True, autoload_with=engine)

    newfilm_year = input(f"Input year of the film: ")

    query = sqlalchemy.insert(Films).values(year=newfilm_year).where(Films.columns.year < 2020)
    result_proxy = connection.execute(query)

elif updatetables == "2":
    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)

    newcar_year = float(input(f"Input year of the car: "))
    newcar_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.update(Cars).values(year=newcar_year, speed=newcar_speed).where(Cars.columns.year < 2000)
    result_proxy = connection.execute(query)

    Animals = sqlalchemy.Table('animals', metadata, autoload=True, autoload_with=engine)

    newanimal_country = input(f"Input country of the animal: ")

    query = sqlalchemy.insert(Animals).values(country=newanimal_country).where(Animals.columns.Id == 1)
    result_proxy = connection.execute(query)


elif updatetables == "3":
    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)

    newcar_year = float(input(f"Input year of the car: "))
    newcar_speed = float(input(f"Input maximum speed of the car: "))

    query = sqlalchemy.update(Cars).values(year=newcar_year, speed=newcar_speed).where(Cars.columns.year < 2000)
    result_proxy = connection.execute(query)

# SELECT DATA ON TABLES
selecttables = input(f''' UPDATE MYSQL TABLES
 1) Select Cars table
 2) Select Animals table
 3) Select Cars table
Choose which option you'd like to execute from the following options: ''')

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

if selecttables == "1":
    model = sqlalchemy.Table('model', metadata, autoload=True, autoload_with=engine)

    query = sqlalchemy.select([model])
    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()
    pprint(result_set)


elif selecttables == "2":
    name = sqlalchemy.Table('name', metadata, autoload=True, autoload_with=engine)

    query = sqlalchemy.select([name])
    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()
    pprint(result_set)

elif selecttables == "3":
    title = sqlalchemy.Table('title', metadata, autoload=True, autoload_with=engine)

    query = sqlalchemy.select([title])
    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()
    pprint(result_set)


# DELETE DATA ON TABLES

updatetables = input(f''' UPDATE MYSQL TABLES
 1) Delete Data from Cars table
 2) Select Data from Animals table
 3) Select Data from Cars table
Choose which option you'd like to execute from the following options: ''')

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

if updatetables == "1":

    Cars = sqlalchemy.Table('cars', metadata, autoload=True, autoload_with=engine)
    query = sqlalchemy.delete(Cars).where(Cars.columns.year < 2000)
    result_proxy = connection.execute(query)

elif updatetables == "2":

    Animals = sqlalchemy.Table('animals', metadata, autoload=True, autoload_with=engine)
    query = sqlalchemy.delete(Animals).where(Animals.columns.country != "Spain")
    result_proxy = connection.execute(query)

elif updatetables == "3":

    Films = sqlalchemy.Table('films', metadata, autoload=True, autoload_with=engine)
    query = sqlalchemy.delete(Films).where(Films.columns.year < 2010)
    result_proxy = connection.execute(query)
