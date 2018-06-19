import json
from jira import JIRA
from config import basic_auth


options = {'server': 'https://jira.photobox.com'}
jira = JIRA(options, basic_auth=basic_auth)

aprrisksS = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/04/01" and created <= "2017/04/30"',maxResults=2000)

myaprS = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprrisksS]}

with open('jsonData/aprSrisks.json','w') as outfile:
    json.dump(myaprS, outfile, indent=4)

mayrisksS = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/05/01" and created <= "2017/05/31"',maxResults=2000)

mymayS = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayrisksS]}

with open('jsonData/maySrisks.json','w') as outfile:
    json.dump(mymayS, outfile, indent=4)


junrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/06/01" and created <= "2017/06/30"',maxResults=2000)

myjun = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in junrisks]}

with open('jsonData/junrisks.json','w') as outfile:
    json.dump(myjun, outfile, indent=4)

julrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/07/01" and created <= "2017/07/31"',maxResults=2000)

myjul = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in julrisks]}

with open('jsonData/julrisks.json','w') as outfile:
    json.dump(myjul, outfile, indent=4)


augrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/08/01" and created <= "2017/08/31"',maxResults=2000)

myaug = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in augrisks]}


with open('jsonData/augrisks.json','w') as outfile:
    json.dump(myaug, outfile, indent=4)

seprisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/09/01" and created <= "2017/09/30"',maxResults=2000)

mysep = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in seprisks]}


with open('jsonData/seprisks.json','w') as outfile:
    json.dump(mysep, outfile, indent=4)

octrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/10/01" and created <= "2017/10/31"',maxResults=2000)

myoct = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in octrisks]}


with open('jsonData/octrisks.json','w') as outfile:
    json.dump(myoct, outfile, indent=4)

novrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/11/01" and created <= "2017/11/30"',maxResults=2000)

mynov = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in novrisks]}


with open('jsonData/novrisks.json','w') as outfile:
    json.dump(mynov, outfile, indent=4)

decrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2017/12/01" and created <= "2017/12/31"',maxResults=2000)

mydec = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in decrisks]}


with open('jsonData/decrisks.json','w') as outfile:
    json.dump(mydec, outfile, indent=4)


janrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2018/01/01" and created <= "2018/01/31"',maxResults=2000)

myjan = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in janrisks]}


with open('jsonData/janrisks.json','w') as outfile:
    json.dump(myjan, outfile, indent=4)


febrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2018/02/01" and created <= "2018/02/28"',maxResults=2000)

myfeb = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in febrisks]}


with open('jsonData/febrisks.json','w') as outfile:
    json.dump(myfeb, outfile, indent=4)

marrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2018/03/01" and created <= "2018/03/31"',maxResults=2000)

mymar = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in marrisks]}


with open('jsonData/marrisks.json','w') as outfile:
    json.dump(mymar, outfile, indent=4)


aprrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2018/04/01" and created <= "2018/04/30"',maxResults=2000)

myapr = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprrisks]}


with open('jsonData/aprrisks.json','w') as outfile:
    json.dump(myapr, outfile, indent=4)

mayrisks = jira.search_issues('project = RISK and issuetype = Risk and created >= "2018/05/01" and created <= "2018/05/31"',maxResults=2000)

mymay = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayrisks]}


with open('jsonData/mayrisks.json','w') as outfile:
    json.dump(mymay, outfile, indent=4)

##################### CLOSED DATA ###################################

aprSrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/04/01","2017/04/30")',maxResults=2000)

myaprSC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprSrisksClosed]}


with open('jsonData/aprSrisksClosed.json','w') as outfile:
    json.dump(myaprSC, outfile, indent=4)

maySrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/05/01","2017/05/31")',maxResults=2000)

mymaySC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in maySrisksClosed]}


with open('jsonData/maySrisksClosed.json','w') as outfile:
    json.dump(mymaySC, outfile, indent=4)




junrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/06/01","2017/06/30")',maxResults=2000)

myjunC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in junrisksClosed]}


with open('jsonData/junrisksClosed.json','w') as outfile:
    json.dump(myjunC, outfile, indent=4)

julrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/07/01","2017/07/31")',maxResults=2000)

myjulC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in julrisksClosed]}


with open('jsonData/julrisksClosed.json','w') as outfile:
    json.dump(myjulC, outfile, indent=4)

augrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/08/01","2017/08/31")',maxResults=2000)

myaugC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in augrisksClosed]}


with open('jsonData/augrisksClosed.json','w') as outfile:
    json.dump(myaugC, outfile, indent=4)

seprisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/09/01","2017/09/30")',maxResults=2000)

mysepC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in seprisksClosed]}


with open('jsonData/seprisksClosed.json','w') as outfile:
    json.dump(mysepC, outfile, indent=4)

octrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/10/01","2017/10/31")',maxResults=2000)

myoctC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in octrisksClosed]}


with open('jsonData/octrisksClosed.json','w') as outfile:
    json.dump(myoctC, outfile, indent=4)


novrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/11/01","2017/11/30")',maxResults=2000)

mynovC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in novrisksClosed]}


with open('jsonData/novrisksClosed.json','w') as outfile:
    json.dump(mynovC, outfile, indent=4)

decrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2017/12/01","2017/12/31")',maxResults=2000)

mydecC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in decrisksClosed]}


with open('jsonData/decrisksClosed.json','w') as outfile:
    json.dump(mydecC, outfile, indent=4)

janrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2018/01/01","2018/01/31")',maxResults=2000)

myjanC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in janrisksClosed]}


with open('jsonData/janrisksClosed.json','w') as outfile:
    json.dump(myjanC, outfile, indent=4)

febrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2018/02/01","2018/02/28")',maxResults=2000)

myfebC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in febrisksClosed]}


with open('jsonData/febrisksClosed.json','w') as outfile:
    json.dump(myfebC, outfile, indent=4)

marrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2018/03/01","2018/03/31")',maxResults=2000)

mymarC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in marrisksClosed]}


with open('jsonData/marrisksClosed.json','w') as outfile:
    json.dump(myfebC, outfile, indent=4)

aprrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2018/04/01","2018/04/30")',maxResults=2000)

myaprC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in aprrisksClosed]}


with open('jsonData/aprrisksClosed.json','w') as outfile:
    json.dump(myaprC, outfile, indent=4)

mayrisksClosed = jira.search_issues('project = RISK and issuetype = "Risk" AND Status CHANGED FROM ("Not a Risk","Test Fix", "Open","In Progress","Risk Approved","Accepted","Awaiting Acceptance") to ("Not a Risk","Closed","Done","Fixed") during ("2018/05/01","2018/05/31")',maxResults=2000)

mymayC = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value} 
				  for issue in mayrisksClosed]}


with open('jsonData/mayrisksClosed.json','w') as outfile:
    json.dump(mymayC, outfile, indent=4)