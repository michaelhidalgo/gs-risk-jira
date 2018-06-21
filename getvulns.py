import json
from jira import JIRA
from config import basic_auth


options = {'server': 'https://jira.photobox.com'}
jira = JIRA(options, basic_auth=basic_auth)

vulns = jira.search_issues('project = VULN', maxResults=2000)

myvulns = {"items":[{"Key":vuln.key,
				   "Summary": vuln.fields.summary,
				   "Status":vuln.fields.status.name,
				   "Rating":vuln.fields.customfield_12639.value,
				   "Description":vuln.fields.description,
				   "Components":[{"name":i.name}for i in vuln.fields.components]}  
				   for vuln in vulns]}

with open('jsonData/vulns.json','w')as outfile:
 	json.dump(myvulns, outfile, indent=4)




aprvulnsS = jira.search_issues('project = VULN and created >= "2017/04/01" and created <= "2017/04/30"',maxResults=2000)

myaprS = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprvulnsS]}

with open('jsonData/aprSvulns.json','w') as outfile:
    json.dump(myaprS, outfile, indent=4)

mayvulnsS = jira.search_issues('project = VULN and created >= "2017/05/01" and created <= "2017/05/31"',maxResults=2000)

mymayS = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayvulnsS]}

with open('jsonData/maySvulns.json','w') as outfile:
    json.dump(mymayS, outfile, indent=4)


junvulns = jira.search_issues('project = VULN and created >= "2017/06/01" and created <= "2017/06/30"',maxResults=2000)

myjun = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in junvulns]}

with open('jsonData/junvulns.json','w') as outfile:
    json.dump(myjun, outfile, indent=4)

julvulns = jira.search_issues('project = VULN and created >= "2017/07/01" and created <= "2017/07/31"',maxResults=2000)

myjul = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in julvulns]}

with open('jsonData/julvulns.json','w') as outfile:
    json.dump(myjul, outfile, indent=4)


augvulns = jira.search_issues('project = VULN and created >= "2017/08/01" and created <= "2017/08/31"',maxResults=2000)

myaug = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in augvulns]}


with open('jsonData/augvulns.json','w') as outfile:
    json.dump(myaug, outfile, indent=4)

sepvulns = jira.search_issues('project = VULN and created >= "2017/09/01" and created <= "2017/09/30"',maxResults=2000)

mysep = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in sepvulns]}


with open('jsonData/sepvulns.json','w') as outfile:
    json.dump(mysep, outfile, indent=4)

octvulns = jira.search_issues('project = VULN and created >= "2017/10/01" and created <= "2017/10/31"',maxResults=2000)

myoct = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in octvulns]}


with open('jsonData/octvulns.json','w') as outfile:
    json.dump(myoct, outfile, indent=4)

novvulns = jira.search_issues('project = VULN and created >= "2017/11/01" and created <= "2017/11/30"',maxResults=2000)

mynov = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in novvulns]}


with open('jsonData/novvulns.json','w') as outfile:
    json.dump(mynov, outfile, indent=4)

decvulns = jira.search_issues('project = VULN and created >= "2017/12/01" and created <= "2017/12/31"',maxResults=2000)

mydec = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in decvulns]}


with open('jsonData/decvulns.json','w') as outfile:
    json.dump(mydec, outfile, indent=4)


janvulns = jira.search_issues('project = VULN and created >= "2018/01/01" and created <= "2018/01/31"',maxResults=2000)

myjan = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in janvulns]}


with open('jsonData/janvulns.json','w') as outfile:
    json.dump(myjan, outfile, indent=4)


febvulns = jira.search_issues('project = VULN and created >= "2018/02/01" and created <= "2018/02/28"',maxResults=2000)

myfeb = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in febvulns]}


with open('jsonData/febvulns.json','w') as outfile:
    json.dump(myfeb, outfile, indent=4)

marvulns = jira.search_issues('project = VULN and created >= "2018/03/01" and created <= "2018/03/31"',maxResults=2000)

mymar = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in marvulns]}


with open('jsonData/marvulns.json','w') as outfile:
    json.dump(mymar, outfile, indent=4)


aprvulns = jira.search_issues('project = VULN and created >= "2018/04/01" and created <= "2018/04/30"',maxResults=2000)

myapr = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprvulns]}


with open('jsonData/aprvulns.json','w') as outfile:
    json.dump(myapr, outfile, indent=4)

mayvulns = jira.search_issues('project = VULN and created >= "2018/05/01" and created <= "2018/05/31"',maxResults=2000)

mymay = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayvulns]}


with open('jsonData/mayvulns.json','w') as outfile:
    json.dump(mymay, outfile, indent=4)

##################### CLOSED DATA ###################################

aprSvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/04/01","2017/04/30")',maxResults=2000)

myaprSC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprSvulnsClosed]}


with open('jsonData/aprSvulnsClosed.json','w') as outfile:
    json.dump(myaprSC, outfile, indent=4)

maySvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/05/01","2017/05/31")',maxResults=2000)

mymaySC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in maySvulnsClosed]}


with open('jsonData/maySvulnsClosed.json','w') as outfile:
    json.dump(mymaySC, outfile, indent=4)




junvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/06/01","2017/06/30")',maxResults=2000)

myjunC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in junvulnsClosed]}


with open('jsonData/junvulnsClosed.json','w') as outfile:
    json.dump(myjunC, outfile, indent=4)

julvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/07/01","2017/07/31")',maxResults=2000)

myjulC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in julvulnsClosed]}


with open('jsonData/julvulnsClosed.json','w') as outfile:
    json.dump(myjulC, outfile, indent=4)

augvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/08/01","2017/08/31")',maxResults=2000)

myaugC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in augvulnsClosed]}


with open('jsonData/augvulnsClosed.json','w') as outfile:
    json.dump(myaugC, outfile, indent=4)

sepvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/09/01","2017/09/30")',maxResults=2000)

mysepC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in sepvulnsClosed]}


with open('jsonData/sepvulnsClosed.json','w') as outfile:
    json.dump(mysepC, outfile, indent=4)

octvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/10/01","2017/10/31")',maxResults=2000)

myoctC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in octvulnsClosed]}


with open('jsonData/octvulnsClosed.json','w') as outfile:
    json.dump(myoctC, outfile, indent=4)


novvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/11/01","2017/11/30")',maxResults=2000)

mynovC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in novvulnsClosed]}


with open('jsonData/novvulnsClosed.json','w') as outfile:
    json.dump(mynovC, outfile, indent=4)

decvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2017/12/01","2017/12/31")',maxResults=2000)

mydecC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in decvulnsClosed]}


with open('jsonData/decvulnsClosed.json','w') as outfile:
    json.dump(mydecC, outfile, indent=4)

janvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2018/01/01","2018/01/31")',maxResults=2000)

myjanC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in janvulnsClosed]}


with open('jsonData/janvulnsClosed.json','w') as outfile:
    json.dump(myjanC, outfile, indent=4)

febvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2018/02/01","2018/02/28")',maxResults=2000)

myfebC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in febvulnsClosed]}


with open('jsonData/febvulnsClosed.json','w') as outfile:
    json.dump(myfebC, outfile, indent=4)

marvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2018/03/01","2018/03/31")',maxResults=2000)

mymarC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in marvulnsClosed]}


with open('jsonData/marvulnsClosed.json','w') as outfile:
    json.dump(myfebC, outfile, indent=4)

aprvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2018/04/01","2018/04/30")',maxResults=2000)

myaprC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprvulnsClosed]}


with open('jsonData/aprvulnsClosed.json','w') as outfile:
    json.dump(myaprC, outfile, indent=4)

mayvulnsClosed = jira.search_issues('project = VULN AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance","Fixed by team","GS Review","Fixed") to ("Not a Risk","Closed","Done","Fixed","Fixed by team") during ("2018/05/01","2018/05/31")',maxResults=2000)

mymayC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayvulnsClosed]}


with open('jsonData/mayvulnsClosed.json','w') as outfile:
    json.dump(mymayC, outfile, indent=4)