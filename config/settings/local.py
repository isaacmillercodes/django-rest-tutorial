from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='5yn9v7u82v*yb-s2+1p07t4fqhnnq3@!z=4##a$9#n7t(q&eto')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
