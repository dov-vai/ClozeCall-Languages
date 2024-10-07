#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Process Tatoeba sentence pairs and add language code to output.')
parser.add_argument('input_file', help='Path to the input file')
parser.add_argument('output_file', help='Path to the output file')
parser.add_argument('language_code', help='Language code to append to each line')

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
language_code = args.language_code

with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
    open(output_file, 'w', encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        elements = line.strip().split('\t')

        outfile.write('\t'.join([elements[1], elements[3], language_code]) + '\n')

print(f"Processed {input_file} and saved the result to {output_file}.")

