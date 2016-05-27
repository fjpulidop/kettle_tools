import os, sys, getopt

def main(argv):
   hells_kitchen = ''
   job = ''
   log = ''
   iterations = ''
   try:
      opts, args = getopt.getopt(argv,"hk:j:l:i:",["hells_kitchen_path=","job=","log=","iterations="])
   except getopt.GetoptError:
      print 'loopEventFact.py -k <hells_kitchen_path> -j <etl_job_path_and_main_kjb> -l <log_name> -i <iterations>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'loopEventFact.py -k <hells_kitchen_path> -j <etl_job_path_and_main_kjb> -l <log_name> -i <iterations>'
         sys.exit()
      elif opt in ("-k", "--hells_kitchen"):
         hells_kitchen = arg + "hells_kitchen.sh"
      elif opt in ("-j", "--job"):
         job = arg
      elif opt in ("-l", "--log"):
	     log = arg
      elif opt in ("-i", "--iterations"):
         iterations = arg 

   EXECUTION = hells_kitchen + " --job=" + job + " --log-name=" + log

   for x in range(0, int(iterations)):
	   os.system(EXECUTION)

if __name__ == "__main__":
   main(sys.argv[1:])

