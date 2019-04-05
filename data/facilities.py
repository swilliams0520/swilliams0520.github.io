# -*- coding: utf-8 -*-
import csv

sum_of_facilities = 0
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
        print("<h2>%s</h2>" % (business_name))
        print("<div>")
        print("<h3>%s in %s County</h3>" % (type, county))

        if hemp == 'Yes' and medical_grade == 'Yes' and retail_delivery == 'Yes':
            print("<p><em>Hemp, Medical and Retail Delivery Certification.</em></p>")
        elif hemp == 'Yes' and medical_grade == 'Yes':
            print("<p><em>Hemp and Medical Certication.</em></p>")
        elif hemp == 'Yes' and retail_delivery == 'Yes':
            print("<p><em>Hemp and Retail Delivery Certification.")
        elif retail_delivery == 'Yes' and medical_grade =='Yes':
            print("<p><em>Medical and Retail Delivery Certification.")
        elif hemp == 'Yes':
            print("<p><em>Hemp Certification.</em></p>")
        elif medical_grade == 'Yes':
            print("<p><em>Medical Certification.</em></p>")
        elif retail_delivery == 'Yes':
            print("<p><em>Retail Delivery Certification.</em></p>")
        else:
            print("<p><em>No additional certifications.</em></p>")


        print("</div>")
        print("</div>")

        sum_of_facilities = sum_of_facilities + 1

print("</div>")
print("Number of Oregon Recreational Cannabis Operators:")
print(sum_of_facilities)
