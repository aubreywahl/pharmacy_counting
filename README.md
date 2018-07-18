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

In other words, as an input the program takes a list of drug perscribers/drug name/cost of drug. The output is a list of the drug names/number of perscribers/total cost, orderd in descending order by total cost -> drug name -> number of perscribers.

# How to Run

You need python 3. This program only uses python3 standard library functions.

To use on it's own, try something like

`python3 ./src/pharmacy_counting path/to/input path/to/output`