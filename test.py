import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)


def percent_tweet_punctuation(tweets):
    charcount = 0
    punctcount = 0
    symbols = (".", ",", "/", "'", "!", "¡", "?", "¿", ")", "(", "[", "]", "+", "-", "*", ":", ";", "_")
    lentweet = []
    for t in tweets:
        characcount = 0
        text = t.text
        for word in text:
            for char in word:
                charcount += 1
                characcount += 1
                if char in symbols:
                    punctcount += 1
        lentweet.append(characcount)
    mean = np.mean(lentweet)
    div = punctcount / charcount
    percentage = div * 100
    return percentage, mean

print(percent_tweet_punctuation(tweets))


