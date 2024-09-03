from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database_Xisob:

    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            oper varchar(255),
            kassa varchar(255),
            kyxt varchar(255),
            qzu varchar(255),
            tafsil varchar(255),
            val varchar(255),
            summa varchar(255),
            fish varchar(255),
            vaqt varchar(255)
            );
"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, oper: str = None, kassa: str = None, kyxt: str = None,
                       qzu: str = None, tafsil: str = None, val: str = None, summa: str = None,
                       fish: str = None, vaqt: str = None):

        sql = """
        INSERT INTO Users(oper, kassa, kyxt, qzu, tafsil, val, summa, fish, vaqt) 
        VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9) returning *
        """
        return await self.execute(sql, oper, kassa, kyxt, qzu, tafsil, val, summa, fish, vaqt,
                                  fetchrow=True)

    # async def update_user_bonus(self, phone_nomer, bonus):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
    #
    #     sql = f"""
    #     UPDATE Users SET bonus=$1 WHERE phone_nomer=$2
    #     """
    #     return await self.execute(sql, bonus, phone_nomer, fetchrow=True)

    # async def update_user_qabul(self, user_id, doctor, oy, day, soat):
    #     # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"
    #
    #     sql = f"""
    #     UPDATE Users SET doctor=$1, oy = $2,day=$3, soat=$4 WHERE user_id=$5
    #     """
    #     return await self.execute(sql, doctor, oy, day, soat, user_id,  fetchrow=True)

    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        return await self.execute("SELECT COUNT(*) FROM Users", fetchval=True)


    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)


