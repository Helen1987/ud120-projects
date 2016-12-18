#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl"))


print "people count is", len(enron_data)
print "features amount is ", len(enron_data.values()[0])

pois = [person for person in enron_data.values() if person["poi"] == 1]
print "count poi ", len(pois)

james = [person for person in enron_data.keys() if person.startswith("Prentice James".upper())]

print james
print "James Prentice has ", enron_data[james[0]]["total_stock_value"], "stocks"

print "messages from Wesley Colwell to person of interest", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "the value of stock options exercised by Jeffrey K Skilling" , enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Kenneth Lay money", enron_data["LAY KENNETH L"]["total_payments"]
print "Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Andrew Fastow money", enron_data["FASTOW ANDREW S"]["total_payments"]

quantifiedsalaries = [person for person in enron_data.values() if person["salary"] != "NaN"]
print "people with quantified salaries ", len(quantifiedsalaries)

quantifiedemails = [person for person in enron_data.values() if person["email_address"] != "NaN"]
print "people with quantified salaries ", len(quantifiedemails)

hasnopayments = [person for person in enron_data.values() if person["total_payments"] == "NaN"]
print "Count of people without total payments info", len(hasnopayments)

print "% to a whole", len(hasnopayments)/float(len(enron_data))

poihasnopayments = [poi for poi in pois if poi["total_payments"] == "NaN"]
print "Count of POI without total payments info", len(poihasnopayments)

print "% to a whole", len(poihasnopayments)/float(len(pois))

stocks = [person["exercised_stock_options"] for person in enron_data.values() if person["exercised_stock_options"] != "NaN"]
print "min stock is", min(stocks)
print "max stock is", max(stocks)
