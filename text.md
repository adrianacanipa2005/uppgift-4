Del 1 – Skillnaden mellan feltyper (Textbaserad förklaring)
Förklara skillnaden mellan dessa tre feltyper i Python. Ge ett enkelt kodexempel på varje feltyp.



#Syntaxfel       
Ett syntaxfel uppstår när Python inte förstår koden eftersom den är skriven på fel sätt. Programmet kan inte starta.
for i in range(5)
    print(i) # Saknar kolon (:) efter for-satsen.

#Logiskt fel
Ett logiskt fel innebär att programmet körs utan felmeddelande, men resultatet blir fel eftersom logiken är fel.
x = 5
if x == 4:
    print("Hej") #Programmet fungerar, men villkoret är fel

#Runtime-fel (exekveringsfel)
Ett runtime-fel innebär när programmet startar men ett fel inträffar under körningen. Då avbryts programmet om felet inte hanteras.

tal = int("hej") # Går inte att göra om texten "hej" till ett heltal.



Del 3 – Pseudokod
Skriv pseudokod (inte Python-kod!) för ett program som:


Fråga användaren efter sin ålder

Om användaren inte skriver ett tal
    Skriv "Fel! Du måste skriva ett tal."

Annars om åldern är 18 eller mer
    Skriv "Du är vuxen"

Annars om åldern är mellan 13 och 17
    Skriv "Du är tonåring"

Annars
    Skriv "Du är barn"


Del 4 - Reflektion

1. Varför är det användbart att skriva pseudokod innan man skriver riktig kod?
Jag tycker att pseudokod är bra eftersom man kan planera hur programmet ska fungera 
innan man börjar skriva riktig kod. Det blir lättare att förstå vad man ska göra.

2. Hur hjälper planering med pseudokod att minska antalet fel?
När man planerar först blir det lättare att hitta misstag innan man börjar koda. Då slipper man ändra lika mycket senare och koden blir enklare att skriva.

3. Vad har du lärt dig från den här aktiviteten om felsökning och planering?

Jag har lärt mig skillnaden mellan syntaxfel, logiska fel och runtime-fel, och hur man kan hitta och rätta dem. Jag har också lärt mig att pseudokod och planering gör det enklare att skriva kod eftersom man tänker igenom lösningen innan man börjar programmera. Det gör att man undviker fler misstag och det blir lättare att felsöka om något inte fungerar. Jag har också lärt mig att använda try/except för att hantera fel så att programmet inte kraschar när användaren skriver in fel värde.
