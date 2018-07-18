# from memory_profiler import memory_usage
from __init__ import main

if __name__ == '__main__':
  main()

  ## uncomment this stuff if you want to profile the memory!
  ## inspired by: https://stackoverflow.com/a/15682871

  # mem_usage = memory_usage(main)
  # print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
  # print('Maximum memory usage: %s' % max(mem_usage))  

