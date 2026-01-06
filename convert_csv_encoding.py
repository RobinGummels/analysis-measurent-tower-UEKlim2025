"""
Konvertiert CSV-Dateien von CP850 (MS-DOS) zu UTF-8 Codierung
um Umlaute korrekt darzustellen.
"""
import os
from pathlib import Path

# Pfad zum CSV-Ordner
csv_folder = Path(__file__).parent / "data" / "data-as-csv"

# Mögliche Codierungen, die ausprobiert werden
encodings = ['cp850', 'cp1252', 'latin-1', 'iso-8859-1']

for csv_file in csv_folder.glob("*.csv"):
    print(f"\nKonvertiere: {csv_file.name}")
    
    content = None
    used_encoding = None
    
    # Versuche verschiedene Codierungen
    for encoding in encodings:
        try:
            with open(csv_file, 'r', encoding=encoding) as f:
                content = f.read()
            used_encoding = encoding
            print(f"  ✓ Erfolgreich gelesen mit {encoding}")
            break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        print(f"  ✗ Konnte {csv_file.name} mit keiner Codierung lesen!")
        continue
    
    # Speichere als UTF-8
    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"  ✓ Gespeichert als UTF-8")
    except Exception as e:
        print(f"  ✗ Fehler beim Speichern: {e}")

print("\n✓ Konvertierung abgeschlossen!")
