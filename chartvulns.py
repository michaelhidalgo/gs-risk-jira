from collections import Counter
from vulnData import *

counter = Counter()


lowVulns = []
mediumVulns = []
highVulns = []
criticalVulns = []

for item in aprS_vuln['items']:
		if item['Rating'] == 'Low':
			counter['aprSLow']+=1
		elif item['Rating'] == 'Medium':
			counter['aprSMedium']+=1
		elif item['Rating'] == 'High':
			counter['aprSHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['aprSCritical']+=1

for item in mayS_vuln['items']:
		if item['Rating'] == 'Low':
			counter['maySLow']+=1
		elif item['Rating'] == 'Medium':
			counter['maySMedium']+=1
		elif item['Rating'] == 'High':
			counter['maySHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['maySCritical']+=1


for item in jun_vuln['items']:
		if item['Rating'] == 'Low':
			counter['junLow']+=1
		elif item['Rating'] == 'Medium':
			counter['junMedium']+=1
		elif item['Rating'] == 'High':
			counter['junHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['junCritical']+=1

for item in jul_vuln['items']:
		if item['Rating'] == 'Low':
			counter['julLow']+=1
		elif item['Rating'] == 'Medium':
			counter['julMedium']+=1
		elif item['Rating'] == 'High':
			counter['julHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['julCritical']+=1

for item in aug_vuln['items']:
		if item['Rating'] == 'Low':
			counter['augLow']+=1
		elif item['Rating'] == 'Medium':
			counter['augMedium']+=1
		elif item['Rating'] == 'High':
			counter['augHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['augCritical']+=1

for item in sep_vuln['items']:
		if item['Rating'] == 'Low':
			counter['sepLow']+=1
		elif item['Rating'] == 'Medium':
			counter['sepMedium']+=1
		elif item['Rating'] == 'High':
			counter['sepHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['sepCritical']+=1

for item in oct_vuln['items']:
		if item['Rating'] == 'Low':
			counter['octLow']+=1
		elif item['Rating'] == 'Medium':
			counter['octMedium']+=1
		elif item['Rating'] == 'High':
			counter['octHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['octCritical']+=1

for item in nov_vuln['items']:
		if item['Rating'] == 'Low':
			counter['novLow']+=1
		elif item['Rating'] == 'Medium':
			counter['novMedium']+=1
		elif item['Rating'] == 'High':
			counter['novHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['novCritical']+=1

for item in dec_vuln['items']:
		if item['Rating'] == 'Low':
			counter['decLow']+=1
		elif item['Rating'] == 'Medium':
			counter['decMedium']+=1
		elif item['Rating'] == 'High':
			counter['decHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['decCritical']+=1


for item in jan_vuln['items']:
		if item['Rating'] == 'Low':
			counter['janLow']+=1
		elif item['Rating'] == 'Medium':
			counter['janMedium']+=1
		elif item['Rating'] == 'High':
			counter['janHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['janCritical']+=1

for item in feb_vuln['items']:
		if item['Rating'] == 'Low':
			counter['febLow']+=1
		elif item['Rating'] == 'Medium':
			counter['febMedium']+=1
		elif item['Rating'] == 'High':
			counter['febHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['febCritical']+=1

for item in mar_vuln['items']:
		if item['Rating'] == 'Low':
			counter['marLow']+=1
		elif item['Rating'] == 'Medium':
			counter['marMedium']+=1
		elif item['Rating'] == 'High':
			counter['marHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['marCritical']+=1

for item in apr_vuln['items']:
		if item['Rating'] == 'Low':
			counter['aprLow']+=1
		elif item['Rating'] == 'Medium':
			counter['aprMedium']+=1
		elif item['Rating'] == 'High':
			counter['aprHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['aprCritical']+=1

for item in may_vuln['items']:
		if item['Rating'] == 'Low':
			counter['mayLow']+=1
		elif item['Rating'] == 'Medium':
			counter['mayMedium']+=1
		elif item['Rating'] == 'High':
			counter['mayHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['mayCritical']+=1


lowVulns.append(counter['aprSLow'])
lowVulns.append(counter['maySLow'])
lowVulns.append(counter['junLow'])
lowVulns.append(counter['julLow'])
lowVulns.append(counter['augLow'])
lowVulns.append(counter['sepLow'])
lowVulns.append(counter['octLow'])
lowVulns.append(counter['novLow'])
lowVulns.append(counter['decLow'])
lowVulns.append(counter['janLow'])
lowVulns.append(counter['febLow'])
lowVulns.append(counter['marLow'])
lowVulns.append(counter['aprLow'])
lowVulns.append(counter['mayLow'])

mediumVulns.append(counter['aprSMedium'])
mediumVulns.append(counter['maySMedium'])
mediumVulns.append(counter['junMedium'])
mediumVulns.append(counter['julMedium'])
mediumVulns.append(counter['augMedium'])
mediumVulns.append(counter['sepMedium'])
mediumVulns.append(counter['octMedium'])
mediumVulns.append(counter['novMedium'])
mediumVulns.append(counter['decMedium'])
mediumVulns.append(counter['janMedium'])
mediumVulns.append(counter['febMedium'])
mediumVulns.append(counter['marMedium'])
mediumVulns.append(counter['aprMedium'])
mediumVulns.append(counter['mayMedium'])


highVulns.append(counter['aprSHigh'])
highVulns.append(counter['maySHigh'])
highVulns.append(counter['junHigh'])
highVulns.append(counter['julHigh'])
highVulns.append(counter['augHigh'])
highVulns.append(counter['sepHigh'])
highVulns.append(counter['octHigh'])
highVulns.append(counter['novHigh'])
highVulns.append(counter['decHigh'])
highVulns.append(counter['janHigh'])
highVulns.append(counter['febHigh'])
highVulns.append(counter['marHigh'])
highVulns.append(counter['aprHigh'])
highVulns.append(counter['mayHigh'])


criticalVulns.append(counter['aprSCritical'])
criticalVulns.append(counter['maySCritical'])
criticalVulns.append(counter['junCritical'])
criticalVulns.append(counter['julCritical'])
criticalVulns.append(counter['augCritical'])
criticalVulns.append(counter['sepCritical'])
criticalVulns.append(counter['octCritical'])
criticalVulns.append(counter['novCritical'])
criticalVulns.append(counter['decCritical'])
criticalVulns.append(counter['janCritical'])
criticalVulns.append(counter['febCritical'])
criticalVulns.append(counter['marCritical'])
criticalVulns.append(counter['aprCritical'])
criticalVulns.append(counter['mayCritical'])

lowVulnsClosed = []
mediumVulnsClosed = []
highVulnsClosed = []
criticalVulnsClosed = []

for item in aprS_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['aprSLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['aprSMediumC']+=1
		elif item['Rating'] == 'High':
			counter['aprSHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['aprSCriticalC']+=1

for item in mayS_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['maySLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['maySMediumC']+=1
		elif item['Rating'] == 'High':
			counter['maySHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['maySCriticalC']+=1

for item in jun_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['junLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['junMediumC']+=1
		elif item['Rating'] == 'High':
			counter['junHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['junCriticalC']+=1

for item in jul_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['julLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['julMediumC']+=1
		elif item['Rating'] == 'High':
			counter['julHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['julCriticalC']+=1

for item in aug_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['augLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['augMediumC']+=1
		elif item['Rating'] == 'High':
			counter['augHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['augCriticalC']+=1

for item in sep_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['sepLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['sepMediumC']+=1
		elif item['Rating'] == 'High':
			counter['sepHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['sepCriticalC']+=1

for item in oct_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['octLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['octMediumC']+=1
		elif item['Rating'] == 'High':
			counter['octHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['octCriticalC']+=1

for item in nov_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['novLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['novMediumC']+=1
		elif item['Rating'] == 'High':
			counter['novHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['novCriticalC']+=1

for item in dec_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['decLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['decMediumC']+=1
		elif item['Rating'] == 'High':
			counter['decHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['decCriticalC']+=1


for item in jan_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['janLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['janMediumC']+=1
		elif item['Rating'] == 'High':
			counter['janHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['janCriticalC']+=1

for item in feb_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['febLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['febMediumC']+=1
		elif item['Rating'] == 'High':
			counter['febHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['febCriticalC']+=1

for item in mar_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['marLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['marMediumC']+=1
		elif item['Rating'] == 'High':
			counter['marHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['marCriticalC']+=1

for item in apr_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['aprLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['aprMediumC']+=1
		elif item['Rating'] == 'High':
			counter['aprHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['aprCriticalC']+=1

for item in may_vuln_Closed['items']:
		if item['Rating'] == 'Low':
			counter['mayLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['mayMediumC']+=1
		elif item['Rating'] == 'High':
			counter['mayHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['mayCriticalC']+=1


lowVulnsClosed.append(counter['aprSLowC'])
lowVulnsClosed.append(counter['maySLowC'])
lowVulnsClosed.append(counter['junLowC'])
lowVulnsClosed.append(counter['julLowC'])
lowVulnsClosed.append(counter['augLowC'])
lowVulnsClosed.append(counter['sepLowC'])
lowVulnsClosed.append(counter['octLowC'])
lowVulnsClosed.append(counter['novLowC'])
lowVulnsClosed.append(counter['decLowC'])
lowVulnsClosed.append(counter['janLowC'])
lowVulnsClosed.append(counter['febLowC'])
lowVulnsClosed.append(counter['marLowC'])
lowVulnsClosed.append(counter['aprLowC'])
lowVulnsClosed.append(counter['mayLowC'])



mediumVulnsClosed.append(counter['aprSMediumC'])
mediumVulnsClosed.append(counter['maySMediumC'])
mediumVulnsClosed.append(counter['junMediumC'])
mediumVulnsClosed.append(counter['julMediumC'])
mediumVulnsClosed.append(counter['augMediumC'])
mediumVulnsClosed.append(counter['sepMediumC'])
mediumVulnsClosed.append(counter['octMediumC'])
mediumVulnsClosed.append(counter['novMediumC'])
mediumVulnsClosed.append(counter['decMediumC'])
mediumVulnsClosed.append(counter['janMediumC'])
mediumVulnsClosed.append(counter['febMediumC'])
mediumVulnsClosed.append(counter['marMediumC'])
mediumVulnsClosed.append(counter['aprMediumC'])
mediumVulnsClosed.append(counter['mayMediumC'])



highVulnsClosed.append(counter['aprSHighC'])
highVulnsClosed.append(counter['maySHighC'])
highVulnsClosed.append(counter['junHighC'])
highVulnsClosed.append(counter['julHighC'])
highVulnsClosed.append(counter['augHighC'])
highVulnsClosed.append(counter['sepHighC'])
highVulnsClosed.append(counter['octHighC'])
highVulnsClosed.append(counter['novHighC'])
highVulnsClosed.append(counter['decHighC'])
highVulnsClosed.append(counter['janHighC'])
highVulnsClosed.append(counter['febHighC'])
highVulnsClosed.append(counter['marHighC'])
highVulnsClosed.append(counter['aprHighC'])
highVulnsClosed.append(counter['mayHighC'])




criticalVulnsClosed.append(counter['aprSCriticalC'])
criticalVulnsClosed.append(counter['maySCriticalC'])
criticalVulnsClosed.append(counter['junCriticalC'])
criticalVulnsClosed.append(counter['julCriticalC'])
criticalVulnsClosed.append(counter['augCriticalC'])
criticalVulnsClosed.append(counter['sepCriticalC'])
criticalVulnsClosed.append(counter['octCriticalC'])
criticalVulnsClosed.append(counter['novCriticalC'])
criticalVulnsClosed.append(counter['decCriticalC'])
criticalVulnsClosed.append(counter['janCriticalC'])
criticalVulnsClosed.append(counter['febCriticalC'])
criticalVulnsClosed.append(counter['marCriticalC'])
criticalVulnsClosed.append(counter['aprCriticalC'])
criticalVulnsClosed.append(counter['mayCriticalC'])

#print(lowVulns)
#print(mediumVulns)
#print(highVulns)
#print(criticalVulns)

#print(lowVulnsClosed)
#print(mediumVulnsClosed)
#print(highVulnsClosed)
#print(criticalVulnsClosed)

#print(lowVulns)
#print(mediumVulns)
#print(highVulns)
#print(criticalVulns)

def accumulate(inarray):
   #print (inarray)
   outarray = []
   acc = 0
   for i in range(len(inarray)):
       acc = acc + inarray[i]
       outarray.append(acc)
   return outarray


testLow = (accumulate(lowVulns))
testMedium = (accumulate(mediumVulns))
testHigh = (accumulate(highVulns))
testCritical = (accumulate(criticalVulns))

#print(testLow)
#print(testMedium)
#print(testHigh)
#print(testCritical)
#print(lowVulnsClosed)
#print(mediumVulnsClosed)
#print(highVulnsClosed)
#print(criticalVulnsClosed)

vulnLow = [a - b for a, b in zip(testLow, lowVulnsClosed)]
vulnMedium = [a - b for a, b in zip(testMedium, mediumVulnsClosed)]
vulnHigh = [a - b for a, b in zip(testHigh, highVulnsClosed)]
vulnCritical = [a - b for a, b in zip(testCritical, criticalVulnsClosed)]

#print(vulnLow)
#print(vulnMedium)
#print(vulnHigh)
#print(vulnCritical)

#dummyLow = [16,23,30,38,46,48,62,82,85,82,82]
#dummyMedium = []
#dummyHigh = []
#dummyCritical = []

monthlyLow = [a - b for a, b in zip(lowVulns, lowVulnsClosed)]
monthlyMedium = [a - b for a, b in zip(mediumVulns, mediumVulnsClosed)]
monthlyHigh = [a - b for a, b in zip(highVulns, highVulnsClosed)]
monthlyCritical = [a - b for a, b in zip(criticalVulns, criticalVulnsClosed)]


#print(monthlyCritical)