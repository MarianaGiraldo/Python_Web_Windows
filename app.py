import queue
from flask import Flask, render_template, request, redirect
import UserController
import busController
import ticketController
import routeController

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mission')
def mision():
    return render_template('./mission.html')


@app.route('/contactus/<int:num>')
def contactus(num):
    return f'Contact {num}'


@app.route('/routes')
def routes():
    routes = routeController.selectRoutes()
    return render_template('all_routes.html', routes =  routes)


@app.route('/all-tickets')
def all_tickets():
    tickets = ticketController.selectTickets()
    return render_template('all_tickets.html', tickets = tickets, controller = routeController)


@app.route('/buy-tickets', methods=['GET', 'POST'])
def buy_tickets():
    if request.method == 'POST':
        route = request.form['route']
        bus = request.form['bus']
        route_bus_id = routeController.getRouteBusById(route, bus)[0]
        passenger_id = request.form['passenger']
        quantity = request.form['quantity']
        travel_date = request.form['travel_date']
        departure_time = request.form['departure_time']
        ticketController.insertTicket(route_bus_id, passenger_id, quantity, travel_date, departure_time)
        return redirect('/all-tickets')
    elif request.method == 'GET':
        routes = routeController.selectRoutes()
        buses = busController.selectBuses()
        users = UserController.selectUsers()
        return render_template('buy_tickets.html', routes = routes, buses = buses, users = users)

@app.route('/tickets/edit/<int:id>', methods=['GET', 'POST'])
def editTicket(id):
    if request.method == 'POST':
        route = request.form['route']
        bus = request.form['bus']
        route_bus_id = routeController.getRouteBusById(route, bus)[0]
        passenger_id = request.form['passenger']
        quantity = request.form['quantity']
        travel_date = request.form['travel_date']
        departure_time = request.form['departure_time']
        ticketController.editTicket(route_bus_id, passenger_id, quantity, travel_date, departure_time, id)
        return redirect('/all-tickets')
    elif request.method == 'GET':
        ticket = ticketController.getTicketById(id)
        routes = routeController.selectRoutes()
        buses = busController.selectBuses()
        users = UserController.selectUsers()
        return render_template('edit_ticket.html', ticket = ticket, routes = routes, buses = buses, users = users)

@app.route('/tickets/delete/<int:id>')
def deleteTicket(id):
    ticketController.deleteTicketById(id)
    return redirect('/all-tickets')

@app.route('/register')
def register():
    return render_template('register_form.html')


@app.route('/registerUser', methods=['POST'])
def formPost():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        document = request.form['document']
        password = request.form['password']
        UserController.insertUser(name, document, email, phone, password)
        return redirect('/users')
    else:
        return 'User not registered'


@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
def editUser(id):
    if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            document = request.form['document']
            password = request.form['password']
            UserController.editUser(name, document, email, phone, password, id)
            return redirect('/users')
    elif request.method == 'GET':
        user = UserController.getUserById(id)
        return render_template('edit_user.html', user = user)

@app.route('/insert-bus', methods=['GET', 'POST'])
def insertBuses():
    if request.method == 'POST':
            plate = request.form['plate']
            type = request.form['type']
            capacity = request.form['capacity']
            company = request.form['company']
            busController.insertBus(plate, type, capacity, company)
            return redirect('/buses')
    elif request.method == 'GET':
        return render_template('insert_bus.html')
    
@app.route('/buses', methods=['GET', 'POST'])
def allBuses():
    buses = busController.selectBuses()
    return render_template('all_buses.html', buses = buses)

@app.route('/buses/edit/<int:id>', methods=['GET', 'POST'])
def editBus(id):
    if request.method == 'POST':
            plate = request.form['plate']
            type = request.form['type']
            capacity = request.form['capacity']
            company = request.form['company']
            busController.editBus(plate, type, capacity, company, id)
            return redirect('/buses')
    elif request.method == 'GET':
        bus = busController.getBusById(id)
        return render_template('edit_bus.html', bus = bus)

@app.route('/buses/delete/<int:id>')
def deleteBus(id):
    busController.deleteBusById(id)
    return redirect('/buses')

@app.route('/users/delete/<int:id>')
def deleteUser(id):
    UserController.deleteUserById(id)
    return redirect('/users')

@app.route('/users')
def all_users():
    users = UserController.selectUsers()
    return render_template('all_users.html', users = users)


if __name__ == "__main__":
    app.run(port=3080, debug=True)
