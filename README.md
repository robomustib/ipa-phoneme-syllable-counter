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

## Flowchart
<img src="https://raw.githubusercontent.com/robomustib/ipa-phoneme-syllable-counter/2b140135c233908d91c858e981568151c19e58c6/img/flowchartipa.svg" alt="Flowchart of the IPA Phoneme & Syllable Counter" width="80%"/>

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License.
**Note:** You are free to share and adapt the material for non-commercial purposes, provided you give appropriate credit. Commercial use is not permitted without prior consent. For details, see the [LICENSE](LICENSE) file.

Copyright (c) 2026 Mustafa Bilgin

## Citation

If you use this software for your research, please cite it as follows:

**APA Format:**
> Bilgin, M. (2026). *IPA Phoneme & Syllable Counter* (Version 1.3.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.19138813 

**BibTeX:**
```bibtex

@software{ipa-phoneme-syllable-counter,
  author       = {Bilgin, Mustafa},
  title        = {IPA Phoneme & Syllable Counter: A Python Tool for Phonological Analysis of Child Language Data Latest},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.19138813},
  url          = {https://doi.org/10.5281/zenodo.19138813}
}

```

## Acknowledgements
This repository is the result of an ongoing collaboration with colleagues who brought the right research questions and data to the table. I specifically want to thank Birgit, who provided the initial impulse for many of these features. Her linguistic and methodological questions shaped the conceptual foundation of this tool, while the code and implementation are my own. I am very grateful for this teamwork. It reminds me that code is ultimately just a medium to answer real-world questions – not the other way around.
