"""
IPA Phoneme & Syllable Counter (DE & TR)
Liest Excel-Dateien mit einer Spalte "words" (IPA-Transkription) ein 
und berechnet Wörter, Silben und Phoneme.
"""

import pandas as pd
import re
import sys
import os

VOWELS_GENERIC = r'[aeiouyøœɛɔɪʊəɐæɑɒʌɤɨʉɯ]'
DIPHTHONGS_DE = ['aɪ', 'aʊ', 'ɔʏ', 'oɪ', 'ɔø', 'ʏø']

def count_words(ipa_text):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    words = ipa_text.strip().split()
    return len(words)

def count_phonemes(ipa_text):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    cleaned = re.sub(r'[\sˈˌːˑ.͜͡|]', '', ipa_text)
    return len(cleaned)

def count_syllables(ipa_text, lang):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    text = ipa_text.lower()
    
    if lang.upper() == "DE":
        for d in DIPHTHONGS_DE:
            text = text.replace(d, '1')
        vowel_count = text.count('1') + len(re.findall(VOWELS_GENERIC, text))
        return vowel_count
    
    elif lang.upper() == "TR":
        return len(re.findall(VOWELS_GENERIC, text))
    
    else:
        raise ValueError("Sprache muss 'DE' oder 'TR' sein.")

def main():
    print("="*60)
    print(" IPA PHONEME & SYLLABLE COUNTER")
    print("="*60)

    if len(sys.argv) != 3:
        print("Aufruf: python phonem_laenge_zaehler.py <Excel-Datei> <Sprache: DE oder TR>")
        print("Beispiel: python phonem_laenge_zaehler.py woerter_tr.xlsx TR")
        print("Beispiel: python phonem_laenge_zaehler.py woerter_de.xlsx DE")
        sys.exit(1)

    excel_file = sys.argv[1]
    language = sys.argv[2].upper()

    if language not in ["DE", "TR"]:
        print("Fehler: Sprache muss 'DE' oder 'TR' sein.")
        sys.exit(1)

    if not os.path.exists(excel_file):
        print(f"Fehler: Datei '{excel_file}' nicht gefunden.")
        sys.exit(1)

    try:
        df = pd.read_excel(excel_file)
        print(f"Datei '{excel_file}' erfolgreich geladen.")
    except Exception as e:
        print(f"Fehler beim Lesen der Excel-Datei: {e}")
        sys.exit(1)

    if 'phonems_IPA' not in df.columns:
        print("Fehler: Spalte 'phonems_IPA' existiert nicht in der Tabelle.")
        print(f"Gefundene Spalten: {list(df.columns)}")
        sys.exit(1)

    print(f"Sprache: {language}")
    print("Berechne Werte...")
    
    df['n_words_counted'] = df['phonems_IPA'].apply(count_words)
    df['n_phonemes_counted'] = df['phonems_IPA'].apply(count_phonemes)
    df['n_syllables_counted'] = df['phonems_IPA'].apply(lambda x: count_syllables(x, language))

    output_filename = f"counted_{os.path.basename(excel_file)}"
    try:
        df.to_excel(output_filename, index=False)
        print(f"Fertig! Ergebnisse gespeichert in: {output_filename}")
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")
        sys.exit(1)
    
    print("="*60)
    total_rows = len(df)
    print(f"Verarbeitete Zeilen: {total_rows}")
    print(f"Beispieldaten (erste 3 Zeilen):")
    print(df[['phonems_IPA', 'n_words_counted', 'n_syllables_counted', 'n_phonemes_counted']].head(3))

if __name__ == "__main__":
    main()
