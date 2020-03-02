# Imaging mass spectrometry scripts for use with Bruker's flexImaging

## Bruker flexImaging Filter List Generator
Generate m/z filter list in .mir format for Bruker flexImaging from m/z list.

### Dependencies
Python 2 with modules PyQT4, ElementTree, pandas, sys, os, random.

### Instructions
1. Download and unzip this repo.
2. Create spreadsheet with column header "mz" followed by m/z values and save as .csv file, as seen in "ExampleMZFile.csv".
3. Ensure that Python 2 is set to PATH.
4. Run "FilterListGenerator.bat" and follow instructions.
5. Place the generated .mir file in the same folder as your flexImaging Sequence.
6. Analyze data!

## Bruker flexImaging AutoHotKey Macros
Automatically tab through ion images and map F2 key to add ion to filter list in Bruker flexImaging.

### Dependencies
AutoHotKey

### Instructions
1.	Download and install AutoHotKey if necessary.
2.	Download the script and place it the desired directory.
3.	Double-click the script to run.
	NOTE: If the script is not working, you may need to “Run as Administrator”.
4.	Click anywhere in “Spectrum Display” in flexImaging to begin auto-tabbing while the script is running.
	NOTE: Tabbing is done every X seconds and can be edited by opening the script in a text editor and changing the number after “SetTimer,Tab,” (value is in msec).
5.	Press the “Pause” key on the keyboard to pause tabbing.
6.	Press F2 to add the current m/z value to the current filter list.
	NOTE: Warning: Leaving the script open when not using flexImaging will affect other programs that have the F2 key mapped to another function.
7.	Analyze data!
