
import copy
from src.application.UserConverter import UserConverter
from src.application.EventService import EventService
from src.data.User import User
from src.application.UserService import UserService
from src.application.EventConverter import EventConverter
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager,login_user, current_user, logout_user, login_required
from src import login_manager,app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user)
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        user_service = UserService()
        try:
            user = user_service.login(request.form['email'],request.form['password'])
        except:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('user_page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        #hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user_service = UserService()
        user_converter = UserConverter()
        input_data = dict(request.form)
        confirm_password = input_data.pop('confirm_password',None)
        if confirm_password == input_data['password']:
            user = user_converter.dict_to_object(input_data)
        else:
            flash('Passwords are not the same')
            user = None
        try:
            user = user_service.create_user(user)
        except:
            flash('Error creating user')
        else:
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
    return render_template('register.html') 

@app.route('/new_event', methods=['GET', 'POST'])
@login_required
def new_event(sub_events = [], is_subevent = False):
    if request.method == 'POST':
        if request.args.get('is_subevent') == 'True':
            converter = EventConverter()    
            input_data = dict(request.form)
            input_data['host'] = copy.deepcopy(current_user)
            sub_event = converter.dict_to_object(input_data)
            sub_events.append(sub_event)
            #redirect to itself to avoid refreshing-resubmitting problem
            return redirect(url_for('new_event', sub_events=sub_events))
        else:
            converter = EventConverter()    
            event_service = EventService()
            event = None
            input_data = dict(request.form)
            input_data['host'] = copy.deepcopy(current_user)
            
            try:
                event = converter.dict_to_object(input_data)
                #return event if save successfully
                event = event_service.save(event)
                for sub_event in sub_events:
                    sub_event.set_event_parent(event)
                    event_service.save(sub_event)
            except Exception as error:
                flash(str(error),'danger')
                return render_template('create_event.html', sub_events = sub_events,error=error)
            else:
                flash('Evento criado com sucesso','success')
                return redirect(url_for('home'))
    return render_template('create_event.html',sub_events = sub_events)

@login_manager.unauthorized_handler
def unauthorized_callback():
    print(request.path)
    return redirect(url_for('login',next=request.path))

@app.route('/search', methods=['GET', 'POST'])    
def search():
    events = []
    if request.method == 'POST':
        event_service = EventService()
        if request.form.get('filter') == 'Nome':
            events = event_service.get_events_by_name(request.form.get('input'))
        elif request.form.get('filter') == 'Genero':
            events = event_service.get_events_by_category(request.form.get('input'))
        elif request.form.get('filter') == 'Localidade':
            events = event_service.get_events_by_address_string(request.form.get('input'))
        #default search by event
        else:
            events = event_service.get_events_by_name(request.form.get('input'))
    return render_template('search_form.html',events=events)

@app.route("/event/<int:event_id>")
def event(event_id):  
    event_service = EventService()
    event = event_service.get_event_by_id(event_id)
    return render_template('event_page.html',event=event)

@app.route("/event/<int:event_id>/subscribe")
def subscribe(event_id):
    user_service = UserService()
    try:
        user_service.subscribe_to_event(event_id,current_user.get_id())
    except Exception as error:
        flash(str(error),'danger')
    else:
        flash('Inscrito com sucesso','success')
        return redirect(url_for('home'))
    return redirect(url_for('event',event_id=event_id))

@app.route("/event/<int:event_id>/check_in")
def check_in(event_id):
    user_service = UserService()
    try:
        has_checked_in = False
        user_service.check_in(event_id,current_user.get_id())
    except Exception as error:
        flash(str(error),'danger')
    else:
        has_checked_in = True
        flash('Check in feito com sucesso','success')
    print(has_checked_in)
    return render_template('presence_confirmation.html',check_in=has_checked_in, action_name='check-in')

