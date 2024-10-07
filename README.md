# Cloze Call Languages

A repository for storing language files used in the [Cloze Call](https://github.com/dov-vai/ClozeCall) project.

# Languages

Currently available languages:
- Russian
- French
- German
- Spanish
- Portuguese

Feel free to open an issue if you need a certain language to be added, as long as it's available on [Tatoeba](https://tatoeba.org), or another source that's easy to process.

# Making your own

The format of the files is simple, each row looks like this:

`
original_sentence   translated_sentence language_code
`

The entries are separated by tabs.

You can mix and match multiple languages in a single file to have a custom language pack.

The two letter language code follows the [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) standard. It is used in the application for the translations and text-to-speech.

# Process Tatoeba sentence pairs
This repository includes [process_tatoeba.py](process_tatoeba.py) for sentence pair processing.
The pairs can be found [here](https://tatoeba.org/en/downloads).

## Usage
```bash
> python process_tatoeba.py --help
usage: process_tatoeba.py [-h] input_file output_file language_code

Process Tatoeba sentence pairs and add language code to output.

positional arguments:
  input_file     Path to the input file
  output_file    Path to the output file
  language_code  Language code to append to each line

options:
  -h, --help     show this help message and exit
```

## Issues
However when running this script, there might occur errors like:
> SyntaxError: unterminated string literal

> SyntaxError: invalid character

For some reason Tatoeba provides some files incorrectly encoded as UTF-8. On Linux you can use iconv to force re-encode the file:

```bash
iconv -t UTF-8 input.tsv -o output.tsv
```
Then the python script should work.

# Credits

All credits for the sentences go to [Tatoeba](https://tatoeba.org).

The language pairs are downloaded, and then processed to fit the format the application requires.
