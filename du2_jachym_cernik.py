import csv


# promenne a listy kde se ukladaji hodnoty
flow_values = []
calenweek = []
calenyear = []
week_sum = 0
year_sum = 0


week_average = 0

try:
    with open("vstup.csv", encoding="utf-8") as vstup,\
        open("vystup_tyden.csv", "w", newline="", encoding="utf-8") as vystup_tyden,\
        open("vystup_rok.csv", "w", newline="", encoding="utf-8") as vystup_rok:
        reader = csv.reader(vstup, delimiter = ",")
        writer_week = csv.writer(vystup_tyden)
        writer_year = csv.writer(vystup_rok)
        for row in reader:
            
            # try vyzkousi jestli jsou data v poradku na prvnim radku
            try:
                firstRow = float(row[3])
            except ValueError:
                print("Na prvním řádku vstupního souboru jsou chybně zadána data")

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
                year_date = row[2]
            if len(calenyear)<365:
                calenyear.append(float(row[3]))
                
            if len(calenyear)==365:
                for i in calenyear: 
                    year_sum += i
                year_average =round(year_sum/365,4)
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
except FileNotFoundError:
    print("Vstupní soubor se nepodařilo načíst")
except PermissionError:
    print("Program nemá přístup k zápisu výstupních souborů.")