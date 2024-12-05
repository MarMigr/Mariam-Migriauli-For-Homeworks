from contextlib import contextmanager

@contextmanager
def db_connection():
    print("Connecting to the database...")
    try:
        yield
    finally:
        print("Disconecting from the database...")
with db_connection():
    print("Performing database operations...")
    pass