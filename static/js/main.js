;(function () {
    	var fullHeight = function() {
		//if ( !isMobile.any() ) {
			$('.js-fullheight').css('height', $(window).height());
			$(window).resize(function(){
				$('.js-fullheight').css('height', $(window).height());
			});
		//}
	};
	$(function(){
		fullHeight();
	});
});

// window.addEventListener('load', () => {

// })

// function book(e) {
// 	e.preventDefault();
// 	const formData = new FormData(e.target);
// 	console.log("formData", formData)
// 	return false;
// }

var book = () => {
	// debugger;
	//document.getElementById('bookGo').disabled = true;
	var name = document.getElementById('name').value;
	var email = document.getElementById('email').value;
	var sourcePlace = document.getElementById('sourcePlace').value;
	var destinationPlace = document.getElementById('destinationPlace').value;
	var noOfPassengers = document.getElementById('noOfPassengers').value;
	var date = document.getElementById('date').value;
	var departureTime = document.getElementById('departureTime').value;

	const bookingData = {
		"name": name,
		"email": email,
		"sourcePlace": sourcePlace,
		"destinationPlace": destinationPlace,
		"noOfPassengers": noOfPassengers,
		"date": date,
		"departureTime": departureTime
	}

	fetch('/book-ticket', {method:"POST", body: JSON.stringify(bookingData)})
	.then((res) => {
		if (res.status == 200) {
			showSnackbar('Ticket booked successfully!');
			// location.href = "/thank-you";
			clearForm();
		} else {
			showSnackbar('Something went wrong! Please try again!');
			clearForm();
		}
	})
	.catch((err) => {
		showSnackbar('Something went wrong! Please try again!');
		clearForm();
	})
	return false;
}

var clearForm = () => {
	document.getElementById('name').value = '';
	document.getElementById('email').value = '';
	document.getElementById('sourcePlace').value = '';
	document.getElementById('destinationPlace').value = '';
	document.getElementById('noOfPassengers').value = '';
	document.getElementById('date').value = '';
	document.getElementById('departureTime').value = '';
}

var fetchTicketTable = () => {
	var ticketTable = document.getElementById('ticketTable');
	return ticketTable;
}

var printTicket = (data) => {
	var ticketTable = fetchTicketTable();
	ticketTable.className = 'showTable';
	
	var pnrRecords = data['data']['pnrRecords'];
	pnrRecords = pnrRecords.join(" and ")
	// console.log(pnrRecords)
	// for(k=0; k< pnrRecords.length; k++) {
	// 	console.log(pnrRecords[k])
	// }

	var tableJson = {
		"Passenger Name": data['data']['name'],
		"Email Id": data['data']['email'],
		"Total Passenger(s)": data['data']['noOfPassengers'],
		"Departure Date": data['data']['date'],
		"From Place": data['data']['sourcePlace'],
		"To Place": data['data']['destinationPlace'],
		"Departure Time": data['data']['departureTime'],
		"Your PNR Numbers": pnrRecords,
	}

	for (i=0;i < ticketTable.rows.length; i++) {
		var oCells = ticketTable.rows.item(i).cells;
		// console.log(oCells)
		var cellLength = oCells.length;
		for(var j = 0; j < cellLength; j++){
			var cellVal = oCells.item(j).innerHTML;
			var localName = oCells.item(j).localName;
			
			if (localName === 'th') {
				nextValue = tableJson[cellVal];
			}

			if (localName === 'td') {
				oCells.item(j).innerHTML = nextValue;
			}
		 }
	}
}

var searchTicketByPNR = () => {
	document.getElementById("submitButton").disabled = true;
	var ticketTable = fetchTicketTable();
	ticketTable.className = ' ';
    var pnrNumber = document.getElementById('pnrNumber').value;
	const pnrNumberRecord = {
		"pnrNumber": pnrNumber
	}

	fetch('/search-ticket', {method:"POST", body: JSON.stringify(pnrNumberRecord)})
	.then(async (res) => {
		if(res.status === 200) {
			let data = await res.json();
			printTicket(data);
		} else if (res.status === 500) {
			showSnackbar('Something went wrong! Please try again later.');
		} else if (res.status === 204) {
			showSnackbar('Ticket Not Found With PNR ' + pnrNumber);
		}
		document.getElementById("submitButton").disabled = false;
	})
	.catch((err) => {
		showSnackbar('Something went wrong! Please try again later.');
		document.getElementById("submitButton").disabled = false;
	});
    return false;
}

window.onload = () => {
	// (B1) MIN SELECTABLE DATE IS TODAY
	// let datepick = document.getElementsByName("date")[0];
	// datepick.min = new Date().toISOString().split("T")[0];
  
	// (B2) ENABLE FORM
	document.getElementById("submitButton").disabled = false;
};

var showSnackbar = (text) => {
	var slack = document.getElementById('snackbar');
	slack.textContent = text;
	slack.className = 'show';
	setTimeout(() => {
		slack.className = slack.className.replace('show', '');
	}, 3000);
}

var burgerMenu = function() {

	$('.js-fh5co-nav-toggle').on('click', function(event){
		event.preventDefault();
		var $this = $(this);

		if ($('body').hasClass('offcanvas')) {
			$this.removeClass('active');
			$('body').removeClass('offcanvas');	
		} else {
			$this.addClass('active');
			$('body').addClass('offcanvas');	
		}
	});
};

$(function(){
	burgerMenu();
});
  