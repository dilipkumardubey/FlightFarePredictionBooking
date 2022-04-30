def get_airline_oneHotEncoding(airline):
	# OneHotEncoding of Airline
	if(airline=='Jet Airways'):
		Jet_Airways = 1
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0 

	elif (airline=='IndiGo'):
		Jet_Airways = 0
		IndiGo = 1
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0 

	elif (airline=='Air India'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 1
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0 

	elif (airline=='Multiple carriers'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 1
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0 

	elif (airline=='SpiceJet'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 1
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0 

	elif (airline=='Vistara'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 1
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0

	elif (airline=='GoAir'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 1
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0

	elif (airline=='Multiple carriers Premium economy'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 1
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0

	elif (airline=='Jet Airways Business'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 1
		Vistara_Premium_economy = 0
		Trujet = 0

	elif (airline=='Vistara Premium economy'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 1
		Trujet = 0

	elif (airline=='Trujet'):
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 1

	else:
		Jet_Airways = 0
		IndiGo = 0
		Air_India = 0
		Multiple_carriers = 0
		SpiceJet = 0
		Vistara = 0
		GoAir = 0
		Multiple_carriers_Premium_economy = 0
		Jet_Airways_Business = 0
		Vistara_Premium_economy = 0
		Trujet = 0

	# return [Jet_Airways, IndiGo, Air_India, Multiple_carriers, SpiceJet, Vistara, GoAir, Multiple_carriers_Premium_economy, Jet_Airways_Business, Vistara_Premium_economy, Trujet]
	return [Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business, Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy ]

def get_source_oneHotEncoding(source):
	# OneHotEncoding of Source
	if (source == 'Delhi'):
		s_Delhi = 1
		s_Kolkata = 0
		s_Mumbai = 0
		s_Chennai = 0

	elif (source == 'Kolkata'):
		s_Delhi = 0
		s_Kolkata = 1
		s_Mumbai = 0
		s_Chennai = 0

	elif (source == 'Mumbai'):
		s_Delhi = 0
		s_Kolkata = 0
		s_Mumbai = 1
		s_Chennai = 0

	elif (source == 'Chennai'):
		s_Delhi = 0
		s_Kolkata = 0
		s_Mumbai = 0
		s_Chennai = 1

	else:
		s_Delhi = 0
		s_Kolkata = 0
		s_Mumbai = 0
		s_Chennai = 0

	return s_Delhi, s_Kolkata, s_Mumbai, s_Chennai

def get_destination_oneHotEncoding(destination):
	# OneHotEncoding of Destination
	if (destination == 'Cochin'):
		d_Cochin = 1
		d_Delhi = 0
		d_New_Delhi = 0
		d_Hyderabad = 0
		d_Kolkata = 0

	elif (destination == 'Delhi'):
		d_Cochin = 0
		d_Delhi = 1
		d_New_Delhi = 0
		d_Hyderabad = 0
		d_Kolkata = 0

	elif (destination == 'New_Delhi'):
		d_Cochin = 0
		d_Delhi = 0
		d_New_Delhi = 1
		d_Hyderabad = 0
		d_Kolkata = 0

	elif (destination == 'Hyderabad'):
		d_Cochin = 0
		d_Delhi = 0
		d_New_Delhi = 0
		d_Hyderabad = 1
		d_Kolkata = 0

	elif (destination == 'Kolkata'):
		d_Cochin = 0
		d_Delhi = 0
		d_New_Delhi = 0
		d_Hyderabad = 0
		d_Kolkata = 1

	else:
		d_Cochin = 0
		d_Delhi = 0
		d_New_Delhi = 0
		d_Hyderabad = 0
		d_Kolkata = 0

	return d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata

import random
import pandas as pd
import numpy as np
from datetime import datetime

def prepare_input_dataframe(selected_airline, selected_source, selected_destination, selected_doj, selected_stops, perm_data):
	# Prepares dataframe from inputs

	k = 5 # Select number of rates	
	available_data = random.choices(perm_data[selected_airline], k=5) # Get random 5 combinations of airlines	
	df = pd.DataFrame(available_data, columns =['Departure_Time', 'Duration'])
	departure_time_list = list(df["Departure_Time"])
	df["Dep_hour"] = pd.to_datetime(df["Departure_Time"]).dt.hour
	df["Dep_min"] = pd.to_datetime(df["Departure_Time"]).dt.minute

	# 
	duration = list(df["Duration"])
	duration_hours = []
	duration_mins = []
	for i in range(len(duration)):
	    duration_hours.append(int(duration[i].split(sep="h")[0]))
	    duration_mins.append(int(duration[i].split(" ")[1].split("m")[0]))
	    
	df["Duration_hours"] = duration_hours
	df["Duration_mins"] = duration_mins
	
	df["Total_Duration"] = df["Duration_hours"]*60 + df["Duration_mins"] # total duration in mins
	
	df["Date_of_Journey"] = [selected_doj]*k # column for Date_of_Journey
	df["Departure_Date_Time"] = df["Date_of_Journey"] + " " + df["Departure_Time"]

	#
	df["Actual_Arrival_Date_Time"] = pd.to_datetime(df["Departure_Date_Time"], format="%Y-%m-%d %H:%M") + pd.to_timedelta(df["Total_Duration"],unit='m')
	df["Actual_Arrival_Date"] = df["Actual_Arrival_Date_Time"].dt.date
	df["Actual_Arrival_Time"] = df["Actual_Arrival_Date_Time"].dt.time
	df["Arrival_hour"] = df["Actual_Arrival_Date_Time"].dt.hour
	df["Arrival_min"] = df["Actual_Arrival_Date_Time"].dt.minute

	actual_arrival_date_list = list(df["Actual_Arrival_Date"])
	actual_arrival_time_list = list(df["Actual_Arrival_Time"])

	
	dt = datetime.strptime(selected_doj, "%Y-%m-%d") # Convert string into datetime object	 
	df["Journey_day"] = [dt.day]*5# Column for Journey_day
	df["Journey_month"] = [dt.month]*5 # Column for Journey_month


	#
	encoded_airline = get_airline_oneHotEncoding(selected_airline)
	df['Airline_Air India'] = [encoded_airline[0]]*k
	df['Airline_GoAir'] = [encoded_airline[1]]*k
	df['Airline_IndiGo'] = [encoded_airline[2]]*k
	df['Airline_Jet Airways'] = [encoded_airline[3]]*k
	df['Airline_Jet Airways Business'] = [encoded_airline[4]]*k
	df['Airline_Multiple carriers'] = [encoded_airline[5]]*k
	df['Airline_Multiple carriers Premium economy'] = [encoded_airline[6]]*k
	df['Airline_SpiceJet'] = [encoded_airline[7]]*k
	df['Airline_Trujet'] = [encoded_airline[8]]*k
	df['Airline_Vistara'] = [encoded_airline[9]]*k
	df['Airline_Vistara Premium economy'] = [encoded_airline[10]]*k
	
	# 
	s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = get_source_oneHotEncoding(selected_source)
	df['Source_Chennai'] = [s_Chennai]*k
	df['Source_Delhi'] = [s_Delhi]*k
	df['Source_Kolkata'] = [s_Kolkata]*k
	df['Source_Mumbai'] = [s_Mumbai]*k

	# 
	d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = get_destination_oneHotEncoding(selected_destination)
	df['Destination_Cochin'] = [d_Cochin]*k
	df['Destination_Delhi'] = [d_Delhi]*k
	df['Destination_Hyderabad'] = [d_Hyderabad]*k
	df['Destination_Kolkata'] = [d_Kolkata]*k
	df['Destination_New Delhi'] = [d_New_Delhi]*k

	# 
	df['Total_Stops'] = [selected_stops]*k

	df.drop(["Departure_Time", "Total_Duration", "Duration", "Departure_Date_Time", "Date_of_Journey", "Actual_Arrival_Date_Time", "Actual_Arrival_Date", "Actual_Arrival_Time","Airline_Trujet"], axis=1, inplace=True) # Drop/remove Arrival_Time column

	return df, departure_time_list, actual_arrival_date_list, actual_arrival_time_list, duration

def predict_rate(selected_airline, selected_source, selected_destination, selected_doj, selected_stops, perm_data, model):
	# Prepare input dataframe
	df, departure_time_list, actual_arrival_date_list, actual_arrival_time_list, duration_list = prepare_input_dataframe(selected_airline, selected_source, selected_destination, selected_doj, selected_stops, perm_data)
	predicted_rate_list = model.predict(df)
	df["Departure_Time"] = departure_time_list
	
	time_with_seconds = [i.strftime("%H:%M") for i in actual_arrival_time_list] 
	date_time_list = []
	for ii in range(len(time_with_seconds)):
		date_time_list.append( actual_arrival_date_list[ii].strftime('%Y-%m-%d') + ' ' + time_with_seconds[ii])
	
	df["Actual_Arrival_Date_List"] = departure_time_list
	df["Actual_Arrival_Time_List"] =  date_time_list
	df["Predicted_Rate_List"] = list(np.array(predicted_rate_list, 'float').astype('int'))

	# 
	dataframe = df[["Actual_Arrival_Date_List", "Actual_Arrival_Time_List"]]
	dataframe['Duration'] = duration_list
	dataframe["Total_Stops"] = df["Total_Stops"]
	dataframe["Predicted_Rate_List"] = df["Predicted_Rate_List"]
	return df, dataframe

from datetime import datetime

class Token():
    def __init__(self):
        self.airline = ''
        self.source = ''
        self.destination = ''
        self.date_of_journey = ''
        self.date_of_booking = datetime.now().date().strftime('%Y-%m-%d')
        self.no_stops = ''
        self.arrival_date = ''
        self.arrival_time = ''
        self.duration = ''
        self.flight_fare = ''
        self.no_passengers = ''
        self.passenger_names = ''
        self.passenger_ages = ''
        self.passenger_aadhars = ''
        self.primary_email = 'todilipdubey@gmail.com'
        self.mobile = '987654321'
        self.total_amount = ''
        self.ticket_number = ''
        self.payment_status = False
        self.date_of_payment = ''
        self.bank = ''
        self.transaction_no = ''

    # Generate unique ticket number
    def generate_ticket_number(self):
        ticket_str = self.airline + self.source + self.destination + str(self.date_of_journey) + str(self.date_of_booking) + str(self.flight_fare) + str(self.no_passengers) + self.primary_email + str(self.total_amount)
        ticket_number = str(hash(ticket_str))
        if ticket_number[0] == '-':
            ticket_number = ticket_number.replace('-', 'TM')
        else:
            ticket_number = 'TP'+ ticket_number

        self.ticket_number = ticket_number                          

    # Generates Transaction No for payment
    def generate_transaction_no(self):
    	transaction_str = self.ticket_number + self.bank + str(self.date_of_payment)
    	transaction_number = str(hash(transaction_str))
    	if transaction_number[0] == '-':
    		transaction_number = transaction_number.replace('-', 'TM')
    	else:
    		transaction_number = 'TP' + transaction_number
    	self.transaction_no = transaction_number

# Generate Invoice Table
# from flask import url_for
def get_invoice_table(flight_fare, no_passengers, gst=18):
	amount = flight_fare*no_passengers
	gst_amount = (gst*amount)/100
	grand_total = amount + gst_amount
	invoice_table = [flight_fare, no_passengers, amount, gst, gst_amount, grand_total]
	return invoice_table


# Get absolute path for file.
import os		
def get_absolute_path(filename):
	base_path = os.getcwd() # Replace this appropriately with your static folder path
	# We shouldn't use 'static' twice if it is already there in the base_path as correctly pointed out by mark-hildreth
	if os.path.basename(base_path) == 'static':
	    file_path = os.path.normpath('/qr_images/'+filename)
	else:
	    file_path = os.path.normpath('/static//qr_images/'+filename)
	
	abs_path = os.path.join(base_path+file_path)
	
	if os.path.exists(abs_path): # Verifies existence of given path
	    print(abs_path, '\n\n\n\n')	

	return abs_path

# Generates QR code for Payment URL
import pyqrcode
import png
def create_qrcode(payment_url, qr_fullpath):	
	url = pyqrcode.create(payment_url) # Generate QR code
	# url.svg("myqr.svg", scale = 8) # Create and save the svg file naming "myqr.svg"
	url.png(qr_fullpath, scale = 6) # Create and save the png file naming "myqr.png"	