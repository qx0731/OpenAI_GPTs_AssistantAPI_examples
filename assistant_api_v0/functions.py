import os
import time
from datetime import datetime, timedelta
import random
import json

def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "result_label": "from_file", 
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)

def book_flight(loc_origin, loc_destination, date, airline):
    """Book a flight based on flight information."""

    # Example output returned from an API or database
    book_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "result_label": "from_file", 
        "datetime": date,
        "airline": airline, 
        "bookstatus": 'Success'
    }

    return json.dumps(book_info)

def file_complaint(name, email, text):
    """File a complaint as a customer."""

    # Example output returned from an API or database
    complaint_info = {
        "customername": name,
        "customeremail": email,
        "result_label": "from_file", 
        "complaintcontent": text, 
        "submitstatus": 'Success'
    }
    return json.dumps(complaint_info)