assyriolograph
==============

## Process scripts to help build a graph of ancient letters

To run these scripts, you need the following tools:

1.  Python
2.  R
3.  Gephi

First, you will run the `process_all.py` script.  In order to run it, you need to first open the file in any text editor and change the path to the exported file from Filemaker.  Then, open a terminal, change to the correct directory and type `python process_all.py`.

This will create a file called `AllLetters_Proc.csv`, which contains the parsed information from the original file.  You will then use R to compute some basic statistics.

Open the R file `ranks_nomerge.R` and change the paths in this file as well.  You will then run this file by, e.g., clicking the Source button in RStudio.  Note that before running this script, you will need to install a few R packages.  You can do that by typing:

     install.packages('plyr')	
     install.packages('SDMTools')

In the RStudio console.  You will only need to do this once.

After running this R Script, you can load your data into Gephi.  Load the Nodes csv first by going to data laboratory and clicking import spreadsheet, then finding the `all_letter_nodes.csv` file.  You will need to do the following:

* Change the data type to `double` for anything that is a number (there will be a lot of these!)
* After loading, copy the column data from rankname to label

Then, you can load in the `all_letter_edges.csv` file as an edge table.

The upper left hand panel in the Overview tab will let you map rank information to color and size.  I like using meanrank as size and wsd as color.  The variable wsd here stands for the weighted standard deviation - a measure of confidence in a node's rank.

The layout options we've been using start with the YiFan Hu proportional, but you can do whatever looks good!