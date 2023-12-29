# LegalGPT: Ein LLM-basiertes Codingprojekt für juristische Fragen

1. Projektfrage

Ausgehend von einem LLM-Projekt auf deutscher Sprache fällt mir schnell ein "LegalGPT" ein: Ein LLM, welches sowohl für in der deutschen Sprache unerfahrene als auch juristisch unerfahrene Nutzer ein Interface für juristische Fragen ermöglicht.

Dies ist ein ambitioniertes Projekt, das definitiv seinen Use-Case hat. Fragen wir uns nicht alle, ob wir zu viel Miete in Berlin bezahlen? Darf mein Nachbar wirklich so laut und so lange Techno pumpen?

2. Projektziel

Das Ziel ist klar definiert: Gegeben gewisser Umstände und Tatbestände wollen wir wissen, wie wir etwas legal auslegen oder als illegal bewerten können; eine klassische Argumentation auf Grundlage von juristischen Annahmen und Konsequenzen (Paragraphen). Dieses legale Framework, welches sich in Deutschland kodifiziert hat - mit vielen Ausnahmen (siehe Probleme) - könnte sehr gut von einem LLM verstanden und genutzt werden, um Anwälten zu helfen, ihre Argumente zu verbessern, Verteidigungen nachzuvollziehen oder generell bessere Entscheidungen zu treffen.

3. Lösungsansatz

Die Lösung besteht darin, ein LLM auf Grundlage von juristischen Hausarbeiten und Bestlösungen zu trainieren. Wir haben klassische Prompts (Aufgaben) und die Lösung (die optimalen Antworten) mit jahrelanger Erfahrung und Daten, die wir in Deutschland durch Anfrage oder Kauf von Hausarbeiten erlangen können. Diese Daten könnten eine solide Grundlage bieten. Sie müssten lediglich aufbereitet und strukturiert werden, um als Trainingsdatensatz verwendet zu werden. Hierbei ist die Anonymisierung von Namen, das Entfernen gewisser Daten und das Berücksichtigen von Fairness gegenüber benachteiligten Gruppen wichtig.

Als Foundation-Modell wäre z.B. GPT-3 Turbo geeignet. Dieses könnten wir feintunen, vorausgesetzt, der Use-Case entspricht den Lizenzvereinbarungen. Feintuning bedeutet in den meisten Fällen, das LLM-Netzwerk um einige Transformer-Layer zu erweitern, die an unsere Daten angepasst werden. Eine Alternative wäre das Umgewichten der Foundation-Modell-Gewichte auf Basis unserer Bedürfnisse (Daten/Prompts). Nachdem wir die richtigen Hyperparameter (Lernrate, Temperatur, Batch-Größe usw.) eingestellt haben, könnten wir mit dem Monitoring des Trainings fortfahren.

4. Entscheidende Metriken für das Training

Beim Trainieren des Modells sind folgende Metriken entscheidend:

    Genauigkeit (Accuracy): Wie oft liefert das Modell die korrekte Antwort oder Lösung im Vergleich zu einem Goldstandard?
    Precision und Recall: Wie oft ist eine gelieferte juristische Information korrekt (Precision), und wie viele relevante juristische Informationen erkennt das Modell (Recall)?
    F1-Score: Kombiniert Precision und Recall in einer einzigen Metrik.
    Verständlichkeit und Kohärenz (Coherence): Beurteilt, wie klar und logisch konsistent der generierte Text ist.
    Spezifität und Relevanz: Bewerten, wie spezifisch und relevant die Antworten des Modells sind.
    Robustheit: Einschätzung der Fehleranfälligkeit und Generalisierbarkeit des Modells.
    Effizienz: Bewertung von Trainingszeit, Inferenzzeit und Ressourcenverbrauch.
    Fairness und Verzerrung (Bias): Sicherstellen, dass das Modell fair und unvoreingenommen ist und systematische Verzerrungen minimiert.

5. Bewertung und Iteration

    Qualitätssicherung: Testen des Modells mit realen juristischen Fragen und Fällen zur Bewertung seiner Genauigkeit und Zuverlässigkeit.
    Iteratives Lernen: Kontinuierliche Verbesserung des Modells basierend auf Feedback und Ergebnissen.

6. Ethik und Compliance

    Datenschutz: Beachtung von Datenschutzgesetzen und -richtlinien, insbesondere beim Umgang mit sensiblen Daten.
    Fairness und Verzerrung: Bewusstsein und Minimierung von Verzerrungen im Modell.
    Verantwortungsvoller Einsatz: Sicherstellung, dass die Nutzung des Modells ethisch vertretbar und gesetzlich zulässig ist.

7. Zusätzliche Tipps:

    Expertise: Zusammenarbeit von Juristen und Datenwissenschaftlern, um eine Brücke zwischen juristischer Expertise und technischem Know-how zu schlagen.
    Community und Ressourcen: Nutzung von Open-Source-Ressourcen und der Community für Unterstützung und Leitfäden beim Training von LLMs. Nutzung von der juristischen Studierdenschaft zur Schaffung eines OSS Netzwerks zur verbesserung dieses Dienstes.
    Markt: Viele LLMS koennten als unterscheidliceh Produkte entwickelt und verkauft werden - sowohl kommerziell als auch Non-Profit. Data Scientists sind oftmals auch in der Lage diese Business Development Bruecke auch zu schlagen weil sie ihre Anwendung besser kennen als Software Engineers.


