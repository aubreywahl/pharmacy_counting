import os
import csv

from args import parse_commandline_args

# get input/output file paths
path_in, path_out = parse_commandline_args()

with open(path_in) as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row["drug_name"])

# TODO: make this a real thing!
output_text = """drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300"""

with open(path_out, "w+") as f:
  f.write(output_text)
