
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import render_template, request, redirect, url_for
#from app import app, db
#from models import Room, Block  # adjust import based on your file

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY','dev_secret_key')

# DATABASE: default sqlite; set DATABASE_URL env var to use MySQL e.g. mysql+pymysql://user:pass@host/db
db_uri = os.environ.get('DATABASE_URL','sqlite:///hostel.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Models ---
class Block(db.Model):
    block_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    total_floors = db.Column(db.Integer, default=1)

class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_no = db.Column(db.String(20), nullable=False)
    block_id = db.Column(db.Integer, db.ForeignKey('block.block_id'), nullable=False)
    floor_no = db.Column(db.Integer, default=1)
    capacity = db.Column(db.Integer, nullable=False)
    occupancy = db.Column(db.Integer, default=0)
    room_type = db.Column(db.String(20))
    monthly_fee = db.Column(db.Float, default=0.0)
    block = db.relationship('Block', backref=db.backref('rooms', lazy=True))

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    admission_no = db.Column(db.String(30), unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    department = db.Column(db.String(100))
    year_of_study = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    join_date = db.Column(db.Date, default=date.today)
    is_active = db.Column(db.Boolean, default=True)

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    assigned_block = db.Column(db.Integer, db.ForeignKey('block.block_id'))
    block = db.relationship('Block', backref=db.backref('staff_members', lazy=True))

class Allocation(db.Model):
    allocation_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.room_id'), nullable=False)
    allocate_date = db.Column(db.Date, default=date.today)
    leave_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.String(255))
    student = db.relationship('Student', backref=db.backref('allocations', lazy=True))
    room = db.relationship('Room', backref=db.backref('allocations', lazy=True))

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    amount = db.Column(db.Float, default=0.0)
    payment_date = db.Column(db.Date, default=date.today)
    for_month = db.Column(db.Date, nullable=False)
    payment_mode = db.Column(db.String(20))
    remarks = db.Column(db.String(255))
    student = db.relationship('Student', backref=db.backref('payments', lazy=True))

# --- Simple admin auth for demo ---
def is_logged_in():
    return session.get('admin_logged_in', False)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # demo credentials (for production, store hashed passwords in DB)
        if username=='admin' and password=='admin123':
            session['admin_logged_in'] = True
            session['admin_user'] = 'admin'
            flash('Logged in as admin','success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials','danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out','info')
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not is_logged_in():
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    total_students = Student.query.count()
    total_rooms = Room.query.count()
    vacant_rooms = Room.query.filter(Room.capacity > Room.occupancy).count()
    return render_template('dashboard.html', total_students=total_students, total_rooms=total_rooms, vacant_rooms=vacant_rooms)

# --- Students CRUD ---
@app.route('/students')
def students():
    if not is_logged_in():
        return redirect(url_for('login'))
    q = Student.query.all()
    return render_template('students.html', students=q)
from datetime import datetime

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        admission_no = request.form['admission_no']
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        year_of_study = request.form['year_of_study']

        #Convert string dates to Python date objects
        date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
        join_date = datetime.strptime(request.form['join_date'], '%Y-%m-%d').date()

        new_student = Student(
            admission_no=admission_no,
            fullname=fullname,
            email=email,
            phone=phone,
            department=department,
            year_of_study=year_of_study,
            date_of_birth=date_of_birth,
            join_date=join_date,
            is_active=True
        )

        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('students'))

    return render_template('add_student.html')


# --- Rooms ---
@app.route('/rooms')
def rooms():
    if not is_logged_in():
        return redirect(url_for('login'))
    room_list = Room.query.join(Block).add_columns(Room.room_id, Room.room_no, Room.capacity, Room.occupancy, Room.room_type, Room.monthly_fee, Block.name.label('block_name')).all()
    return render_template('rooms.html', rooms=room_list)
@app.route('/add_room', methods=['GET', 'POST'])
def add_room():
    from datetime import date
    blocks = Block.query.all()   # ✅ this fetches all available blocks

    if request.method == 'POST':
        room = Room(
            room_no=request.form['room_no'],
            block_id=request.form['block_id'],
            floor_no=request.form['floor_no'],
            capacity=request.form['capacity'],
            occupancy=request.form['occupancy'],
            room_type=request.form['room_type'],
            monthly_fee=request.form['monthly_fee']
        )
        db.session.add(room)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_room.html', blocks=blocks)

#-- Delete Room --
@app.route('/rooms/delete/<int:room_id>', methods=['POST'])
def delete_room(room_id):
    if not is_logged_in():
        return redirect(url_for('login'))

    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    return redirect(url_for('rooms'))


# --- Blocks ---
@app.route('/blocks')
def blocks():
    if not is_logged_in():
        return redirect(url_for('login'))
    b = Block.query.all()
    return render_template('blocks.html', blocks=b)

@app.route('/blocks/add', methods=['GET','POST'])
def add_block():
    if not is_logged_in():
        return redirect(url_for('login'))
    if request.method=='POST':
        b = Block(name=request.form.get('name'), address=request.form.get('address'), total_floors=request.form.get('total_floors') or 1)
        db.session.add(b); db.session.commit()
        flash('Block added','success'); return redirect(url_for('blocks'))
    return render_template('add_block.html')

# --- Staff ---
@app.route('/staff')
def staff():
    if not is_logged_in():
        return redirect(url_for('login'))
    s = Staff.query.all()
    return render_template('staff.html', staff_list=s)

@app.route('/staff/add', methods=['GET','POST'])
def add_staff():
    if not is_logged_in():
        return redirect(url_for('login'))
    blocks = Block.query.all()
    if request.method=='POST':
        st = Staff(fullname=request.form.get('fullname'), role=request.form.get('role'), phone=request.form.get('phone'), email=request.form.get('email'), assigned_block=request.form.get('assigned_block') or None)
        db.session.add(st); db.session.commit()
        flash('Staff added','success'); return redirect(url_for('staff'))
    return render_template('add_staff.html', blocks=blocks)

# --- Allocations ---
@app.route('/allocations')
def allocations():
    if not is_logged_in():
        return redirect(url_for('login'))
    a = Allocation.query.filter(Allocation.leave_date==None).all()
    return render_template('allocations.html', allocations=a)

@app.route('/allocations/add', methods=['GET','POST'])
def add_allocation():
    if not is_logged_in():
        return redirect(url_for('login'))
    students = Student.query.all()
    rooms = Room.query.filter(Room.capacity > Room.occupancy).all()
    if request.method=='POST':
        student_id = request.form.get('student_id')
        room_id = request.form.get('room_id')
        notes = request.form.get('notes')
        # simple check: does student already have active allocation?
        existing = Allocation.query.filter_by(student_id=student_id, leave_date=None).first()
        if existing:
            flash('Student already has an allocation','danger')
            return redirect(url_for('allocations'))
        alloc = Allocation(student_id=student_id, room_id=room_id, notes=notes)
        db.session.add(alloc)
        # increment occupancy
        room = Room.query.get(room_id); room.occupancy = (room.occupancy or 0) + 1
        db.session.commit()
        flash('Allocated room','success'); return redirect(url_for('allocations'))
    return render_template('add_allocation.html', students=students, rooms=rooms)

@app.route('/allocations/deallocate/<int:allocation_id>')
def deallocate(allocation_id):
    if not is_logged_in(): return redirect(url_for('login'))
    alloc = Allocation.query.get_or_404(allocation_id)
    if alloc.leave_date is None:
        alloc.leave_date = date.today()
        if alloc.room:
            alloc.room.occupancy = max(0, (alloc.room.occupancy or 0) - 1)
        db.session.commit()
        flash('Deallocated','success')
    return redirect(url_for('allocations'))

# --- Payments ---
@app.route('/payments')
def payments():
    if not is_logged_in(): return redirect(url_for('login'))
    p = Payment.query.order_by(Payment.payment_date.desc()).all()
    return render_template('payments.html', payments=p)

@app.route('/payments/add', methods=['GET','POST'])
def add_payment():
    if not is_logged_in(): return redirect(url_for('login'))
    students = Student.query.all()
    if request.method=='POST':
        p = Payment(student_id=request.form.get('student_id'), amount=float(request.form.get('amount') or 0.0), for_month=request.form.get('for_month'), payment_mode=request.form.get('payment_mode'), remarks=request.form.get('remarks'))
        db.session.add(p); db.session.commit()
        flash('Payment recorded','success'); return redirect(url_for('payments'))
    return render_template('add_payment.html', students=students)

# --- Init DB helper ---
@app.cli.command('initdb')
def initdb():
    db.create_all()
    print('DB initialized (tables created)')

if __name__=='__main__':
    app.run(debug=True)
