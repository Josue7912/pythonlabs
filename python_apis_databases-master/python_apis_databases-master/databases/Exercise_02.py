'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

'''- Select all the actors with the first name of your choice'''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'DAN')
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

'''- Select all the actors and the films they have been in'''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

'''- Select all the actors that have appeared in a category of a comedy of your choice'''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id).join(film_category, film_category.columns.film_id == film.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).where(film_category.columns.category_id == 5).select_from(join_statement)
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

'''- Select all the comedic films and sort them by rental rate'''
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

join_statement = film.join(film_category, film_category.columns.film_id == film.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title, film.columns.rental_rate, film_category.columns.category_id]).where(film_category.columns.category_id == 5).order_by(sqlalchemy.desc(film.columns.rental_rate)).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

'''- Using one of the statements above, add a GROUP BY statement of your choice'''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id).join(film_category, film_category.columns.film_id == film.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).group_by(film_category.columns.category_id).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

'''- Using one of the statements above, add a ORDER BY statement of your choice'''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id).join(film_category, film_category.columns.film_id == film.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title, film.columns.length, actor.columns.first_name, actor.columns.last_name]).order_by(sqlalchemy.desc(film.columns.length)).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)