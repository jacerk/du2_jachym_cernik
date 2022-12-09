import csv
import os


# promenne kde se ukladaji hodnoty
flow_values = []
calenweek = []
calenyear = []
year = []
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
        
        if os.path.getsize('vstup.csv') == 0:
            raise Exception("Soubor je prazdny")
            
        
        for row in reader:
            if len(row) != 4:
            
                raise Exception("spatny pocet sloupcu")
    
        

            # vypocet prumeru tydne 
            if len(calenweek) == 0:
                week_ID = row[0]
                week_date = row[2]
                
            if len(calenweek)<7:
                calenweek.append(float(row[3]))
            



           
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

            if theYear % 4 == 0:
                day_amount = 366
                print(theYear)
            else:
                day_amount = 365
            

            if len(calenyear)<day_amount:
                calenyear.append(float(row[3]))

                
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
            flow_values.append(float(row[3]))

        # je vytvoren list na uchovani prutokovych hodnot ktery je nasledne roztrideny funkci sort a pak nasledne indexovan pro hodnoty 
        flow_values.sort(key = float)
        print("největší denní prutok byl ", flow_values[len(flow_values)-1])  
        print("nejmenší denní prutok byl " ,flow_values[0])
            #values.append(float(flow_rate)) 
        print(counter)
        if len(calenweek)!=7:
                for i in calenweek:
                    week_sum += i
                week_average = round(week_sum/len(calenweek),4)
                outrow2 = [week_ID,week_date,week_average]
                writer_week.writerow(outrow2)
                week_sum = 0
        

        
except FileNotFoundError:
    print("Vstupní soubor se nepodařilo načíst")
except PermissionError:
    print("Program nemá přístup k zápisu výstupních souborů.")