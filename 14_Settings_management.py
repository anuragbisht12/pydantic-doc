from typing import Set

from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    Field,
)


class SubModel(BaseModel):
    foo = 'bar'
    apple = 1


class Settings(BaseSettings):
    auth_key: str
    api_key: str = Field(..., env='my_api_key')

    redis_dsn: RedisDsn = 'redis://user:pass@localhost:6379/1'
    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'

    special_function: PyObject = 'math.cos'

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: Set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    class Config:
        env_prefix = 'my_prefix_'  # defaults to no prefix, i.e. ""
        fields = {
            'auth_key': {
                'env': 'my_auth_key',
            },
            'redis_dsn': {
                'env': ['service_redis_dsn', 'redis_url']
            }
        }


print(Settings().dict())
"""
{
    'auth_key': 'xxx',
    'api_key': 'xxx',
    'redis_dsn': RedisDsn('redis://user:pass@localhost:6379/1',
scheme='redis', user='user', password='pass', host='localhost',
host_type='int_domain', port='6379', path='/1'),
    'pg_dsn': PostgresDsn('postgres://user:pass@localhost:5432/foobar',
scheme='postgres', user='user', password='pass', host='localhost',
host_type='int_domain', port='5432', path='/foobar'),
    'special_function': <built-in function cos>,
    'domains': set(),
    'more_settings': {'foo': 'bar', 'apple': 1},
}
"""
