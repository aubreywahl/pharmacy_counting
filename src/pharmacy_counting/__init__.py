import os
import csv
import operator
from itertools import groupby
from args import parse_commandline_args


def group_costs_by_drug_and_prescriber(path_in):
  """
  This function take the path to csv formatter like:
    id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
    1000000001,Smith,James,AMBIEN,100
    1000000002,Garcia,Maria,AMBIEN,200
    1000000003,Johnson,James,CHLORPROMAZINE,1000
    1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
    1000000005,Smith,David,BENZTROPINE MESYLATE,1500

  And returns an object that looks like this:

  {
    'AMBIEN': {
      ('James', 'Smith'): 100,
      ('Maria', 'Garcia'): 200,
    }

    [...]
  }

  In other words, it groups the cost the cost of each drug by
  prescriber and drug name. If a particular drug has more than
  one presriber of the same name, it takes the one with the 
  highest cost.

  """
  accumulator = {}

  with open(path_in) as f:

    reader = csv.DictReader(f)

    # read relevant info from dataset
    for row in reader:
      
      drug  = row["drug_name"]
      fname = row["prescriber_first_name"]
      lname = row["prescriber_last_name"]
      cost  = int(row["drug_cost"])
      
      if (drug not in accumulator):
        accumulator[drug] = {}

      cost_by_prescriber = accumulator[drug]

      tup = (fname, lname)

      # if cost has not been recorded, record it
      if (tup not in cost_by_prescriber):
        cost_by_prescriber[tup] = cost
      
      # greedily use highest-cost value
      elif (cost_by_prescriber[tup] < cost):
        cost_by_prescriber[tup] = cost

      accumulator[drug] = cost_by_prescriber

    return accumulator


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

  # see the definition of group_costs_by_drug_and_prescriber
  # to see an example of what this object looks like
  info_grouped_by_drug = group_costs_by_drug_and_prescriber(path_in)

  # this is a list of [drug_name,num_prescriber,total_cost] tuples, unsorted
  output = [
    flatten([[k], count_and_sum(info_grouped_by_drug[k])]) 
    for k in info_grouped_by_drug
  ]

  # we use the sort method to sort in-place, which may spare us 
  # some memory when we use a larger input file!
  output.sort(key=operator.itemgetter(2,0), reverse=True)

  with open(path_out, "w+") as f:

    f.write('drug_name,num_prescriber,total_cost')
    
    for line in output:
      # for some reason, the spec neglects ending newline char
      formatted = "\n" + ",".join(map(str, line))
      f.write(formatted)
