from __init__ import main
from memory_profiler import memory_usage

if __name__ == '__main__':
  # main()
  mem_usage = memory_usage(main)
  print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
  print('Maximum memory usage: %s' % max(mem_usage))  

