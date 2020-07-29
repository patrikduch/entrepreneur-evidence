

# dependencies
django 3.0.4


# admin credentials
admin
duch0704


# Server startup
python manage.py runserver 


# Run migrations
python manage.py migrate 


# Package installation
pipenv install requests



Formulář

Vytvoření webové aplikace v Djangu umožňující vyplnit a uložit formulář.

Web
Obsahuje pouze hlavní stranu, která zobrazuje formulář.

Formulář
Datový model formuláře je zobrazený v administraci. V administraci nelze přidat nový záznam, nové záznamy se přidávají pouze na webové části.

Položky formuláře
Jméno: varchar(255), povinný
E-mail: varchar(255), nepovinný, validace E-mail
IČO: varchar(8), povinný, validace, ověření podle ARES

Odevzdání
Součástí projektu bude soubor readme, kde bude popis instalace a použité verze knihoven a Pythonu. Projekt lze odeslat zabalený v zipu nebo odesláním odkazu na git. Databáze nemusí být součástí projektu - instalace bude provedena příkazem migrate. 