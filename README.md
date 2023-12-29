# Coding Challenge

## Aufgabe 1

Die Loesung zur `Aufgabe 1` befindet sich in der Datei `Aufgabe1.md`

## Aufgabe 2

Problem: Datenschutzkonfome Implementierung fuer Wissensaufbau zu LLama-2 

Loesung: Chat Applikation mit Interface 

Um die Applikation zu starten brauchen Sie folgende Commands in der CLI einfuegen. 
Vorausgesetzt Sie haben Python3.11 installiert, sollte dies laufen und die Applikation oeffnen.

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

In dieser Applikation sollte dann ein Chatfenster offen sein, in dem Sie ihre Fragen zu LLama 2 stellen koennen.

## TODO's

- TODO: REST API aufbau mit Post endpoint ?
- TODO: Docker Container
- TODO: Emebddings in Container updaten ?
- TODO: Healthchecks implementieren ...
