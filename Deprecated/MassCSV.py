import os
import csv
import pandas as pd

###DEPRECATED BY CSV FORMATTER



def masscsvformatter(filename,olm):
    print("Formatting " + filename)
    page4.update_idletasks()
    file = open(os.path.join(os.getcwd(),filename))
    outpname = filename.split('.')[0] + ".csv"
    outpath = os.path.join(os.getcwd(),outpname)
    reader = csv.reader(file)
    x = 1
    if(olm == 1):
        for i, row in enumerate(reader):
            if i == 8:
                length = int(len(row[0].split())) - 1
                writer = csv.writer(open(outpath, "w"), delimiter = ',', lineterminator='\n')
                header = ['year','day','hour']
                header.extend(list(range(1,length)))
                writer.writerow(header)
            if i==9:
                new_row = []
                if x == 1:
                    for j in range(1,len(filter(None,str(row).split(" "))[2:]) + 1):
                        new_row.append("Rec " + str(j))
                    loclist = pd.DataFrame(new_row)
                    new_row = []
                    x = 0
                for j in filter(None,str(row).split(" "))[2:]:
                    new_row.append(float(j.strip("']")))
                loclist['x'] = new_row
            if i==10:
                new_row = []
                for j in filter(None,str(row).split(" "))[2:]:
                    new_row.append(float(j.strip("']")))
                loclist['y'] = new_row
                locname = filename + "_Locations.csv"
                loclist.to_csv(locname)

            if i>15 and row[0] is not "":
                year = row[0].split()[0]
                day = row[0].split()[1]
                hour = row[0].split()[2]
                columns = []
                new_row = [year,day,hour]
                length = int(len(row[0].split()))
                for j in range(3,length):
                    value = float(row[0].split()[j])
                    if value is not "":
                        columns.append(value)
                new_row.extend(columns)
                writer = csv.writer(open(outpath, "a+"), delimiter = ',', lineterminator='\n')
                writer.writerow(new_row)
    else:
        txt_file = filename
        csv_file = outpath
        in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
        out_csv = csv.writer(open(outpath, 'wb'))
        out_csv.writerows(in_txt)