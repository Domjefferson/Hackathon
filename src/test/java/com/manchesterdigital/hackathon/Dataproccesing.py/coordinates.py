import requests
import csv
from OSGridConverter import latlong2grid
import os

with open('parking.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count +=1
        else:
            # print(row[8] +', manchester , UK', )
            responce = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address=' + row[8]+ ', manchester, uk&key=AIzaSyCAcR729aS6d0hfZGpLWsDBBuK1X0hFpB8')

            lattitude = responce.json()['results'][0]['geometry']['location']['lat']
            longtitude =(responce.json()['results'][0]['geometry']['location']['lng'])

            line_count +=1


            grid = latlong2grid(lattitude,longtitude)



            grifref= [(str(grid)[0:2] +str(grid.E)[1:-2] + str(grid.N)[1:-2])]
            # print(grifref)
                    # p= csv.writer(grifref)
            with open("output.csv",'a') as finalfile:
                wr = csv.writer(finalfile, dialect='excel')
                wr.writerow(grifref)


















