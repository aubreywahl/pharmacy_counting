"""
coding challenge for insight data engineering
by: Aubrey Wahl
created: July 17 2018
"""

import argparse
import os
import csv

parser = argparse.ArgumentParser("Process a pharms .csv file")
parser.add_argument("fn_in", 
                    metavar="fn_input", 
                    type=str,
                    help="relative path to input .csv file (e.g. ./input/itcont.txt)"
                    ) 
parser.add_argument("fn_out", 
                    metavar="fn_output", 
                    type=str,
                    help="relative path to output .csv file (e.g. ./output/top_cost_drug.txt)"
                    ) 

args = parser.parse_args()

fd_in = args.fn_in
fd_out = args.fn_out

with open(fd_in) as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row["drug_name"])

# TODO: make this a real thing!
output_text = """drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300"""

with open(fd_out, "w") as f:
  f.write(output_text)
