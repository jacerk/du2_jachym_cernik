import csv
import os


# promenne kde se ukladaji hodnoty
calenweek = []
calenyear = []
year = []
max_flow_rate = []
min_flow_rate = []
week_sum = 0
year_sum = 0
counter = 0
theYear = 0
day_amount = 0
week_average = 0



try:
    with open("vstup.csv", encoding="utf-8") as vstup,\
        open("vystup_tyden.csv", "w", newline="", encoding="utf-8") as vystup_tyden,\
        open("vystup_rok.csv", "w", newline="", encoding="utf-8") as vystup_rok:
        reader = csv.reader(vstup, delimiter = ",")
        writer_week = csv.writer(vystup_tyden)
        writer_year = csv.writer(vystup_rok)
        

        # program nenacha skript jet pokud je vstup prazdny
        if os.path.getsize('vstup.csv') == 0:
            print("Soubor je prazdny")
            quit()
            
        for row in reader:
            if len(row) != 4:
                raise Exception("spatny pocet sloupcu")
           
           
            # vytrideni datumu prez list 
            string = row[2]
            year=[]
            for letter in string:
                year.append(letter)
            for i in range(6):
                del year[0]
            for i in range(0, len(year)): 
                year[i] = int(year[i])
            s=[str(i) for i in year]
            theYear = int(("".join(s)))


            # rozeznani prestupnich roku 
            if theYear % 4 == 0:
                day_amount = 366
            else:
                day_amount = 365
                
            # vypocet prumeru tydne 
            if len(calenweek) == 0:
                week_ID = row[0]
                week_date = row[2]
                
                
            if len(calenweek)<7:
                calenweek.append(float(row[3]))
                

            # vytvoreni radku 
            if len(calenweek)==7:
                for i in calenweek:
                    week_sum += i
                week_average = round(week_sum/7,4)
                outrow = [week_ID,week_date,week_average]
                writer_week.writerow(outrow)
                calenweek.clear()
                week_sum = 0
            
            # vypocet prumeru roku 
            if len(calenyear) == 0:
                year_ID = row[0]
                year_date = str(row[2])

            # vytrideni datumu prez list 
            if len(calenyear)<day_amount:
                calenyear.append(float(row[3]))
                counter += 1

            if len(calenyear)==day_amount:
                year = row[2] 
                for i in calenyear: 
                    year_sum += i
                year_average =round(year_sum/day_amount,4)
                outrow1 = [year_ID,year_date,year_average]
                writer_year.writerow(outrow1)
                calenyear.clear()
                year_sum = 0
       
            # maxium - minimum 
            if len(max_flow_rate)==0 and len(min_flow_rate) == 0:
                max_flow_rate=[row[2] , row[3]]
                min_flow_rate=[row[2] , row[3]]
            if float(max_flow_rate[1]) < float(row[3]):
                max_flow_rate = [row[2], row[3]]
            if float(min_flow_rate[1]) > float(row[3]):
                min_flow_rate = [row[2], row[3]]
    
            # je vytvoren list na uchovani prutokovych hodnot ktery je nasledne roztrideny funkci sort a pak nasledne indexovan pro hodnoty
        print("nejv??t???? denn?? prutok byl {Q} v den: {date}". format(Q = max_flow_rate[1], date = max_flow_rate[0]))
        print("nejmen???? denn?? prutok byl {Q} v den: {date}". format(Q = min_flow_rate[1], date = min_flow_rate[0]))
            #values.append(float(flow_rate)) 
        
        if len(calenweek)!=7:
                for i in calenweek:
                    week_sum += i
                week_average = round(week_sum/len(calenweek),4)
                outrow2 = [week_ID,week_date,week_average]
                writer_week.writerow(outrow2)
                week_sum = 0
           
except FileNotFoundError:
    print("Vstupn?? soubor se nepoda??ilo na????st" )
except PermissionError:
    print("Program nem?? p????stup k z??pisu v??stupn??ch soubor??.")