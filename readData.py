import json

f=open("jsonData/risks.json", "r")
data= f.read()
new_data = json.loads(data)

v=open("jsonData/vulns.json", "r")
vdata= v.read()
vulnData = json.loads(vdata)

#RISK DATA MONTHLY#

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

# VULNS MONTHLY DATA

aprS=open("jsonData/aprSvulns.json", "r")
aprSdata= aprS.read()
aprS_vuln = json.loads(aprSdata)

mayS=open("jsonData/maySvulns.json", "r")
maySdata= mayS.read()
mayS_vuln = json.loads(maySdata)


jun=open("jsonData/junvulns.json", "r")
jundata= jun.read()
jun_vuln = json.loads(jundata)

junC=open("jsonData/junvulnsClosed.json", "r")
jundataC= junC.read()
jun_vuln_Closed = json.loads(jundataC)

jul=open("jsonData/julvulns.json", "r")
juldata= jul.read()
jul_vuln = json.loads(juldata)

julC=open("jsonData/julvulnsClosed.json", "r")
juldataC= julC.read()
jul_vuln_Closed = json.loads(juldataC)

augR = open("jsonData/augvulns.json", "r")
augvulns = augR.read()
aug_vuln = json.loads(augvulns)

sepR = open("jsonData/sepvulns.json", "r")
sepvulns = sepR.read()
sep_vuln = json.loads(sepvulns)

octR = open("jsonData/octvulns.json", "r")
octvulns = octR.read()
oct_vuln = json.loads(octvulns)

novR = open("jsonData/novvulns.json", "r")
novvulns = novR.read()
nov_vuln = json.loads(novvulns)

decR = open("jsonData/decvulns.json", "r")
decvulns = decR.read()
dec_vuln = json.loads(decvulns)

janR = open("jsonData/janvulns.json", "r")
janvulns = janR.read()
jan_vuln = json.loads(janvulns)

febR = open("jsonData/febvulns.json", "r")
febvulns = febR.read()
feb_vuln = json.loads(febvulns)

marR = open("jsonData/marvulns.json", "r")
marvulns = marR.read()
mar_vuln = json.loads(marvulns)

aprR = open("jsonData/aprvulns.json", "r")
aprvulns = aprR.read()
apr_vuln = json.loads(aprvulns)

mayR = open("jsonData/mayvulns.json", "r")
mayvulns = mayR.read()
may_vuln = json.loads(mayvulns)


aprSC = open("jsonData/aprSvulnsClosed.json", "r")
aprSvulnsC = aprSC.read()
aprS_vuln_Closed = json.loads(aprSvulnsC)

maySC = open("jsonData/maySvulnsClosed.json", "r")
maySvulnsC = maySC.read()
mayS_vuln_Closed = json.loads(maySvulnsC)

augC = open("jsonData/augvulnsClosed.json", "r")
augvulnsC = augC.read()
aug_vuln_Closed = json.loads(augvulnsC)

sepC = open("jsonData/sepvulnsClosed.json", "r")
sepvulnsC = sepC.read()
sep_vuln_Closed = json.loads(sepvulnsC)

octC = open("jsonData/octvulnsClosed.json", "r")
octvulnsC = octC.read()
oct_vuln_Closed = json.loads(octvulnsC)

novC = open("jsonData/novvulnsClosed.json", "r")
novvulnsC = novC.read()
nov_vuln_Closed = json.loads(novvulnsC)

decC = open("jsonData/decvulnsClosed.json", "r")
decvulnsC = decC.read()
dec_vuln_Closed = json.loads(decvulnsC)

janC = open("jsonData/janvulnsClosed.json", "r")
janvulnsC = janC.read()
jan_vuln_Closed = json.loads(janvulnsC)

febC= open("jsonData/febvulnsClosed.json", "r")
febvulnsC = febC.read()
feb_vuln_Closed = json.loads(febvulnsC)

marC = open("jsonData/marvulnsClosed.json", "r")
marvulnsC = marC.read()
mar_vuln_Closed = json.loads(marvulnsC)

aprC = open("jsonData/aprvulnsClosed.json", "r")
aprvulnsC = aprC.read()
apr_vuln_Closed = json.loads(aprvulnsC)

mayC = open("jsonData/mayvulnsClosed.json", "r")
mayvulnsC = mayC.read()
may_vuln_Closed = json.loads(mayvulnsC)

