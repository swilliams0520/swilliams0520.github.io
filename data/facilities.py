# -*- coding: utf-8 -*-
import csv

sum_of_facilities = 0
print("<h2>Oregon Cannabis Facilities</h2>")
print("<p>Applicants on this list have been approved for a recreational marijuana license in the state of Oregon.</p>")
print("<div>")
with open('facilities.csv') as csvfile:
    facilityreader = csv.reader(csvfile, delimiter=',')
    for line in facilityreader:
        row = line
        number = row[0]
        name = row[1]
        business_name = row[2]
        type = row[3]
        active = row[4]
        county = row[5]
        retail_delivery = row[6]
        medical_grade = row[7]
        hemp = row[8]

        print("<div class='facility'>")
        print("<h3>%s (%s)</h3>" % (business_name, county))
        print("<div>")
        print("<p>License Type: %s</p>" % (type))
        print("<h4>Registration: %s</h4>" % (name))
        print("<p>License Number: %s</p>" % (number))

        if hemp == 'Yes':
            print("<p><em>Hemp Certification</em></p>")

        if medical_grade == 'Yes':
            print("<p><em>Medical Certification</em></p>")

        if retail_delivery == 'Yes':
            print("<p><em>Retail Delivery Certification</em></p>")


        print("</div>")
        print("</div>")

        sum_of_facilities = sum_of_facilities + 1

print("</div>")
print("Number of Oregon Recreational Cannabis Operators:")
print(sum_of_facilities)
