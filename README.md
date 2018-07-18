# Pharmacy Counting Challenge

The purpose of this program is to process a CSV file in the following format:

```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

Into a CSV like this:

```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

In other words, as an input the program takes a list of drug perscribers/drug name/cost of drug. The output is a list of the drug names/number of perscribers/total cost, orderd in descending order by total cost -> drug name -> number of prescribers.

# How to Run

You need python 3. This program only uses python3 standard library functions.

To run this, try something like

`python3 ./src/pharmacy_counting path/to/input path/to/output`

# Notes/Concerns

I certainly did not give myself enough time to work on this (i basically learned python from scratch for this).


This implementation is not performant. Running this code on the large (1 GB+) dataset took about 6 minutes on my hardware and ran over 5 GB of RAM. This is obviously not ideal. This happens because my program sorts the data in-memory. If I had time, I would attempt to implement an external sort. This would sacrifice disk space for memory space, and also might take much longer to run (especially if my implementation is crummy). However, memory might be more precious than disk (depending on the setup). 


In the real world, I would just use a more advanced data structure like a panda or something. External libraries were forbidden here.


I would also like to add some test inputs so that I can be sure my code is rigorously correct.


For example, I should be writing tests to ensure that my inputs are indeed sorting in the correct order for funky inputs. Also should test the behavior of duplicate drug_name/prescriber combos.


Given more time, I might also implement some light data sanitization--i.e. to skip any rows in the input that might happen to be poorly-formatted.
