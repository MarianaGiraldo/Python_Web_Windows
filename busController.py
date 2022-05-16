from Db import mysqlConnect 

def insertBus(plate, type, capacity, company):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "INSERT INTO `buses`(`plate`, `type`, `capacity`, `company`) VALUES (%s,%s,%s,%s) "
            cursor.execute(sql, (plate, type, capacity, company))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def selectBuses():
    try :
        conn = mysqlConnect()
        buses = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `buses`"
            cursor.execute(sql)
            buses = cursor.fetchall()
            conn.close()
        return buses
    except:
        print("An exception occurred")

def getBusById(id):
    try :
        conn = mysqlConnect()
        bus = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `buses` WHERE id = %s"
            cursor.execute(sql, (id))
            bus = cursor.fetchone()
            conn.close()
        return bus
    except:
        print("An exception occurred")
        

def editBus(plate, type, capacity, company, id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "UPDATE `buses` SET `plate`= %s,`type`= %s,`capacity`= %s,`company`= %s WHERE id = %s"
            cursor.execute(sql, (plate, type, capacity, company, id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def deleteBusById(id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "DELETE FROM `buses` WHERE id = %s"
            cursor.execute(sql, (id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")       