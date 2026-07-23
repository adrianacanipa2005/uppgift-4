Del 2 Undantagshantering med try/except (Kod + förklaring)
Skriv ett Python-program som:
Frågar användaren att skriva in ett tal
Delar 100 med det talet
Använder try/except för att hantera ZeroDivisionError
Använder try/except för att hantera ValueError



try:
    tal = int(input("Skriv ett tal: "))
    resultat = 100 / tal
    print("Resultatet är:", resultat)

except ZeroDivisionError:
    print("Du kan inte dela med 0.")

except ValueError:
    print("Du måste skriva ett tal.")


Förklaring:

Hur fungerar try/except?

try testar att köra koden. Om ett fel händer hoppar programmet till 
except och visar ett  felmeddelande istället för att krascha.


Varför är det bra att använda undantagshantering?

Det gör att programmet blir mer användarvänligt. Om användaren skriver fel, 
till exempel text istället för ett tal eller 0, kan programmet visa ett tydligt meddelande 
istället för att avslutas med ett fel.



