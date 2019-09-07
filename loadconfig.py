import os


class Config:
    def __init__(self):
        # default db settings
        self.db_config = dict(
                  host='localhost',
                  user='root',
                  port=3306,
                  password='password',
                  db='mypolls'
                )

        # default redis settings
        self.cache_config = dict(
                 host='127.0.0.1',
                 port=6379,
                 password='password'
        )

        # load db settings from environment variables if set
        if os.environ.get('RELATIONAL_DATABASE_HOST') is not None:
            self.db_config['host'] = os.environ.get('RELATIONAL_DATABASE_HOST')

        if os.environ.get('RELATIONAL_DATABASE_DB_USER') is not None:
            self.db_config['user'] = os.environ.get('RELATIONAL_DATABASE_DB_USER')

        if os.environ.get('RELATIONAL_DATABASE_PORT') is not None:
            self.db_config['port'] = int(os.environ.get('RELATIONAL_DATABASE_PORT'))

        if os.environ.get('RELATIONAL_DATABASE_PASSWORD') is not None:
            self.db_config['password'] = os.environ.get('RELATIONAL_DATABASE_PASSWORD')

        if os.environ.get('RELATIONAL_DATABASE_DB_NAME') is not None:
            self.db_config['db'] = os.environ.get('RELATIONAL_DATABASE_DB_NAME')

        # print(self.db_config)

        # load redis settings from environment variables if set
        if os.environ.get('DISTRIBUTED_CACHE_HOST') is not None:
            self.cache_config['host'] = os.environ.get('DISTRIBUTED_CACHE_HOST')

        if os.environ.get('DISTRIBUTED_CACHE_PORT') is not None:
            self.cache_config['port'] = os.environ.get('DISTRIBUTED_CACHE_PORT')

        if os.environ.get('DISTRIBUTED_CACHE_PASSWORD') is not None:
            self.cache_config['password'] = os.environ.get('DISTRIBUTED_CACHE_PASSWORD')

        # print(self.cache_config)

    def get_db_config(self):
        return self.db_config

    def get_cache_config(self):
        return self.cache_config
