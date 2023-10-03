#!/bin/bash
Me="Methionine"
Le="Leucine"
Cy="Cysteine"
Al="Alanine"
Va="Valine"
echo $Me
echo $Le
echo $Cy
echo $Al
echo $Va
total=$((${#Me}+${#Le}+${#Cy}+${#Al}+${#Va}))
echo $total