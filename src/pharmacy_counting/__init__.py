import os
import csv
from itertools import groupby
from args import parse_commandline_args

def main():
  # get input/output file paths
  path_in, path_out = parse_commandline_args()

  info_grouped_by_drug = {}

  with open(path_in) as f:

    reader = csv.DictReader(f)

    for row in reader:
      
      drug  = row["drug_name"]
      fname = row["prescriber_first_name"]
      lname = row["prescriber_last_name"]
      cost  = row["drug_cost"]
      
      if (drug not in row):
        info_grouped_by_drug[drug] = {}

      cost_by_prescriber = info_grouped_by_drug[drug]

      tup = (fname, lname)

      # if cost has not been recorded, record it
      if (tup not in cost_by_prescriber):
        cost_by_prescriber[tup] = cost
      
      # greedily use highest-cost value
      elif (cost_by_prescriber[tup] < cost):
        cost_by_prescriber[tup] = cost

  print(info_grouped_by_drug.keys())

  # TODO: make this a real thing!
  output_text = """drug_name,num_prescriber,total_cost
  CHLORPROMAZINE,2,3000
  BENZTROPINE MESYLATE,1,1500
  AMBIEN,2,300"""

  with open(path_out, "w+") as f:
    f.write(output_text)