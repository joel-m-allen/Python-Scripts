import csv
import sys
from operator import itemgetter

f = open("csv.txt", "rb")
lines = f.readlines()[1:]

list_of_lines = []
total_by_name={}
total_cash_by_name={}

reader = csv.reader(lines)

for row in reader:

    list_of_lines.append(row)    
    
    #order
    #print row
    row[4] = row[4].replace("$","")
    if row[2] not in total_by_name:
        total_by_name[row[2]]=1
        total_cash_by_name[row[2]] = float(row[4])
        
    else:
        total_by_name[row[2]] = total_by_name[row[2]]+1
        
        total_cash_by_name[row[2]] =total_cash_by_name[row[2]]+float(row[4]) 
        
    #dict_list.append(row)

out = open("output.txt", "w")
print "Sorted orders, by person:"
#out.write("Sorted orders, by person:")

for line in sorted(list_of_lines, key=itemgetter(2)):
    print line
   # out.write(line)
print "\nNumber of Orders, by Person:"
#out.write("\nNumber of Orders, by Person:")
for w in sorted(total_by_name, key=total_by_name.get, reverse=True):
    print w, "\t", total_by_name[w]
    #out.write(w, "\t", total_by_name[w], total_cash_by_name[w])
print "\nAverage cost of Orders, by Person:"
#out.write("\nAverage cost of Orders, by Person:")
for w in sorted(total_by_name, key=total_by_name.get, reverse=True):
    print w,"\t", total_cash_by_name[w]/total_by_name[w]
    #out.write(w,"\t", total_cash_by_name[w]/total_by_name[w])



