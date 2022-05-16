from flask import Flask, render_template, request, redirect
import UserController
import busController

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
    return render_template('show_routes.html')


@app.route('/all-tickets')
def all_tickets():
    return render_template('show_tickets.html')


@app.route('/buy-tickets')
def buy_tickets():
    return render_template('buy_tickets.html')


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
    buses =busController.selectBuses()
    return render_template('all_buses.html', buses = buses)

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
