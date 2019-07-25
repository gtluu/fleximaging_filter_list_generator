# Bruker flexImaging Filter List Generator
Generate m/z filter list in .mir format for Bruker flexImaging from m/z list.

## Dependencies
Python 2 with modules PyQT4, ElementTree, pandas, sys, os, random.

## Instructions
1. Download and unzip this repo.
2. Create spreadsheet with column header "mz" followed by m/z values and save as .csv file, as seen in "ExampleMZFile.csv".
3. Ensure that Python 2 is set to PATH.
4. Run "FilterListGenerator.bat" and follow instructions.
5. Place the generated .mir file in the same folder as your flexImaging Sequence.
6. Analyze data!
