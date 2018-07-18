import os
import csv
from itertools import groupby
from args import parse_commandline_args

# gives one level of array-flattening
flatten = lambda l: [item for sublist in l for item in sublist]

def count_and_sum(cost_dict):
  total = 0
  count = 0
  for k in cost_dict:
    total += cost_dict[k]
    count += 1

  return count, total
  

def main():
  # get input/output file paths
  path_in, path_out = parse_commandline_args()

  info_grouped_by_drug = {}

  with open(path_in) as f:

    reader = csv.DictReader(f)

    # read relevant info from dataset
    for row in reader:
      
      drug  = row["drug_name"]
      fname = row["prescriber_first_name"]
      lname = row["prescriber_last_name"]
      cost  = float(row["drug_cost"])
      
      if (drug not in info_grouped_by_drug):
        info_grouped_by_drug[drug] = {}


      cost_by_prescriber = info_grouped_by_drug[drug]

      tup = (fname, lname)

      # print("CPB before:" ,cost_by_prescriber)

      # if cost has not been recorded, record it
      if (tup not in cost_by_prescriber):
        cost_by_prescriber[tup] = cost
        # print("CBP after:", cost_by_prescriber)
      
      # greedily use highest-cost value
      elif (cost_by_prescriber[tup] < cost):
        cost_by_prescriber[tup] = cost

      info_grouped_by_drug[drug] = cost_by_prescriber


  print(info_grouped_by_drug)
  unsorted_output = [flatten([[k], count_and_sum(info_grouped_by_drug[k])]) for k in info_grouped_by_drug]

  print(unsorted_output)

  # TODO: make this a real thing!
  output_text = """drug_name,num_prescriber,total_cost
  CHLORPROMAZINE,2,3000
  BENZTROPINE MESYLATE,1,1500
  AMBIEN,2,300"""

  with open(path_out, "w+") as f:
    f.write(output_text)