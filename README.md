# logging-am-weltfrauentag
Logging mit Env Vars am Weltfrauentag

# Aufgabe
Erstelle eine http API, entweder mit Node (express/nestjs) oder Python (fastapi), die folgende Routen bereitstellt:

- (GET) /info
- (GET) /debug
- (GET) /error
- (GET) /fatal

Definiert eine ENV Variable für LOG_LEVEL, die folgende Werte enthalten kann:
- INFO, DEBUG, ERROR oder FATAL

Implementiert in den Routen, jeweils eine Funktion, die entsprechend des gesetzten Loglevels eine Logmeldung ausgibt.
Beispiel:
Wenn der Loglevel auf INFO gesetzt ist, dann soll die (GET) /info Route eine Info-Logmessage ausgeben.


2024-03-08T11:10:35.689Z info: This is an info message
analog dazu die anderen Loglevel:

2024-03-08T11:10:35.687Z error: This is an error message
2024-03-08T11:10:35.688Z debug: This is a debug message
2024-03-08T11:10:35.688Z fatal: This is a fatal message

Die fertige Anwendung bitte in ein GIT Repo pushen und den Link zu Eurem Repo hier abgeben.

# Config
./setup.sh

# Execute
./execute.sh

