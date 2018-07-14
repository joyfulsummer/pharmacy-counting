Pharmacy Counting Solution

Description:

Input file itcont.txt contains a list of data where each line is in the order of id, prescriber_last_name, prescriber_first_name, 
drug_name, and drug_cost. The program pharmacy-counting.py is used to process the input file to give the output file. 
For each unique drug_name, the number of prescribers that has prescribed the drug is counted, and the total cost prescribed
by all the prescribers for the drug is calculated. The entries in the output file should be sorted in cost-descending order.

Analysis:

There can be different situations in the data of the input file, and needs to be treated differently when reading data.

1st situation: entries are pretty simple, and the five components “id, last_name, first_name, drug_name, drug_cost” are 
separated purely by comma. For example, “1952310666, A’BODJEDI, ENENGE, ALPRAZOLAM, 1964.49“. In this situation, we just
need to use line.split(“,”) to get a list of the correct components, where the variable line is a line read from input.

2nd situation: entries have five components, but the components are more complexed. There may be comma in the drug_name
 or prescriber_name themselves, and the names with comma are quoted by quotation marks. 
For example, “1063421576, "ABRAHAM, M.D.”, CINI, BENZTROPINE MESYLATE, 223.51“.
In this case, simply splitting the string by comma can not distinguish the correct components. Instead, we need to first
treat the thing in the quotation marks as one component like “ABRAHAM, M.D.”, and separate it out. Then we look for other
simpler components. 

3rd situation: components are missing or entries are wrong. For example, prescriber or drug names are missing, or multiple names
are provided so it is hard to distinguish. In this situation, I consider the data invalid and skip the line.

Algorithm:

I use dictionary to store the cost and prescribers for each drug. The variable cost is a dictionary where key is drug_name
and value is the total cost for the drug. The variable prescriber is a dictionary where key is drug_name and value is a
set() where prescriber names are added. The cost is sorted into a list cost_sorted by descending order of the total_cost
for a drug. According to the order of entries in cost_sorted, I know the total_cost and number of unique prescribers for
each drug according to the dictionaries of cost and prescriber. The numbers are written into the output file.

When dealing with the three situations in the data, I use the following algorithm:

First split each line from input by comma into a list t, and distinguish different situations according to the length of t.

1st situation: len(t) = 5; read t to get the five components.

2nd situation: len(t) > 5. First split the line by quotation marks into a list x, and separate the names like "ABRAHAM, M.D.”
as one word. Usually len(x) will be 3. The situation can future be divided into three cases. If prescriber_last_name has 
quotation marks, x[0] will be “id,”, x[1] will be last_name, and x[2] will be “,first_name + drug_name + drug_cost”.
If prescriber_first_name has quotation marks, x[0] will be “id + last_name,”, x[1] will be first_name, and x[2] will be
“,drug_name + drug_cost”. If drug_name has quotation mark, x[0] will be “id + last_name + first_name,”, x[1] will be 
drug_name, x[2] will be “,drug_cost”. The three cases can be distinguished by len(x[0]). Then read the components 
accordingly.

If N is the number of lines in the input file, then space complexity of the code is O(N). Average time complexity is O(N), 
and worst case is O(N^2), since dictionary.get() has an averaged complexity of O(1) and worst case of O(N), and total line
reading takes O(N). 

Note when I calculate the total_cost of drugs, I use float instead of interger to represent the costs. If rounding the cost to intergers, then some information may be missed, for example, cost 0.1 can be the same order as cost 0.2. 

Compilation:

The input file itcont.txt is stored under input directory, and the output file is store under the output directory. The code 
pharmacy-counting.py is stored under the src directory. Just type "./run.sh" in the command window should execute the program. 

In run.sh, Python3 is used. No additional external libraries are used. 

Testing:

The code is tested against provided test case in the test_1 folder and self-made test case in the test_2 folder.
The data of the inputfile in test_2/input is a mix of the 1st and 2nd situation. 

The code is also tested against a file with over 24 million entries are provided and text file 
size is over 1GB. Every entries in the file is processed by pharmacy-counting.py including the 2nd situation. I added up
the total cost by summing up the total_drug_cost from the lines at the output file, and I added up the total cost by
summing up the total_drug_cost2 from the lines at the input file. The two total cost are the same, indicating the code
did well. It took less than 2 mins for an average MAC laptop to process the 1.1GB data using pharmacy-counting.py, 
as both the time and space complexity are O(N). 

The format of output in test_1 and test_2 are both passed by run_tests.sh.




