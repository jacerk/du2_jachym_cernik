Program slouží k převzetí dát denních průtoku. A jejím výstupem jsou dva .csv dokumenty, jeden má týdenní průměry za celou škálu dát a druhý roční.


Program má v počátku definované proměnné a listy které jsou potřeba k ukládání hodnot a k uskutečnění procesů potřebných k výpočtu průměru. 

Následně jsou otevřeny všechny nutné soubory, vstup.csv jsou úvodní data a výstup rok a týden jsou nově vytvořené soubory pro uchování výstupu. Spolu s tím jsou definovány writery. 

Funkce try je implementována za účelem nalezení chyb jako je FileNotFound a 

Následně začíná for loop pro každý řádek. Program pracuje na stejné bázi jak pro týdenní tak i pro měsíční průměry. 
Je zadán list ve kterém se ukládají hodnoty s každého řádku pro určitou dobu (týden nebo rok) nejprve jsou ale prevzané hodnoty pro datum a ID kterého budou následně identifikovat danou dobu ve výstupu. Data průtoku jsou připojená k listu pomocí append. 
Listy se jmenují calenweek a calenyear. Když dojde na den naší určitě doby tudíž když calenweek == 7 tak se v for loop sečtou hodnoty do jedné které jsou následně vydělený do průměru. A pak už se jenom použije writer a data jsou zapsaná po 7mi nebo 365 dny do souborů. 


Maximum a minimum je počítané pomocí funkce sort s key float která seřadí list podle velikosti a pak jsou hodnoty extrému nalezeny podle hraničních indexů.



