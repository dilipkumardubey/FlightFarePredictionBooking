// 
var passenger_number;
$(document).ready(function(){
	passenger_number = 2;
})

// Create array for airlines
var airline_list = new Array('Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet', 
							'Vistara', 'Air Asia', 'GoAir', 'Multiple carriers Premium economy',
							'Jet Airways Business', 'Vistara Premium economy', 'Trujet');
function print_airline(airline_id){
	var option_str = document.getElementById(airline_id);
	option_str.length = 0;
	option_str.options[0] = new Option('---- Select Airline ----', '');	
	for(var i=0; i<airline_list.length; i++){
		option_str.options[option_str.length] = new Option(airline_list[i], airline_list[i]);
	}
	option_str.selectedIndex = 1;
}

// Create array for source
var source_list = new Array('Delhi', 'Kolkata', 'Banglore', 'Mumbai', 'Chennai');
function print_source(source_id){
	option_str = document.getElementById(source_id);
	option_str.length = 0;
	option_str.options[0] = new Option('---- Select Source ----', '');	
	for(var i=0; i<source_list.length; i++){
		option_str.options[option_str.length] = new Option(source_list[i], source_list[i]);
	}
	option_str.selectedIndex = 1;
}

// Create array for destination and 
var destination_list = new Array('Cochin', 'Banglore', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata');
function print_destination(destination_id){
	var option_str = document.getElementById(destination_id);
	option_str.length = 0;
	option_str.options[0] = new Option('---- Select Destination ----', '');
	for(var i=0; i<destination_list.length; i++){
		option_str.options[option_str.length] = new Option(destination_list[i], destination_list[i]);
	}
	option_str.selectedIndex = 1;
}

// Create array for number of stops and print.
var noStops_list = new Array('0', '1', '2', '3');
function print_noStops(noStops_id){
	var option_str = document.getElementById(noStops_id);
	option_str.length = 0;
	option_str.options[0] = new Option('---- Select No of stops ----', '');
	for(var i=0; i<noStops_list.length; i++){
		option_str.options[option_str.length] = new Option(noStops_list[i], noStops_list[i]);
	}
	option_str.selectedIndex = 1;
}

// Create array for bank and print.
var bank_list = new Array('State Bank of India', 'HDFC', 'ICICI', 'Dena Bank');
function print_bank(bank_id){
	var option_str = document.getElementById(bank_id);
	option_str.length = 0;
	option_str.options[0] = new Option('--- Select bank ---', '');
	for(var i=0; i<bank_list.length; i++){
		option_str.options[option_str.length] = new Option(bank_list[i], bank_list[i]);
	}
	option_str.selectedIndex = 1;
}
// Function to get passengers details
function get_passengers_details(element){
	var row_id = element.parentNode.parentNode.rowIndex;
	var row_data = document.getElementById("search_flights_table").rows[row_id];
	var arrival_date = row_data.cells.item(0).innerHTML;
	var arrival_time = row_data.cells.item(1).innerHTML;
	var duration = row_data.cells.item(2).innerHTML;
	var no_stops = row_data.cells.item(3).innerHTML;
	var flight_fare = row_data.cells.item(4).innerHTML;

	var data_to_send = {'arrival_date': arrival_date, 'arrival_time':arrival_time, 'duration':duration, 'no_stops':no_stops, 'flight_fare':flight_fare}
	
	$.ajax({
		type: 'POST',
		url: 'booking_page',
		data: data_to_send,
		success:function(response){
			window.location.href = response.route;
		},
		error: function(error){
			console.log(error);
		}
	})
}

// Function to add passenger
function add_passenger(){
	var newRow = '<div class=row>'+
					'<div class="col-md-4">'+
						'<div class="form-group label-floating">'+
							'<label class="control-label" style="font-weight: bold;">Name*</label>'+
							'<input type="text" class="form-control" style="text-transform:uppercase" required id="name'+passenger_number+'">'+
						'</div>'+
					 '</div>'+
					 '<div class="col-md-4">'+
					 	'<div class="form-group label-floating">'+
					 		'<label class="control-label" style="font-weight: bold;">Age*</label>'+
					 		'<input type="number" class="form-control" minlength="1" maxlength="3" required id="age'+passenger_number+'">'+
					 	'</div>'+
					 '</div>'+
					 '<div class="col-md-4">'+
					 	'<div class="form-group label-floating">'+
					 		'<label class="control-label" style="font-weight: bold;">Aadhar Card No.*</label>'+
					 		'<input type="text" class="form-control" id="aadhar'+passenger_number+'">'+
					 	'</div>'+
					 '</div>'+
				 '</div>';

	$('#container').append(newRow);
	passenger_number++;
}

// Function to continue after addition of passengers
function continue_after(){
	var name_array = new Array(); // Array to store names
	var age_array = new Array(); // Array to store ages
	var aadhar_array = new Array(); // Array to store aadhar card numbers
	for(var i=1; i<passenger_number; i++){
		var name_id = "name"+i;
		var age_id = "age"+i;
		var aadhar_id = "aadhar"+i;
		name_array.push(document.getElementById(name_id).value); // Append name in name array
		age_array.push(document.getElementById(age_id).value); // Append age in age array
		aadhar_array.push(document.getElementById(aadhar_id).value); // Append Aadhar Card No in array
	}
	
	// // print_passenger_table(name_array, age_array, aadhar_array);
	// passenger_table = create_passengers_table(name_array, age_array, aadhar_array);
	// //document.getElementById('passenger_table').innerHTML = passenger_table.innerHTML;
	// document.body.appendChild(passenger_table);
	
	// // var next_url = "{{ url_for('payment_details') ";
	// var pay_button = document.createElement('button');
	// pay_button.innerHTML = "Go to Payment";
	// pay_button.setAttribute("onclick", "go_to_payment_detail_page();");
	// document.body.appendChild(pay_button);
	
	// //  
	name_array_jstr = JSON.stringify(name_array); // Convert name array to string
	age_array_jstr = JSON.stringify(age_array); // Convert age array to string
	aadhar_array_jstr = JSON.stringify(aadhar_array); // Convert Aadhar card nNo array to string

	// Prepare data in JSON
	var data_to_send = {'name_array':name_array_jstr, 'age_array':age_array_jstr, 'aadhar_array':aadhar_array_jstr};
	$.ajax({
		type : "POST",
		url : "continue_to_payment",
		data : data_to_send,
		success : function(response) {
			if (response.success=='ok'){				
				all_passengers_table(name_array, age_array, aadhar_array);
			}			
		},
		error : function(error) {
			console.log(error);
		}
	})
}

// Add and show all passengers details
function all_passengers_table(name_array, age_array, aadhar_array) {
	passenger_table = create_passengers_table(name_array, age_array, aadhar_array);
	
	var pay_button = document.createElement('button');
	pay_button.innerHTML = ">>Payment";
	pay_button.setAttribute("onclick", "go_to_payment_detail_page();");
	document.body.appendChild(passenger_table);
	document.body.appendChild(pay_button);
}


function createTable(tableData) {
  var table = document.createElement('table');
  var tableBody = document.createElement('tbody');

  tableData.forEach(function(rowData) {
    var row = document.createElement('tr');

    rowData.forEach(function(cellData) {
      var cell = document.createElement('td');
      cell.appendChild(document.createTextNode(cellData));
      row.appendChild(cell);
    });

    tableBody.appendChild(row);
  });

  table.appendChild(tableBody);
  return table
  // document.body.appendChild(table);
}

// Create Passenger's table
function create_passengers_table(name_array, age_array, aadhar_array) {
	passenger_table = new Array();
	passenger_table[0] = ['Name', 'Age', 'Aadhar Card No.'];
	for(var i=0; i<name_array.length; i++) {
		passenger_table[i+1] = [name_array[i], age_array[i], aadhar_array[i] ];
	}

	return createTable(passenger_table)
}

// Function to print Passenger's details table
function print_passenger_table(name_array, age_array, aadhar_array) {
	var column_name_list = new Array('Sr No','Name', 'Age', 'Aadhar Card No.');
	var table_head = '';
	for(var i=0; i<column_name_list.length;i++){
		table_head = table_head + '<th>' + column_name_list[i] + '</th>';
	}

	var passenger_table = 	'<table>'+
								'<thead>'+
									table_head +
								'</thead>'+
								'<tbody>'+
								'</tbody>'+
							'</table>';
	document.getElementById('passenger_table').innerHTML = passenger_table;
}

// Function to render Payment Details
function go_to_payment_detail_page() {
	$.ajax({
		type : "POST",
		url : "/get_payment_details_address",
		success : function(response) {
			window.location.href = response.route;
		},
		error : function(error) {
			console.log(error);
		}
	})
}

// Function to make payment
function go_to_make_payment_page() {
	$.ajax({
		type : "POST",
		url : "/get_make_payment_address",
		success : function(response) {
			window.location.href = response.route;
		},
		error : function(error) {
			console.log(error);
		}
	})
}

function check_payment(ticket_amount){
	// Check for bank selected
	var selected_bank = document.getElementById('bank').value;
	if(selected_bank == ''){
		alert('Please select bank');
	}
	var entered_amount = document.getElementById('amount').value;
	if (entered_amount != ticket_amount) {
		alert('Please enter right amount !!!');
	}else{
		$.ajax({
			type: 'POST',
			url: 'generate_transaction_no',
			data: {
				'selected_bank': selected_bank,
				'entered_amount' : entered_amount
			},
			success: function(response){
				window.location.href = response.route;
			},
			error: function(error){
				alert(error);
			}
		});
		
	}

}

// This function creates Ticket
function download_ticket(filename) {
	let doc = new jsPDF('l', 'pt', 'a4');
  doc.fromHTML(document.getElementById('container') )
  doc.save(filename);
}