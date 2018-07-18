import argparse

def parse_commandline_args():
  """
  
  """
  parser = argparse.ArgumentParser("Process a pharms .csv file")
  parser.add_argument("fp_in", 
                      metavar="in", 
                      type=str,
                      help="relative path to input .csv file (e.g. ./input/itcont.txt)"
                      ) 
  parser.add_argument("fp_out", 
                      metavar="out", 
                      type=str,
                      help="relative path to output .csv file (e.g. ./output/top_cost_drug.txt)"
                      ) 

  args = parser.parse_args()

  return args.fp_in, args.fp_out