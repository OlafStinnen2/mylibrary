# PDM Cheat Sheet

> Python Dependency Manager – Schnellreferenz

---

## Projekt Setup

```bash
pdm init                        # Neues Projekt anlegen
pdm install                     # Alle Abhängigkeiten installieren (aus pdm.lock)
pdm install --prod              # Nur Produktionsabhängigkeiten
pdm install -dG test            # Prod + Test-Gruppe
pdm install -dG dev             # Prod + Dev-Gruppe
pdm install --without dev       # Alles außer dev-Gruppe
```

---

## Abhängigkeiten verwalten

```bash
# Hinzufügen
pdm add requests                # Produktionsabhängigkeit
pdm add -dG test pytest         # Test-Gruppe
pdm add -dG dev black           # Dev-Gruppe
pdm add -dG dev pre-commit      # Dev-Gruppe

# Entfernen
pdm remove requests             # Paket entfernen

# Aktualisieren
pdm update                      # Alle Pakete updaten
pdm update requests             # Einzelnes Paket updaten

# Anzeigen
pdm list                        # Installierte Pakete anzeigen
pdm list --tree                 # Abhängigkeitsbaum anzeigen
```

---

## Lockfile

```bash
pdm lock                        # Lockfile neu erzeugen
pdm lock --update-reuse         # Lockfile aktualisieren, Versionen wiederverwenden
```

---

## Virtual Environments

```bash
pdm venv list                   # Alle venvs anzeigen
pdm venv create 3.12            # Neues venv mit Python 3.12
pdm venv remove 3.12            # venv löschen
pdm venv purge                  # Alle venvs löschen
pdm use .venv                   # Standard-venv aktivieren
pdm info                        # Projektinfos und Interpreter-Pfad
```

---

## Scripts & Ausführen

```bash
pdm run python script.py        # Python-Skript ausführen (ohne venv aktivieren)
pdm run pytest                  # pytest ausführen
pdm run black .                 # black ausführen
pdm run black --check .         # black nur prüfen (für CI)
pdm run pre-commit run --all-files  # pre-commit auf alle Dateien anwenden
```

Scripts können in `pyproject.toml` definiert werden:

```toml
[tool.pdm.scripts]
check = "black --check ."
test  = "pytest"
```

---

## pyproject.toml Struktur

```toml
[project]
name = "mein-projekt"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
]

[dependency-groups]
dev  = ["black>=25.0", "pre-commit>=4.0"]
test = ["pytest>=8.0"]

[tool.pdm.scripts]
check = "black --check ."
test  = "pytest"
```

---

## GitHub Actions – CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/pdm-setup
      - run: pdm install -dG dev
      - run: pdm run check

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/pdm-setup
      - run: pdm install -dG test
      - run: pdm run pytest
```

---

## Composite Action

```yaml
# .github/actions/pdm-setup/action.yml
name: PDM Setup
description: Checkout, Python und PDM installieren

inputs:
  python-version:
    description: 'Python version to use'
    required: false
    default: '3.12'

runs:
  using: composite
  steps:
    - uses: actions/checkout@v4.2.2
    - uses: actions/setup-python@v5.4.0
      with:
        python-version: ${{ inputs.python-version }}
    - run: pip install pdm
      shell: bash
```

---

## Pre-commit Hook (Black)

Pre-commit ist eine erste Verteidigungslinie: Black läuft automatisch vor jedem
`git commit` – der Entwickler kann das Formatieren gar nicht vergessen.
Die zweite Verteidigungslinie ist der `black --check` in der CI-Pipeline.

```
Entwickler-PC                    GitHub Actions (CI)
─────────────────────────────    ──────────────────────────────
git commit                       Push / Pull Request
  └─ pre-commit Hook             └─ lint Job
       └─ black formatiert            └─ black --check prüft
          automatisch                    → Merge blockiert falls fehlgeschlagen
```

**Schritt 1: Konfigurationsdatei anlegen**

```yaml
# .pre-commit-config.yaml  (im Projektroot, in Git committen!)
repos:
  - repo: https://github.com/psf/black   # Quelle: offizielles Black-Repo
    rev: 25.1.0                           # Exakte Black-Version (wie ein Lockfile)
    hooks:
      - id: black                         # Welcher Hook aus dem Repo aktiviert wird
```

**Schritt 2: Befehle ausführen**

```bash
# pre-commit als Dev-Abhängigkeit ins Projekt aufnehmen
pdm add -dG dev pre-commit

# Hook in Git registrieren – erzeugt einen Eintrag in .git/hooks/pre-commit
# Muss jeder Entwickler einmalig nach dem Clonen des Repos ausführen
pdm run pre-commit install

# Alle Dateien einmalig prüfen und formatieren (z.B. nach der Ersteinrichtung)
# Bei einem normalen Commit prüft pre-commit nur die geänderten Dateien
pdm run pre-commit run --all-files
```

**Was passiert bei einem `git commit`?**

```
git commit -m "mein feature"
  → pre-commit Hook startet automatisch
  → black prüft alle geänderten .py Dateien
  → Falls Formatierung nötig: Dateien werden korrigiert, Commit wird abgebrochen
  → Entwickler führt git add + git commit erneut aus – diesmal ist alles sauber
```

---

## Migration von requirements.txt

```bash
mkdir mein-projekt
cd mein-projekt
pdm init
# Abhängigkeiten aus requirements.txt manuell übertragen:
pdm add requests
pdm add -dG test pytest
pdm add -dG dev black pre-commit
```

---

## Wichtige Dateien

| Datei | Zweck |
|---|---|
| `pyproject.toml` | Menschenlesbare Projektkonfiguration (PEP 621) |
| `pdm.lock` | Exakte Versionen aller Pakete inkl. Hashes – nie manuell editieren |
| `.pre-commit-config.yaml` | Pre-commit Hook Konfiguration |
| `.github/workflows/ci.yml` | GitHub Actions Pipeline |
| `.github/actions/pdm-setup/action.yml` | Composite Action für Setup-Steps |

---

## Kernprinzipien

- **Lockfile committen** – garantiert reproduzierbare Builds im Team und CI
- **Dependency Groups trennen** – `prod` / `dev` / `test` sauber halten
- **Nie `pip install` im Projekt** – immer `pdm add`
- **Nie `source .venv/bin/activate`** – immer `pdm run`
- **Zwei Verteidigungslinien** – Pre-commit Hook lokal + Black-Check in CI