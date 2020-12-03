from peewee import *

db = PostgresqlDatabase('contactlist', user='postgres', password='',
                        host='localhost', port=5000)