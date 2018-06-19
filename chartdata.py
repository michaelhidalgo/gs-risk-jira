from collections import Counter
from data import *

# Photobox Group Data

techops = 0
groupsecurity = 0
architecture = 0
productionEng = 0
photos = 0
hr = 0



for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] !='Not a Risk':
			for component in item['Components']:
				if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
					techops+=1					
				elif component['name'] == "Group-Security":
					groupsecurity+=1
				elif component['name'] == "PBX-Architecture":
					architecture+=1
				elif component['name'] == "PBX-Production-Eng":
					productionEng+=1
				elif component['name'] == "PBX-imageupload" or component['name']=="PBX-Data":
					photos+=1
				elif component['name'] == "Human Resources":
					hr+=1

techopsCount = ("TechOps {}".format(techops))
groupsecurityCount = ("Group Security {}".format(techops))
architectureCount = ("Architecture {}".format(techops))
productionEngCount = ("Production Engineering {}".format(techops))
photoCount = ("PhotoScience {}".format(techops))
hrCount = ("Human Resources {}".format(hr))
#print(techops)
#print(groupsecurity)
#print(architecture)
#print(productionEng)
#print(photos)
#print(hr)
pbxtotal = techops + groupsecurity + architecture + productionEng + photos + hr
pbxtotalCount = ("Group Total Risks {}".format(pbxtotal))
#print(pbxtotalCount)




groupLowData = []
groupMediumData = []
groupHighData = []
groupCriticalData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsCritical']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsCritical']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureCritical']+=1
				elif component['name']=="PBX-Production-Eng" :
					counter['productionengCritical']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosCritical']+=1
				elif component['name']=="Human Resources" :
					counter['hrCritical']+=1



for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsHigh']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsHigh']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureHigh']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengHigh']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosHigh']+=1
				elif component['name']=="Human Resources":
					counter['hrHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsMedium']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsMedium']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureMedium']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengMedium']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosMedium']+=1
				elif component['name']=="Human Resources":
					counter['hrMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsLow']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsLow']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureLow']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengLow']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosLow']+=1
				elif component['name']=="Human Resources":
					counter['hrLow']+=1

groupLowData.append(counter['techopsLow'])
groupLowData.append(counter['gsLow'])
groupLowData.append(counter['architectureLow'])
groupLowData.append(counter['productionengLow'])
groupLowData.append(counter['photosLow'])
groupLowData.append(counter['hrLow'])

groupMediumData.append(counter['techopsMedium'])
groupMediumData.append(counter['gsMedium'])
groupMediumData.append(counter['architectureMedium'])
groupMediumData.append(counter['productionengMedium'])
groupMediumData.append(counter['photosMedium'])
groupMediumData.append(counter['hrMedium'])

groupHighData.append(counter['techopsHigh'])
groupHighData.append(counter['gsHigh'])
groupHighData.append(counter['architectureHigh'])
groupHighData.append(counter['productionengHigh'])
groupHighData.append(counter['photosHigh'])
groupHighData.append(counter['hrHigh'])

groupCriticalData.append(counter['techopsCritical'])
groupCriticalData.append(counter['gsCritical'])
groupCriticalData.append(counter['architectureCritical'])
groupCriticalData.append(counter['productionengCritical'])
groupCriticalData.append(counter['photosCritical'])
groupCriticalData.append(counter['hrCritical'])




photoboxLowData = []
photoboxMediumData = []
photoboxHighData = []
photoboxCriticalData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelCritical']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioCritical']+=1
				elif component['name']=="PBX-Shop":
					counter['shopCritical']+=1
				elif component['name']=="PBX-checkout" :
					counter['checkoutCritical']+=1
				elif component['name']=="PBX-NativeApps" :
					counter['mobileCritical']+=1



for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelHigh']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioHigh']+=1
				elif component['name']=="PBX-Shop":
					counter['shopHigh']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutHigh']+=1
				elif component['name']=="PBX-NativeApps" :
					counter['mobileHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelMedium']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioMedium']+=1
				elif component['name']=="PBX-Shop":
					counter['shopMedium']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutMedium']+=1
				elif component['name']=="PBX-NativeApps":
					counter['mobileMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelLow']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioLow']+=1
				elif component['name']=="PBX-Shop":
					counter['shopLow']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutLow']+=1
				elif component['name']=="PBX-NativeApps":
					counter['mobileLow']+=1


photoboxLowData.append(counter['BabelLow'])
photoboxLowData.append(counter['studioLow'])
photoboxLowData.append(counter['shopLow'])
photoboxLowData.append(counter['checkoutLow'])
photoboxLowData.append(counter['mobileLow'])

photoboxMediumData.append(counter['BabelMedium'])
photoboxMediumData.append(counter['studioMedium'])
photoboxMediumData.append(counter['shopMedium'])
photoboxMediumData.append(counter['checkoutMedium'])
photoboxMediumData.append(counter['mobileMedium'])

photoboxHighData.append(counter['BabelHigh'])
photoboxHighData.append(counter['studioHigh'])
photoboxHighData.append(counter['shopHigh'])
photoboxHighData.append(counter['checkoutHigh'])
photoboxHighData.append(counter['mobileHigh'])

photoboxCriticalData.append(counter['BabelCritical'])
photoboxCriticalData.append(counter['studioCritical'])
photoboxCriticalData.append(counter['shopCritical'])
photoboxCriticalData.append(counter['checkoutCritical'])
photoboxCriticalData.append(counter['mobileCritical'])

######## NEEDS TO BE REFACTORED ####################
counter = Counter()
for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['critical_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['high_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['medium_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['low_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Info' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['info_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'To be determined' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['tbd_not_fixed']+=1

totalRisks = sum(counter.values())
#print(totalRisks)

###### Risks by Brand

gsRisks = 0
groupRisks = 0
photoboxRisks = 0
moonpigRisks = 0
hofmannRisks = 0
posterRisks = 0


for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] !='Not a Risk':
		if len(item['Components']) == 0:
			gsRisks+=1
		else:
			for component in item['Components']:
				if component['name'] == "PBX-Group-Risk":
					groupRisks+=1					
				elif component['name'] == "Photobox-Risk":
					photoboxRisks+=1
				elif component['name'] == "Moonpig-Risk":
					moonpigRisks+=1
				elif component['name'] == "Hofmann-Risk":
					hofmannRisks+=1
				elif component['name'] == "posterXXL-Risk" or component['name'] == "posterXXL":
					posterRisks+=1

photoboxCount = ("Photobox Risks {}".format(photoboxRisks))
groupCount = ("Group Risks {}".format(groupRisks))
moonpigCount = ("Moonpig Risks {}".format(moonpigRisks))
hofmannCount = ("Hofmann Risk {}".format(hofmannRisks))
posterCount = ("Poster Risk {}".format(posterRisks))
gsCount = ("Group Security under review {}".format(gsRisks))
openRisks = photoboxRisks + groupRisks + moonpigRisks +posterRisks + hofmannRisks

#print(openRisks)


#exceptions = totalRisks - openRisks
#print(exceptions)

groupData = []
moonpigData = []
photoboxData = []
posterData = []
hofmannData = []
gsData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsCritical']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupCritical']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxCritical']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigCritical']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannCritical']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['posterCritical']+=1


for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsHigh']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupHigh']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxHigh']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigHigh']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannHigh']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['posterHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsMedium']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupMedium']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxMedium']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigMedium']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannMedium']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['posterMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsLow']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupLow']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxLow']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigLow']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannLow']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['posterLow']+=1

for item in new_data['items']:
	if item['Rating'] == 'Info' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsinfo']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupinfo']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxinfo']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpiginfo']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmanninfo']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['posterinfo']+=1


for item in new_data['items']:
	if item['Rating'] == 'To be determined' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gstbd']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['grouptbd']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxtbd']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigtbd']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmanntbd']+=1
				elif component['name']=="posterXXL-Risk" or component['name'] == "posterXXL":
					counter['postertbd']+=1


groupData.append(counter['groupCritical'])
groupData.append(counter['groupHigh'])
groupData.append(counter['groupMedium'])
groupData.append(counter['groupLow'])
groupData.append(counter['groupinfo'])
groupData.append(counter['grouptbd'])
#print(groupData)

photoboxData.append(counter['photoboxCritical'])
photoboxData.append(counter['photoboxHigh'])
photoboxData.append(counter['photoboxMedium'])
photoboxData.append(counter['photoboxLow'])
photoboxData.append(counter['photoboxinfo'])
photoboxData.append(counter['photoboxtbd'])
#print(photoboxData)

moonpigData.append(counter['moonpigCritical'])
moonpigData.append(counter['moonpigHigh'])
moonpigData.append(counter['moonpigMedium'])
moonpigData.append(counter['moonpigLow'])
moonpigData.append(counter['moonpiginfo'])
moonpigData.append(counter['moonpigtbd'])
#print(moonpigData)

hofmannData.append(counter['hofmannCritical'])
hofmannData.append(counter['hofmannHigh'])
hofmannData.append(counter['hofmannMedium'])
hofmannData.append(counter['hofmannLow'])
hofmannData.append(counter['hofmanninfo'])
hofmannData.append(counter['hofmanntbd'])
#print(hofmannData)

posterData.append(counter['posterCritical'])
posterData.append(counter['posterHigh'])
posterData.append(counter['posterMedium'])
posterData.append(counter['posterLow'])
posterData.append(counter['posterinfo'])
posterData.append(counter['postertbd'])
#print(posterData)

gsData.append(counter['gsCritical'])
gsData.append(counter['gsHigh'])
gsData.append(counter['gsMedium'])
gsData.append(counter['gsLow'])
gsData.append(counter['gsinfo'])
gsData.append(counter['gstbd'])
#print(gsData)


#RISKCHART#

lowRisks = []
mediumRisks = []
highRisks = []
criticalRisks = []

for item in aprS_data['items']:
		if item['Rating'] == 'Low':
			counter['aprSLow']+=1
		elif item['Rating'] == 'Medium':
			counter['aprSMedium']+=1
		elif item['Rating'] == 'High':
			counter['aprSHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['aprSCritical']+=1

for item in mayS_data['items']:
		if item['Rating'] == 'Low':
			counter['maySLow']+=1
		elif item['Rating'] == 'Medium':
			counter['maySMedium']+=1
		elif item['Rating'] == 'High':
			counter['maySHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['maySCritical']+=1


for item in jun_data['items']:
		if item['Rating'] == 'Low':
			counter['junLow']+=1
		elif item['Rating'] == 'Medium':
			counter['junMedium']+=1
		elif item['Rating'] == 'High':
			counter['junHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['junCritical']+=1

for item in jul_data['items']:
		if item['Rating'] == 'Low':
			counter['julLow']+=1
		elif item['Rating'] == 'Medium':
			counter['julMedium']+=1
		elif item['Rating'] == 'High':
			counter['julHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['julCritical']+=1

for item in aug_data['items']:
		if item['Rating'] == 'Low':
			counter['augLow']+=1
		elif item['Rating'] == 'Medium':
			counter['augMedium']+=1
		elif item['Rating'] == 'High':
			counter['augHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['augCritical']+=1

for item in sep_data['items']:
		if item['Rating'] == 'Low':
			counter['sepLow']+=1
		elif item['Rating'] == 'Medium':
			counter['sepMedium']+=1
		elif item['Rating'] == 'High':
			counter['sepHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['sepCritical']+=1

for item in oct_data['items']:
		if item['Rating'] == 'Low':
			counter['octLow']+=1
		elif item['Rating'] == 'Medium':
			counter['octMedium']+=1
		elif item['Rating'] == 'High':
			counter['octHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['octCritical']+=1

for item in nov_data['items']:
		if item['Rating'] == 'Low':
			counter['novLow']+=1
		elif item['Rating'] == 'Medium':
			counter['novMedium']+=1
		elif item['Rating'] == 'High':
			counter['novHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['novCritical']+=1

for item in dec_data['items']:
		if item['Rating'] == 'Low':
			counter['decLow']+=1
		elif item['Rating'] == 'Medium':
			counter['decMedium']+=1
		elif item['Rating'] == 'High':
			counter['decHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['decCritical']+=1


for item in jan_data['items']:
		if item['Rating'] == 'Low':
			counter['janLow']+=1
		elif item['Rating'] == 'Medium':
			counter['janMedium']+=1
		elif item['Rating'] == 'High':
			counter['janHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['janCritical']+=1

for item in feb_data['items']:
		if item['Rating'] == 'Low':
			counter['febLow']+=1
		elif item['Rating'] == 'Medium':
			counter['febMedium']+=1
		elif item['Rating'] == 'High':
			counter['febHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['febCritical']+=1

for item in mar_data['items']:
		if item['Rating'] == 'Low':
			counter['marLow']+=1
		elif item['Rating'] == 'Medium':
			counter['marMedium']+=1
		elif item['Rating'] == 'High':
			counter['marHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['marCritical']+=1

for item in apr_data['items']:
		if item['Rating'] == 'Low':
			counter['aprLow']+=1
		elif item['Rating'] == 'Medium':
			counter['aprMedium']+=1
		elif item['Rating'] == 'High':
			counter['aprHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['aprCritical']+=1

for item in may_data['items']:
		if item['Rating'] == 'Low':
			counter['mayLow']+=1
		elif item['Rating'] == 'Medium':
			counter['mayMedium']+=1
		elif item['Rating'] == 'High':
			counter['mayHigh']+=1
		elif item['Rating'] == 'Critical':
			counter['mayCritical']+=1


lowRisks.append(counter['aprSLow'])
lowRisks.append(counter['maySLow'])
lowRisks.append(counter['junLow'])
lowRisks.append(counter['julLow'])
lowRisks.append(counter['augLow'])
lowRisks.append(counter['sepLow'])
lowRisks.append(counter['octLow'])
lowRisks.append(counter['novLow'])
lowRisks.append(counter['decLow'])
lowRisks.append(counter['janLow'])
lowRisks.append(counter['febLow'])
lowRisks.append(counter['marLow'])
lowRisks.append(counter['aprLow'])
lowRisks.append(counter['mayLow'])

mediumRisks.append(counter['aprSMedium'])
mediumRisks.append(counter['maySMedium'])
mediumRisks.append(counter['junMedium'])
mediumRisks.append(counter['julMedium'])
mediumRisks.append(counter['augMedium'])
mediumRisks.append(counter['sepMedium'])
mediumRisks.append(counter['octMedium'])
mediumRisks.append(counter['novMedium'])
mediumRisks.append(counter['decMedium'])
mediumRisks.append(counter['janMedium'])
mediumRisks.append(counter['febMedium'])
mediumRisks.append(counter['marMedium'])
mediumRisks.append(counter['aprMedium'])
mediumRisks.append(counter['mayMedium'])


highRisks.append(counter['aprSHigh'])
highRisks.append(counter['maySHigh'])
highRisks.append(counter['junHigh'])
highRisks.append(counter['julHigh'])
highRisks.append(counter['augHigh'])
highRisks.append(counter['sepHigh'])
highRisks.append(counter['octHigh'])
highRisks.append(counter['novHigh'])
highRisks.append(counter['decHigh'])
highRisks.append(counter['janHigh'])
highRisks.append(counter['febHigh'])
highRisks.append(counter['marHigh'])
highRisks.append(counter['aprHigh'])
highRisks.append(counter['mayHigh'])


criticalRisks.append(counter['aprSCritical'])
criticalRisks.append(counter['maySCritical'])
criticalRisks.append(counter['junCritical'])
criticalRisks.append(counter['julCritical'])
criticalRisks.append(counter['augCritical'])
criticalRisks.append(counter['sepCritical'])
criticalRisks.append(counter['octCritical'])
criticalRisks.append(counter['novCritical'])
criticalRisks.append(counter['decCritical'])
criticalRisks.append(counter['janCritical'])
criticalRisks.append(counter['febCritical'])
criticalRisks.append(counter['marCritical'])
criticalRisks.append(counter['aprCritical'])
criticalRisks.append(counter['mayCritical'])

lowRisksClosed = []
mediumRisksClosed = []
highRisksClosed = []
criticalRisksClosed = []

for item in aprS_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['aprSLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['aprSMediumC']+=1
		elif item['Rating'] == 'High':
			counter['aprSHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['aprSCriticalC']+=1

for item in mayS_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['maySLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['maySMediumC']+=1
		elif item['Rating'] == 'High':
			counter['maySHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['maySCriticalC']+=1

for item in jun_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['junLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['junMediumC']+=1
		elif item['Rating'] == 'High':
			counter['junHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['junCriticalC']+=1

for item in jul_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['julLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['julMediumC']+=1
		elif item['Rating'] == 'High':
			counter['julHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['julCriticalC']+=1

for item in aug_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['augLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['augMediumC']+=1
		elif item['Rating'] == 'High':
			counter['augHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['augCriticalC']+=1

for item in sep_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['sepLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['sepMediumC']+=1
		elif item['Rating'] == 'High':
			counter['sepHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['sepCriticalC']+=1

for item in oct_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['octLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['octMediumC']+=1
		elif item['Rating'] == 'High':
			counter['octHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['octCriticalC']+=1

for item in nov_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['novLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['novMediumC']+=1
		elif item['Rating'] == 'High':
			counter['novHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['novCriticalC']+=1

for item in dec_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['decLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['decMediumC']+=1
		elif item['Rating'] == 'High':
			counter['decHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['decCriticalC']+=1


for item in jan_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['janLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['janMediumC']+=1
		elif item['Rating'] == 'High':
			counter['janHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['janCriticalC']+=1

for item in feb_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['febLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['febMediumC']+=1
		elif item['Rating'] == 'High':
			counter['febHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['febCriticalC']+=1

for item in mar_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['marLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['marMediumC']+=1
		elif item['Rating'] == 'High':
			counter['marHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['marCriticalC']+=1

for item in apr_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['aprLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['aprMediumC']+=1
		elif item['Rating'] == 'High':
			counter['aprHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['aprCriticalC']+=1

for item in may_data_Closed['items']:
		if item['Rating'] == 'Low':
			counter['mayLowC']+=1
		elif item['Rating'] == 'Medium':
			counter['mayMediumC']+=1
		elif item['Rating'] == 'High':
			counter['mayHighC']+=1
		elif item['Rating'] == 'Critical':
			counter['mayCriticalC']+=1


lowRisksClosed.append(counter['aprSLowC'])
lowRisksClosed.append(counter['maySLowC'])
lowRisksClosed.append(counter['junLowC'])
lowRisksClosed.append(counter['julLowC'])
lowRisksClosed.append(counter['augLowC'])
lowRisksClosed.append(counter['sepLowC'])
lowRisksClosed.append(counter['octLowC'])
lowRisksClosed.append(counter['novLowC'])
lowRisksClosed.append(counter['decLowC'])
lowRisksClosed.append(counter['janLowC'])
lowRisksClosed.append(counter['febLowC'])
lowRisksClosed.append(counter['marLowC'])
lowRisksClosed.append(counter['aprLowC'])
lowRisksClosed.append(counter['mayLowC'])



mediumRisksClosed.append(counter['aprSMediumC'])
mediumRisksClosed.append(counter['maySMediumC'])
mediumRisksClosed.append(counter['junMediumC'])
mediumRisksClosed.append(counter['julMediumC'])
mediumRisksClosed.append(counter['augMediumC'])
mediumRisksClosed.append(counter['sepMediumC'])
mediumRisksClosed.append(counter['octMediumC'])
mediumRisksClosed.append(counter['novMediumC'])
mediumRisksClosed.append(counter['decMediumC'])
mediumRisksClosed.append(counter['janMediumC'])
mediumRisksClosed.append(counter['febMediumC'])
mediumRisksClosed.append(counter['marMediumC'])
mediumRisksClosed.append(counter['aprMediumC'])
mediumRisksClosed.append(counter['mayMediumC'])



highRisksClosed.append(counter['aprSHighC'])
highRisksClosed.append(counter['maySHighC'])
highRisksClosed.append(counter['junHighC'])
highRisksClosed.append(counter['julHighC'])
highRisksClosed.append(counter['augHighC'])
highRisksClosed.append(counter['sepHighC'])
highRisksClosed.append(counter['octHighC'])
highRisksClosed.append(counter['novHighC'])
highRisksClosed.append(counter['decHighC'])
highRisksClosed.append(counter['janHighC'])
highRisksClosed.append(counter['febHighC'])
highRisksClosed.append(counter['marHighC'])
highRisksClosed.append(counter['aprHighC'])
highRisksClosed.append(counter['mayHighC'])




criticalRisksClosed.append(counter['aprSCriticalC'])
criticalRisksClosed.append(counter['maySCriticalC'])
criticalRisksClosed.append(counter['junCriticalC'])
criticalRisksClosed.append(counter['julCriticalC'])
criticalRisksClosed.append(counter['augCriticalC'])
criticalRisksClosed.append(counter['sepCriticalC'])
criticalRisksClosed.append(counter['octCriticalC'])
criticalRisksClosed.append(counter['novCriticalC'])
criticalRisksClosed.append(counter['decCriticalC'])
criticalRisksClosed.append(counter['janCriticalC'])
criticalRisksClosed.append(counter['febCriticalC'])
criticalRisksClosed.append(counter['marCriticalC'])
criticalRisksClosed.append(counter['aprCriticalC'])
criticalRisksClosed.append(counter['mayCriticalC'])

#print(lowRisks)
#print(mediumRisks)
#print(highRisks)
#print(criticalRisks)

#print(lowRisksClosed)
#print(mediumRisksClosed)
#print(highRisksClosed)
#print(criticalRisksClosed)

#print(lowRisks)
#print(mediumRisks)
#print(highRisks)
#print(criticalRisks)

def accumulate(inarray):
   #print (inarray)
   outarray = []
   acc = 0
   for i in range(len(inarray)):
       acc = acc + inarray[i]
       outarray.append(acc)
   return outarray


testLow = (accumulate(lowRisks))
testMedium = (accumulate(mediumRisks))
testHigh = (accumulate(highRisks))
testCritical = (accumulate(criticalRisks))

#print(testLow)
#print(testMedium)
#print(testHigh)
#print(testCritical)

#print(lowRisksClosed)
#print(mediumRisksClosed)
#print(highRisksClosed)
#print(criticalRisksClosed)

riskLow = [a - b for a, b in zip(testLow, lowRisksClosed)]
riskMedium = [a - b for a, b in zip(testMedium, mediumRisksClosed)]
riskHigh = [a - b for a, b in zip(testHigh, highRisksClosed)]
riskCritical = [a - b for a, b in zip(testCritical, criticalRisksClosed)]

#print(riskLow)
#print(riskMedium)
#print(riskHigh)
#print(riskCritical)

dummyLow = [23,33,63,137,173,235,244,244,248,253,249,247,241,163]
dummyMedium = [12,26,35,44,76,82,84,83,97,104,113,125,123,115]
dummyHigh = [5,17,35,59,118,125,140,151,153,153,162,180,182,181]
dummyCritical = [0,0,0,1,0,0,0,0,0,0,0,0,0,0]

monthlyLow = [a - b for a, b in zip(lowRisks, lowRisksClosed)]
monthlyMedium = [a - b for a, b in zip(mediumRisks, mediumRisksClosed)]
monthlyHigh = [a - b for a, b in zip(highRisks, highRisksClosed)]
monthlyCritical = [a - b for a, b in zip(criticalRisks, criticalRisksClosed)]





#print(dummyCritical)
#print(dummyHigh)
#print(dummyMedium)
print(dummyLow)
