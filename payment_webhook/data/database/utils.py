from sqlalchemy.engine.base import Connection


def autocommit_check(func):
    def wrapper(self, *args, **kwargs):
        if not self.autocommit:
            return func(self, *args, **kwargs)
        eval(f'self.session.{func.__name__}(*args, **kwargs)')
        self.commit()

    return wrapper


def validate_conn(func):
    def wrapper(conn: Connection, *args, **kwargs):
        if not conn.connection.is_valid:
            raise ConnectionError('Connection is not valid')
        return func(conn, *args, **kwargs)

    return wrapper
