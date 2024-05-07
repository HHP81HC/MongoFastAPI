# Standard Library
# Standard Library
import os
from logging import Logger
from logging.config import fileConfig

# My Stuff
from alembic import context

from dotenv import load_dotenv
from sqlalchemy import pool
from sqlalchemy import engine_from_config


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
log = Logger(__name__)


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def load_env_var(env_var: str) -> str:
    """
    Load the value of the specified environment variable.

    Args:
        env_var (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not found.

    """
    status = load_dotenv()
    if status:
        return os.getenv(env_var)
    raise ValueError


def load_env_cmd() -> str:
    """
    Load the environment variable 'DB' and return its value.
    If the variable is not set, return the default value 'DB_LOCAL'.

    Returns:
        str: The value of the 'DB' environment variable or the default value 'DB_LOCAL'.
    """
    name = os.getenv("DB")
    return name


url = load_env_var("DB_ALEMBIC")
if url != "":
    config.set_main_option("sqlalchemy.url", url)
else:
    log.warning('Environment variable SETTINGS missing. Use pre-defined file for URL.')


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
