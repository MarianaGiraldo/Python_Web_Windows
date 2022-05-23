from Db import mysqlConnect 

def insertTicket(route_bus_id, passenger_id, quantity, travel_date, departure_time):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "INSERT INTO `tickets`(`route_bus_id`, `passenger_id`, `quantity`, `travel_date`, `departure_time`) VALUES (%s,%s,%s,%s,%s) "
            cursor.execute(sql, (route_bus_id, passenger_id, quantity, travel_date, departure_time))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def selectTickets():
    try :
        conn = mysqlConnect()
        tickets = []
        with conn.cursor() as cursor:
            sql = """SELECT t.id,  r.origin, r.destination, b.plate, b.type, p.full_name, p.document, t.quantity, t.travel_date, t.departure_time 
                FROM tickets t 
                INNER JOIN passengers p ON p.id = t.passenger_id
                INNER JOIN route_bus rb ON t.route_bus_id = rb.id
                INNER JOIN routes r ON r.id=rb.route_id 
                INNER JOIN buses b ON b.id=rb.bus_id
                """
            cursor.execute(sql)
            tickets = cursor.fetchall()
            conn.close()
        return tickets
    except:
        print("An exception occurred")

def getTicketById(id):
    try :
        conn = mysqlConnect()
        ticket = []
        with conn.cursor() as cursor:
            sql = """SELECT t.id,  r.id, b.id, p.id, t.quantity, t.travel_date, t.departure_time 
                FROM tickets t 
                INNER JOIN passengers p ON p.id = t.passenger_id
                INNER JOIN route_bus rb ON t.route_bus_id = rb.id
                INNER JOIN routes r ON r.id=rb.route_id 
                INNER JOIN buses b ON b.id=rb.bus_id
                WHERE t.id = %s
                """
            cursor.execute(sql, (id))
            ticket = cursor.fetchone()
            conn.close()
        return ticket
    except:
        print("An exception occurred")
        

def editTicket(route_bus_id, passenger_id, quantity, travel_date, departure_time, id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "UPDATE `tickets` SET route_bus_id = %s, passenger_id = %s, quantity = %s, travel_date = %s, departure_time = %s WHERE id = %s"
            cursor.execute(sql, (route_bus_id, passenger_id, quantity, travel_date, departure_time, id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")
        

def deleteTicketById(id):
    try :
        conn = mysqlConnect()
        with conn.cursor() as cursor:
            sql = "DELETE FROM `tickets` WHERE id = %s"
            cursor.execute(sql, (id))
            conn.commit()
            conn.close()
    except:
        print("An exception occurred")       