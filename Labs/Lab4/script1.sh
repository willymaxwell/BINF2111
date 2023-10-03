#!/bin/bash

grep -e 'ATG' example2.fasta|wc -l

grep -e 'TAA|TAG|TGA' example2.fasta|wc -l