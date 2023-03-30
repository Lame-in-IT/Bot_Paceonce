from tokin_bot import conect_bd
import psycopg2

# def connect_database():
#     try:
#         connection = psycopg2.connect(
#             database=conect_bd["database"],
#             user=conect_bd["user"],
#             password=conect_bd["password"],
#             host=conect_bd["host"],
#             port=conect_bd["port"],
#         )
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """ CREATE TABLE Bot_Paceonce(
#                     id_user TEXT NOT NULL,
#                     is_bot TEXT,
#                     first_name TEXT,
#                     username TEXT,
#                     language_code TEXT,
#                     screenshot TEXT,
#                     appeal_True TEXT,
#                     appeal TEXT,
#                     date_scrin TEXT,
#                     telephon TEXT
#                     );"""
#             )
#             print("База создана")
#     except Exception as ex:
#         print(ex)
 
def commect_bd():
    try:
        connection = psycopg2.connect(
            database=conect_bd["database"],
            user=conect_bd["user"],
            password=conect_bd["password"],
            host=conect_bd["host"],
            port=conect_bd["port"],
        )
        connection.autocommit = True
        return connection
    except Exception as ex:
        print(ex)
        
def read_bd(user_id):
    try:
        connection = commect_bd()
        list_id_user = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id_user FROM Bot_Paceonce")
            for item_id_user in cursor.fetchall():
                list_id_user.append(item_id_user[0])
        if str(user_id) in list_id_user:
            return True
        elif str(user_id) not in list_id_user:
            return False
    except Exception as ex:
        print(ex)
        
def create_user(data_user):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO Bot_Paceonce(id_user, is_bot, first_name, username, language_code)
                            VALUES(%s, %s, %s, %s, %s)""", [data_user["id"], data_user["is_bot"], data_user["first_name"],
                                                                    data_user["username"], data_user["language_code"]])
    except Exception as ex:
        print(ex)

def create_appeal_True(id_user, appeal_True):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Paceonce SET appeal_True = %s WHERE id_user = %s""", [
                        appeal_True, str(id_user)])
    except Exception as ex:
        print(ex)
        
def create_telephon(id_user, namver_phon):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Paceonce SET telephon = %s WHERE id_user = %s""", [
                        namver_phon, str(id_user)])
    except Exception as ex:
        print(ex)


def read_appeal_True(id_user):
    try:
        connection = commect_bd()
        list_appeal_True = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT appeal_True FROM Bot_Paceonce WHERE id_user = '{id_user}'")
            for item_appeal_True in cursor.fetchall():
                list_appeal_True.append(item_appeal_True[0])
        return list_appeal_True[0]
    except Exception as ex:
        print(ex)

def create_appeal(id_user, appeal):
    try:
        connection = commect_bd()
        list_appeal = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT appeal FROM Bot_Paceonce WHERE id_user = '{id_user}'")
            for item_appeal in cursor.fetchall():
                for item_1 in item_appeal:
                    list_appeal.append(item_1)
        list_appeal.append(str(appeal))
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Paceonce SET appeal = %s WHERE id_user = %s""", [
                        list_appeal, str(id_user)])
    except Exception as ex:
        print(ex)

def create_screenshot(id_user, screenshot):
    try:
        connection = commect_bd()
        list_telephon = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT telephon FROM Bot_Paceonce WHERE id_user = '{id_user}'")
            for item_telephon in cursor.fetchall():
                for item_telephon1 in item_telephon:
                    list_telephon.append(item_telephon1)
        if list_telephon[0] != None:
            list_screenshot = []
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT screenshot FROM Bot_Paceonce WHERE id_user = '{id_user}'")
                for item_appeal in cursor.fetchall():
                    for item_1 in item_appeal:
                        list_screenshot.append(item_1)
            list_screenshot.append(str(screenshot))
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE Bot_Paceonce SET screenshot = %s WHERE id_user = %s""", [
                            list_screenshot, str(id_user)])
            return [str(list_screenshot[-1]), list_telephon[0]] 
        elif list_telephon[0] == None:
            return ["No", "No"]
        
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    create_screenshot()