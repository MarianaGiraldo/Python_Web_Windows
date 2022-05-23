from Db import mysqlConnect 

def selectRoutes():
    try :
        conn = mysqlConnect()
        routes = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `routes`"
            cursor.execute(sql)
            routes = cursor.fetchall()
            conn.close()
        return routes
    except:
        print("An exception occurred")

def getRouteById(id):
    try :
        conn = mysqlConnect()
        bus = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `routes` WHERE id = %s"
            cursor.execute(sql, (id))
            bus = cursor.fetchone()
            conn.close()
        return bus
    except:
        print("An exception occurred")

def getRouteBusById(route_id, bus_id):
    try :
        conn = mysqlConnect()
        bus = []
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `route_bus` WHERE route_id = %s AND bus_id = %s LIMIT 1"
            cursor.execute(sql, (route_id, bus_id))
            bus = cursor.fetchone()
            conn.close()
        return bus
    except:
        print("An exception occurred")
        
def getRouteAndBusByRBId(id):
    try :
        conn = mysqlConnect()
        bus = []
        with conn.cursor() as cursor:
            sql = "SELECT r.origin, r.destination, b.plate, b.type FROM route_bus rb INNER JOIN routes r ON r.id=rb.route_id INNER JOIN buses b ON b.id=rb.bus_id"
            cursor.execute(sql, (id))
            bus = cursor.fetchone()
            conn.close()
        return bus
    except:
        print("An exception occurred")
        