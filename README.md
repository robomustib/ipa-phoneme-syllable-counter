# IPA Phoneme & Syllable Counter

Python tool for counting words, phonemes and syllables from IPA-transcribed child language data. Supports German and Turkish.

## Features

- Counts number of words in an IPA string
- Counts number of phonemes (ignores IPA diacritics)
- Counts number of syllables with language-specific rules:
  - **German**: Diphthongs count as one syllable
  - **Turkish**: Simple vowel counting (no diphthongs)
- Works directly with IPA input from phonemizer
- Outputs new columns in Excel without overwriting original data

## Requirements

```bash
pip install pandas openpyxl
```

## Usage

```bash
python phonem_laenge_zaehler.py <excel_file> <language>
```

## Examples
```bash
# Turkish data
python phonem_laenge_zaehler.py woerter_tr.xlsx TR

# German data
python phonem_laenge_zaehler.py woerter_de.xlsx DE
```

## Input Format
The Excel file must contain a column named phonems_IPA with IPA transcriptions.

## Output
The script creates a new file counted_<original_filename>.xlsx with three additional columns:
- n_words_counted
- n_phonemes_counted
- n_syllables_counted

## Language-Specific Syllable Counting
### German
Diphthongs (aɪ, aʊ, ɔʏ, oɪ, ɔø, ʏø) are counted as single syllables.

### Turkish
Every vowel counts as one syllable (no diphthongs in Turkish).

