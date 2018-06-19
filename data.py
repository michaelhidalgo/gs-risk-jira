import json

f=open("risks.json", "r")
data= f.read()
new_data = json.loads(data)

r=open("projects.json", "r")
pdata= r.read()
projectData = json.loads(pdata)

v=open("vulns.json", "r")
vdata= v.read()
vulnData = json.loads(vdata)


#RISK DATA#

aprS=open("jsonData/aprSrisks.json", "r")
aprSdata= aprS.read()
aprS_data = json.loads(aprSdata)

mayS=open("jsonData/maySrisks.json", "r")
maySdata= mayS.read()
mayS_data = json.loads(maySdata)


jun=open("jsonData/junrisks.json", "r")
jundata= jun.read()
jun_data = json.loads(jundata)

junC=open("jsonData/junrisksClosed.json", "r")
jundataC= junC.read()
jun_data_Closed = json.loads(jundataC)

jul=open("jsonData/julrisks.json", "r")
juldata= jul.read()
jul_data = json.loads(juldata)

julC=open("jsonData/julrisksClosed.json", "r")
juldataC= julC.read()
jul_data_Closed = json.loads(juldataC)

augR = open("jsonData/augrisks.json", "r")
augRisks = augR.read()
aug_data = json.loads(augRisks)

sepR = open("jsonData/seprisks.json", "r")
sepRisks = sepR.read()
sep_data = json.loads(sepRisks)

octR = open("jsonData/octrisks.json", "r")
octRisks = octR.read()
oct_data = json.loads(octRisks)

novR = open("jsonData/novrisks.json", "r")
novRisks = novR.read()
nov_data = json.loads(novRisks)

decR = open("jsonData/decrisks.json", "r")
decRisks = decR.read()
dec_data = json.loads(decRisks)

janR = open("jsonData/janrisks.json", "r")
janRisks = janR.read()
jan_data = json.loads(janRisks)

febR = open("jsonData/febrisks.json", "r")
febRisks = febR.read()
feb_data = json.loads(febRisks)

marR = open("jsonData/marrisks.json", "r")
marRisks = marR.read()
mar_data = json.loads(marRisks)

aprR = open("jsonData/aprrisks.json", "r")
aprRisks = aprR.read()
apr_data = json.loads(aprRisks)

mayR = open("jsonData/mayrisks.json", "r")
mayRisks = mayR.read()
may_data = json.loads(mayRisks)


aprSC = open("jsonData/aprSrisksClosed.json", "r")
aprSRisksC = aprSC.read()
aprS_data_Closed = json.loads(aprSRisksC)

maySC = open("jsonData/maySrisksClosed.json", "r")
maySRisksC = maySC.read()
mayS_data_Closed = json.loads(maySRisksC)

augC = open("jsonData/augrisksClosed.json", "r")
augRisksC = augC.read()
aug_data_Closed = json.loads(augRisksC)

sepC = open("jsonData/seprisksClosed.json", "r")
sepRisksC = sepC.read()
sep_data_Closed = json.loads(sepRisksC)

octC = open("jsonData/octrisksClosed.json", "r")
octRisksC = octC.read()
oct_data_Closed = json.loads(octRisksC)

novC = open("jsonData/novrisksClosed.json", "r")
novRisksC = novC.read()
nov_data_Closed = json.loads(novRisksC)

decC = open("jsonData/decrisksClosed.json", "r")
decRisksC = decC.read()
dec_data_Closed = json.loads(decRisksC)

janC = open("jsonData/janrisksClosed.json", "r")
janRisksC = janC.read()
jan_data_Closed = json.loads(janRisksC)

febC= open("jsonData/febrisksClosed.json", "r")
febRisksC = febC.read()
feb_data_Closed = json.loads(febRisksC)

marC = open("jsonData/marrisksClosed.json", "r")
marRisksC = marC.read()
mar_data_Closed = json.loads(marRisksC)

aprC = open("jsonData/aprrisksClosed.json", "r")
aprRisksC = aprC.read()
apr_data_Closed = json.loads(aprRisksC)

mayC = open("jsonData/mayrisksClosed.json", "r")
mayRisksC = mayC.read()
may_data_Closed = json.loads(mayRisksC)



