# PAII-WLAN_Roaming_analysis_Tool

Dieses Tool soll der Analyse von Verzögerungen bei WLAN-Roaming dienen. Um das Skript zu Nutzen, muss dieses lediglich gestartet werden und in sich in dem gewünschten Bereich bewegt werden. Sobald ein Roaming-Vorgang erkannt wird, terminiert das Programm automatisch nach 5 weiteren Sekunden und speichert die Ergebnisse in die pings.csv Datei. 


# Funktionsweise

Bei start des Skripts wird 10x/Sekunde die BSSID des aktuell verbundenen APs ausgelesen und ausgegeben. Parallel wird 20x/Sekunde eine zuvor eingegebene IP-Adresse gepingt.

Das Ergebniss jedes einzelnen Pings wird in ein Array gespeichert und nach Abschluss der Messungen in eine Datei geschrieben.

Sobald der erste Thread eine neue BSSID erkennt, wird eine Flag in dem zweiten Ping-Threat gesetzt, welche einen Eintrag in dem Array hinterlässt, dass eine neue BSSID erkannt wurde.

Nach erkanntem Roaming-Vorgang geht der erste Threat in den Counting-Modus, in welchem 50 letzte BSSID auslesungen vorgenommen werden, bevor beide Threats terminieren und die Messwerte aus dem Array in die Datei pings.csv geschrieben werden.


# Disclaimer

Das Skript läuft aktuell ausschließlich auf MacOS-Systemen. Durch Anpassung des Befehls zur ermittlung der BSSID kann es jedoch auf jeder Plattform betrieben werden.
