import sys

# get the command line parameters
input_filename = sys.argv[1].strip()
output_filename = sys.argv[2].strip()
#open input_file for reading and output_file for writing
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#skip the first line of the input_file
next(input_file)

#the variable cost is a dictionary where key is drug_name, and value is the drug's total_cost.
#the variable prescriber is a dictionary where key is drug_name, and value is a set() where entries
#are the names of prescribers that has prescribed the drug.
cost = {}
prescriber = {}

for line in input_file:
# variable t is used to store the list where line is splited by comma
     t = line.split(',')

# the first situation: there are exactly five entries in the line and 
#there is no comma or additional quotation marks in the names
     if len(t) == 5:
          id,last_name,first_name,drug_name,drug_cost = t[0],t[1],t[2],t[3],t[4]
          
#the second situation is more complexed: doctor names or drug_names may contain 
#comma in themselves, or they are quoted by quotation marks
     elif len(t) > 5:
     
#first we look at things in the quotation mark as one word, and separate them out
          x = [z.strip() for z in line.split('"')]

#normally after separation, x will be a list of length three
          if len(x) == 3:
              component1 = x[0].split(',')
              length = len(component1)
              
              if length == 2:
#first situation: x[0] will be 'id,', x[1] will be the last_name with qutotation
#marks, x[2] will be the rest: ',first_name + drug_name + drug_cost'
                   id = component1[0]
                   last_name = x[1]
                   component2 = x[2].split(',')
                   first_name, drug_name, drug_cost = component2[1], component2[2], component2[3]
                   
#second situation: x[0] will be "id+last_name,", x[1] will be first_name with qutotation mark, 
#x[2] will be ',drug_name + drug_cost'
              elif length == 3:
                   id, last_name = component1[0], component1[1]
                   first_name = x[1]
                   component2 = x[2].split(',')
                   drug_name, drug_cost = component2[1], component2[2]

#third situation: x[0] will be "id+last_name+first_name,", x[1] will be drug_name with quotation 
#mark, and x[2] will be ',drug_cost'
              elif length == 4:
                   id, last_name, first_name = component1[0], component1[1], component1[2]
                   drug_name,drug_cost = x[1], x[2].strip(',')
                   
#the other situations are considered as missing or wrong information, and will be thrown out
     else:   
           continue

#id and drug_cost are convert from string to int and float
     id = int(id)
     name = last_name + ' ' + first_name
     drug_cost = float(drug_cost)  

# the value in the cost dictionary is used to record the total cost for a drug
     cost[drug_name] = cost.get(drug_name,0)+ drug_cost

#the prescriber names are added to a set which counts only unique prescribers
     prescriber[drug_name] = prescriber.get(drug_name,set())
     prescriber[drug_name].add(name)

#variable cost_sorted (a list) stores the information of cost in cost-descending order
cost_sorted = sorted(cost.items(), key=lambda kv: kv[1],reverse = True)

#write the required information to output_file
output_file.write('drug_name,num_prescriber,total_cost\n')

for name, value in cost_sorted:
# y will be the length of each set and the number of unique prescribers for a drug
     y = len(prescriber[name])
     output_file.write(name +','+str(y)+','+ str(value) +'\n')


     
