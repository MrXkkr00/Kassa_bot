# from utils.db_api.users_sql import Database_User
#
# db = Database_User(path_to_db='test.db')
#
# db.create_table_users()
# db.add_user(user_id=34123, user_name="Rasulbek", full_name="Qadomboyev_r", birth_day='11-07-2000', phone_nomer="1",
#             bonus=2, day=3, soat=4, doctor="sardor")
# user = db.select_user(user_id=34123)
# print(user)
# bonus = db.update_user_bonus(user_id=34123, bonus=22)
# print(bonus)
# day = db.update_user_qabul(user_id=34123, day=33,oy=12, soat= 12,doctor="alisher")
# print(day)
import asyncio
from time import strftime, gmtime

from utils.db_api.xisobot import Database_Xisob


# soat = (int(strftime('%H', gmtime())) + 5) % 24
# time = str(strftime(f"%d %b {soat}:%M", gmtime()))
# oy = str(strftime(f"%B", gmtime()))
# oy_son = int(strftime(f"%m", gmtime()))
# print(time)
# print(oy)
# print(type(oy_son))
# print((oy_son))


async def test():
    db = Database_Xisob()
    await db.create()
    # await db.drop_users()

    # await db.create_table_users()
    # print(type(user10))
    # user10 = await db.add_user(oper="1231")
    user10 = await db.select_all_users()

    print(user10)
    # for i in range(len(user10)):
    #     print(user10[i])
    #     print("\n")

# soat = (int(strftime('%H', gmtime())) + 5) % 24
# vaqt = str(strftime(f"%d.%b.%Y {soat}:%M", gmtime()))
# print(soat)
# print(finish_time)

asyncio.run(test())

#
# soat = "10-11"
# print(soat[:2])
# print(soat[2])
# print(soat[3:5])
