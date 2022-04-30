from flask import render_template, request, redirect, url_for, jsonify
from prediction_app import app

from prediction_app.utils import *
import os
import json
import pickle

# Load pretrained model
MODEL_FILENAME = "flight_rf.pkl"
MODEL_FULLPATH = os.path.join(app.static_folder, 'media', MODEL_FILENAME)
with open(MODEL_FULLPATH, "rb") as file:
	model = pickle.load(file)

# Load Flight Arrival_Time and Duration 
ARR_DUR_FILENAME = "airline_depTime_dur.pkl"
ARR_DUR_FULLPATH = os.path.join(app.static_folder, 'media', ARR_DUR_FILENAME)
with open(ARR_DUR_FULLPATH, "rb") as file:
	flight_details = pickle.load(file)

global BASE_URL

# Create token
token = Token()
token.payment_status = False

@app.route('/', methods=['GET', 'POST'])
def home():
	BASE_URL = request.base_url
	# print('base Url is ', request.base_url, '\n\n\n\n')
	if request.method == 'POST':
		airline = request.form.get('airline')
		source = request.form.get('source')
		destination = request.form.get('destination')
		doj = request.form.get('date_of_journey')
		no_stops = request.form.get('no_stops')
 
		_, dataframe = predict_rate(airline, source, destination, doj, no_stops, flight_details, model)

		# Extract required data
		column_name_list = ['Departure Time','Arrival Time', 'Duration', 'Number of Stops', 'Fare (Rs)', 'Book']
		row_data = list(dataframe.values.tolist())

		# Update token
		token.airline = airline
		token.source = source
		token.destination = destination
		token.date_of_journey = doj
		token.no_stops = no_stops
		token.payment_status = False

		return render_template('home.html', title='Flight Fare Prediction', column_name_list=column_name_list, row_data=row_data, zip=zip)

	return render_template('home.html', title="Flight Fare Prediction")

@app.route('/booking_page', methods=['GET', 'POST'])
def booking_page():
	if request.method=='POST':
		# Update token
		token.arrival_date = request.form.get('arrival_date')
		token.arrival_time = request.form.get('arrival_time')
		token.duration = request.form.get('duration')
		token.flight_fare = request.form.get('flight_fare')
		token.payment_status = False

		return jsonify({'route' : url_for('book_ticket')})

# Function which render template to add passengers details
@app.route('/book_ticket')
def book_ticket():
	return render_template('book_ticket.html', title='Book Ticket', token=token)

# Function to display Added Passengers details
@app.route('/continue_to_payment', methods=['GET', 'POST'])
def continue_to_payment():	
	if request.method=='POST':
		data_dict = request.form.to_dict()
		name_array_str = data_dict['name_array']
		age_array_str = data_dict['age_array']
		aadhar_array_str = data_dict['aadhar_array']

		name_list = json.loads(name_array_str)
		age_list = json.loads(age_array_str)
		aadhar_list = json.loads(aadhar_array_str)
		
		# Update token
		token.no_passengers = len(name_list)
		token.passenger_names = name_list
		token.passenger_ages = age_list
		token.passenger_aadhars = aadhar_list
		token.payment_status = False

		return jsonify({'success' : 'ok'})

# Get URL for Payment Details Address
@app.route('/get_payment_details_address', methods=[
	'POST'])
def get_payment_details_address():
	if request.method=='POST':
		token.generate_ticket_number()	
		ticket_number = token.ticket_number	
		
		payment_url = request.url_root[:-1] + url_for('make_payment', ticket_number=ticket_number)
		
		filename = ticket_number + '.png'
		qr_fullpath = 'prediction_app/static/qr_images/' + filename
		create_qrcode(payment_url, qr_fullpath)

		return jsonify({
			'success': 'ok',
			'route' : url_for('payment_details'),
			})

		
# Show payment details
@app.route('/payment_details')
def payment_details():
	invoice_table = get_invoice_table(int(float(token.flight_fare)), int(token.no_passengers))
	token.total_amount = invoice_table[5]
	filename = 'qr_images/'+token.ticket_number+'.png'
	invoice_table.append(url_for('static', filename=filename))

	return render_template('payment_detail.html', title="Payment Details", invoice_table=invoice_table)


# Get payment link
@app.route('/get_make_payment_address', methods=['POST'])
def get_make_payment_address():
	ticket_number = token.ticket_number
	return jsonify({
		'success' : 'ok',
		'route' : url_for('make_payment', ticket_number=ticket_number)
		})

# Check payment status
@app.route('/make_payment/check_payment_status', methods=['POST'])
def check_payment_status():
	if request.method=="POST":
		payment_status = "NOT PAID"
		if token.payment_status:
			payment_status = "PAID"
		
		return jsonify({
			'payment_status': payment_status,
			'route' : url_for('thanks') 
			})

# Show Payment page
@app.route('/make_payment/<ticket_number>')
def make_payment(ticket_number):
	return render_template('make_payment.html', title="Make Payment", amount=token.total_amount)

# Generates Transaction Number
@app.route('/make_payment/generate_transaction_no', methods=['POST'])
def generate_transaction_no():
	if request.method=='POST':
		token.bank = request.form.get('selected_bank')
		token.payment_status = True
		token.date_of_payment = datetime.now().date()
		token.generate_transaction_no()
		return jsonify({
			'success' : 'ok',
			'transaction_no' : token.transaction_no
		})

# Generates Ticket PDF
@app.route('/thanks')
def thanks():
	name_list= token.passenger_names
	age_list = token.passenger_ages
	aadhar_list = token.passenger_aadhars	
	data_list = zip(name_list, age_list, aadhar_list)
	invoice_table = get_invoice_table(int(float(token.flight_fare)), int(token.no_passengers))
	filename = token.ticket_number + '.pdf'
	return render_template('ticket_details.html', title='Ticket Details', ticket=token, data_list=data_list, invoice_table=invoice_table, filename=filename)