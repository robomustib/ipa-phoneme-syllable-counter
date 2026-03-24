"""
IPA Phoneme & Syllable Counter (DE & TR) - v2.0
Liest Excel-Dateien mit einer Spalte "phonems_IPA" ein 
und berechnet Anzahl Wörter, Silben und Phoneme (inkl. Affrikaten/Diphthong-Korrektur).
"""

import pandas as pd
import re
import sys
import os

VOWELS_GENERIC = r'[aeiouyøœɛɔɪʊəɐæɑɒʌɤɨʉɯ]'

DIPHTHONGS_DE = ['aɪ', 'aʊ', 'ɔʏ', 'oɪ', 'ɔø', 'ʏø']

AFFRICATES_ALL = ['pf', 'ts', 'tʃ']
AFFRICATES_TR = ['dʒ']

def count_words(ipa_text):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    words = ipa_text.strip().split()
    return len(words)

def count_ipa_chars(ipa_text):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    cleaned = re.sub(r'[\sˈˌːˑ.͜͡|]', '', ipa_text)
    return len(cleaned)

def count_phonemes(ipa_text, lang):
    if pd.isna(ipa_text) or not isinstance(ipa_text, str):
        return 0
    cleaned = re.sub(r'[\sˈˌːˑ.͜͡|]', '', ipa_text)
    for aff in AFFRICATES_ALL:
        cleaned = cleaned.replace(aff, 'X')
    if lang.upper() == "DE":
        for d in DIPHTHONGS_DE:
            cleaned = cleaned.replace(d, 'X')
    elif lang.upper() == "TR":
        for aff in AFFRICATES_TR:
            cleaned = cleaned.replace(aff, 'X')
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
    if len(sys.argv) != 3:
        print("Aufruf: python phonem_laenge_zaehler.py <Excel-Datei> <Sprache: DE oder TR>")
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
        print("Fehler: Spalte 'phonems_IPA' existiert nicht.")
        sys.exit(1)

    print(f"Sprache: {language}")

    df['n_words'] = df['phonems_IPA'].apply(count_words)
    df['n_ipa_chars'] = df['phonems_IPA'].apply(count_ipa_chars)
    df['n_phonemes'] = df['phonems_IPA'].apply(lambda x: count_phonemes(x, language))
    df['n_syllables'] = df['phonems_IPA'].apply(lambda x: count_syllables(x, language))

    output_filename = f"counted_{os.path.basename(excel_file)}"
    try:
        df.to_excel(output_filename, index=False)
        print(f"Fertig! Ergebnisse gespeichert in: {output_filename}")
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()