import csv 
with open('/Users/ruth/Desktop/coding/python/c-105/class1.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
totalMarks = 0
totalEntries = len(fileData)
for marks in fileData:
    totalMarks+= float(marks[1])
mean = totalMarks/totalEntries
print('The mean is:'+str(mean))


