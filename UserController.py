from Db import mysqlConnect 

def insertUser(name, document, email, phone, password):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "INSERT INTO `passengers`(`full_name`, `document`, `email`, `phone`, `password`) VALUES (%s,%s,%s,%s,%s) "
            cursor.execute(sql, (name, document, email, phone, password))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def selectUsers():
    try :
        conn = mysqlConnect()
        users = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `passengers`"
            cursor.execute(sql)
            users = cursor.fetchall()
            conn.close()
        return users
    except:
        print("An exception occurred")

def getUserById(id):
    try :
        conn = mysqlConnect()
        user = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `passengers` WHERE id = %s"
            cursor.execute(sql, (id))
            user = cursor.fetchone()
            conn.close()
        return user
    except:
        print("An exception occurred")
        

def editUser(name, document, email, phone, password, id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "UPDATE `passengers` SET `full_name` = %s, document = %s, `email` = %s, `phone` = %s, `password` = %s WHERE `id` = %s;"
            cursor.execute(sql, (name, document, email, phone, password, id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def deleteUserById(id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "DELETE FROM `passengers` WHERE id = %s"
            cursor.execute(sql, (id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")        
        