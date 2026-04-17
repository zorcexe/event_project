# Pull Requests – Grundlagen und Vorgehensweise

## 1. Ziel dieses Dokuments

Dieses Dokument erklärt die grundlegende Arbeitsweise mit Pull Requests (PR) am Beispiel des Projekts
**[https://github.com/zorcexe/event_project](https://github.com/zorcexe/event_project)**.

Es richtet sich an Projektteilnehmende, die Änderungen beitragen möchten, ohne direkten Schreibzugriff auf das Hauptrepository zu besitzen.

---

## 2. Begriffserklärung: Pull Request

Ein **Pull Request** ist ein formalisierter Vorschlag, Änderungen aus einem eigenen Repository (Fork) in das zentrale Projekt (Main Repository) zu übernehmen.

Der Maintainer prüft diese Änderungen und entscheidet über:

* Annahme (Merge)
* Anpassung (Review-Kommentare)
* Ablehnung

**Wichtiger Hinweis:**
Ein Pull Request ist **kein Bestandteil von Git selbst**, sondern eine Funktion von Plattformen wie GitHub, Bitbucket oder GitLab.
Git stellt lediglich die technischen Grundlagen bereit, also insbesondere Commits, Branches und Merges.

---

## 3. Rollen

* **Maintainer**
  Verantwortlich für das Hauptrepository und die Integration von Änderungen.

* **Beitragende (Kollegen / Contributors)**
  Entwickeln neue Features oder Verbesserungen und schlagen diese per Pull Request vor.

---

## 4. Grundprinzip (Workflow)

```text
Main Repository (event_project)
        ↓ Fork
Eigenes Repository (Fork)
        ↓ Änderungen
Feature-Branch
        ↓ Pull Request
Main Repository
```

---

## 5. Schritt-für-Schritt-Anleitung

### 5.1 Fork erstellen

1. Öffnen Sie das Hauptrepository:
   [https://github.com/zorcexe/event_project](https://github.com/zorcexe/event_project)

2. Klicken Sie oben rechts auf **„Fork“**

3. Es wird eine Kopie des Repositories in Ihrem(!) eigenen GitHub-Account erstellt

### 5.2 Repository klonen

In diesem Schritt wird das geforkte Repository von GitHub auf den lokalen Rechner kopiert.
Erst dadurch können Sie lokal am Code arbeiten und Änderungen vornehmen.

```bash
git clone https://github.com/<ihr-username>/event_project.git
cd event_project
```

* `git clone` lädt das Repository inklusive aller Dateien und Versionshistorie herunter
* `cd event_project` wechselt in das Projektverzeichnis, in dem Sie weiterarbeiten



### 5.3 Feature-Branch erstellen

Bevor Sie mit der eigentlichen Entwicklung beginnen, sollten Sie einen **eigenen Branch** anlegen.
Ein Branch ist ein separater Arbeitszweig innerhalb des Repositories. Dadurch arbeiten Sie nicht direkt auf `main`, sondern isoliert von der Hauptentwicklung.

Das ist aus mehreren Gründen wichtig:

* Änderungen bleiben thematisch getrennt
* mehrere Arbeiten können parallel durchgeführt werden
* der Pull Request wird übersichtlicher und leichter prüfbar
* die Hauptentwicklung wird nicht unnötig mit Zwischenständen belastet

Direktes Arbeiten auf `main` ist problematisch, weil dort idealerweise nur geprüfter und stabiler Stand liegen sollte. Ein eigener Feature-Branch schafft daher Ordnung, Nachvollziehbarkeit und Sicherheit.

Arbeiten Sie deshalb **niemals direkt auf `main`**.

```bash
git checkout -b feature/feature1
```

Mit diesem Befehl wird ein neuer Branch erstellt und sofort aktiviert. Ab diesem Zeitpunkt erfolgen Ihre Änderungen in diesem Branch.

#### Zwischen Branches wechseln

Während der Arbeit kann es notwendig sein, zwischen Branches zu wechseln, z.B. um:

* den aktuellen Stand von `main` zu prüfen
* neue Änderungen zu holen
* an einem anderen Feature weiterzuarbeiten

Wechsel zurück auf `main`:

```bash
git checkout main
```

Wechsel zurück auf einen bereits existierenden Feature-Branch:

```bash
git checkout feature/mein-feature
```

Wichtig:
Beim Wechsel zwischen Branches sollten keine ungesicherten Änderungen vorhanden sein.

Git erlaubt den Wechsel nur dann, wenn keine Dateien überschrieben würden.
Falls Änderungen im aktuellen Zustand mit dem Ziel-Branch kollidieren, wird der Wechsel aus Sicherheitsgründen verhindert, um Datenverlust zu vermeiden.

Empfehlung:
Sichern Sie Ihre Änderungen vor dem Wechsel, z.B. durch einen Commit oder temporär mit `git stash`.

---

### 5.4 Änderungen durchführen

* Code anpassen
* Dateien hinzufügen oder ändern

---

### 5.5 Änderungen committen und pushen

Nachdem Sie Ihre Änderungen vorgenommen haben, müssen diese zunächst lokal in Git festgehalten werden. Dies geschieht mit einem **Commit**.
Ein Commit ist ein definierter Zwischenstand Ihrer Arbeit mit einer Beschreibung, was geändert wurde.

Das ist wichtig, weil dadurch:

* Ihre Arbeit nachvollziehbar dokumentiert wird
* einzelne Änderungen historisch sichtbar bleiben
* der Maintainer besser versteht, was gemacht wurde
* Änderungen im Zweifel gezielt überprüft oder rückgängig gemacht werden können

Anschließend müssen Sie den Branch in Ihr entferntes Repository auf GitHub übertragen. Diesen Schritt nennt man **Push**.
Erst dadurch wird Ihre Arbeit online sichtbar und kann später als Pull Request eingereicht werden.

```bash
git add .
git commit -m "Beschreibung der Änderung"
git push origin feature/mein-feature
```

Die drei Befehle haben dabei folgende Funktion:

* `git add .` markiert geänderte Dateien für den nächsten Commit
* `git commit -m "..."` erstellt einen Commit mit einer aussagekräftigen Nachricht
* `git push origin feature/mein-feature` überträgt Ihren Branch auf GitHub

Achten Sie darauf, sinnvolle Commit-Nachrichten zu verwenden.
Eine gute Nachricht beschreibt knapp und konkret, was geändert wurde.

Nachdem der Feature akzeptiert und gemerged wurde, kann der Feature-Branch gelöscht werden

a) Remote Branch löschen

```bash
git push origin --delete feature/feature1
```

b) Lokalen Branch löschen (erzwingen)

```bash
git branch -D feature/feature1
```
---

### 5.6 Pull Request erstellen

Sobald Ihr Branch auf GitHub liegt, können Sie daraus einen **Pull Request** erstellen.
Damit teilen Sie dem Maintainer mit, dass Ihre Änderungen geprüft und gegebenenfalls in das Hauptrepository übernommen werden sollen.

Ein Pull Request erfüllt mehrere Zwecke:

* er macht Änderungen offiziell sichtbar
* er ermöglicht Review und fachliche Rückmeldung
* er dokumentiert den Grund und Inhalt einer Änderung
* er trennt Entwicklung und Integration sauber voneinander

Vorgehen:

1. Öffnen Sie Ihr Fork auf GitHub
2. Klicken Sie auf **„Compare & pull request“**
3. Prüfen Sie sorgfältig:

   * **Quelle:** Ihr Branch (`feature/mein-feature`)
   * **Ziel:** `zorcexe/event_project` → `main`
4. Fügen Sie eine aussagekräftige Beschreibung hinzu
5. Erstellen Sie den Pull Request

Wichtig ist insbesondere die Kontrolle von **Quelle** und **Ziel**.
Der Pull Request muss von Ihrem Fork beziehungsweise Ihrem Branch **in das Hauptrepository** gestellt werden.

In der Beschreibung sollte kurz stehen:

* was geändert wurde
* warum die Änderung vorgenommen wurde
* ob es Besonderheiten gibt, die beim Review zu beachten sind

### 5.7 Best Practices

Für eine effiziente Zusammenarbeit und eine reibungslose Integration Ihrer Änderungen sollten folgende Grundsätze beachtet werden:

**Kleine, fokussierte Änderungen**
Arbeiten Sie in möglichst kleinen, in sich abgeschlossenen Schritten.
Ein Pull Request sollte idealerweise genau eine fachliche Änderung enthalten. Das erleichtert Review und Fehlersuche erheblich.

**Aussagekräftige Commit-Nachrichten**
Beschreiben Sie präzise, was geändert wurde und ggf. warum.
Vermeiden Sie allgemeine Nachrichten wie „Update“ oder „Fix“.

**Klare Struktur im Code**
Halten Sie sich an bestehende Projektkonventionen (Formatierung, Benennung, Aufbau).
Uneinheitlicher Code erschwert die Wartung.

**Regelmäßig committen**
Erstellen Sie mehrere sinnvolle Commits statt eines großen Sammel-Commits.
So bleibt die Entwicklung nachvollziehbar.

**Pull Request verständlich beschreiben**
Erläutern Sie im Pull Request:

* was geändert wurde
* warum die Änderung notwendig ist
* ggf. wie getestet wurde

**Keine unnötigen Änderungen**
Vermeiden Sie Änderungen, die nicht direkt zum Ziel gehören (z.B. Formatierung im gesamten Projekt).
Diese erschweren das Review.

**Aktuellen Stand berücksichtigen (fortgeschritten)**
Stellen Sie sicher, dass Ihr Branch auf einem aktuellen Stand von `main` basiert, um Konflikte zu vermeiden.



## 6. Beispiel: Beitrag durch einen Teilnehmer (inkl. Befehle)

```text
Maintainer-Repository:
https://github.com/zorcexe/event_project

Beitragender (z.B. Bob):
https://github.com/bob/event_project   ← Fork
```

### Ablauf mit konkreten Befehlen

#### 1. Fork klonen

```bash
git clone https://github.com/bob/event_project.git
cd event_project
```

---

#### 2. Feature-Branch erstellen

```bash
git checkout -b feature/login-form
```

---

#### 3. Änderungen durchführen

(Beispiel: Code anpassen, neue Funktion hinzufügen)

---

#### 4. Änderungen committen

```bash
git add .
git commit -m "Login-Formular hinzugefügt"
```

---

#### 5. Branch pushen

```bash
git push origin feature/login-form
```

---

#### 6. Pull Request erstellen

* GitHub öffnen: https://github.com/bob/event_project
* Button klicken: **Compare & pull request**
* Ziel auswählen:

  * **von:** bob/event_project:feature/login-form
  * **nach:** zorcexe/event_project:main
* Beschreibung ergänzen
* Pull Request erstellen

---

### Ergebnis

```text
bob/event_project:feature/login-form
                ↓ Pull Request
zorcexe/event_project:main
```

Der Maintainer prüft anschließend die Änderungen und entscheidet über die Integration.


---

## 7. Anforderungen an einen guten Pull Request

* Klare Beschreibung der Änderung
* Kleine, fokussierte Änderungen
* Nachvollziehbare Commit-Nachrichten
* Funktionsfähiger Code

---

## 8. Review-Prozess

* Prüfung durch den Maintainer
* ggf. Rückfragen oder Anpassungen
* Integration in das Hauptprojekt
