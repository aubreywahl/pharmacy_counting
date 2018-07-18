import os
import csv
import operator
from itertools import groupby
from args import parse_commandline_args

"""
flattens iterable by one level.

e.g. flatten([1, ("some str", 2)]) => [1, "some str", 2]
"""
flatten = lambda l: [item for sublist in l for item in sublist]


def count_and_sum(cost_dict):
  """
  takes a dictionary that looks like this:
    {
      ("Smith", "James"): 100.00,
      ("Maria", "Hernandez"): 2033.33
    }

  returns a tuple (count, total), where `count` is a count of the entries 
  and `total` is a sum of all the values in the dict.
  """
  total = 0
  count = 0

  for k in cost_dict:
    total += cost_dict[k]
    count += 1

  return count, total
  

def main():

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

      # if cost has not been recorded, record it
      if (tup not in cost_by_prescriber):
        cost_by_prescriber[tup] = cost
      
      # greedily use highest-cost value
      elif (cost_by_prescriber[tup] < cost):
        cost_by_prescriber[tup] = cost

      info_grouped_by_drug[drug] = cost_by_prescriber

  # this is a list of [drug_name,num_prescriber,total_cost] tuples, unsorted
  output = [flatten([[k], count_and_sum(info_grouped_by_drug[k])]) for k in info_grouped_by_drug]

  output.sort(key=operator.itemgetter(2,0), reverse=True)

  with open(path_out, "w+") as f:
    fieldnames = ['drug_name', 'num_prescriber', 'total_cost']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    
    for line in output:
      # this looks kinda dumb, but i had to for it to work
      # i don't know how to python :'-(
      writer.writerow({
        'drug_name': line[0], 
        'num_prescriber': line[1],
        'total_cost': line[2],
      })
