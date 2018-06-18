import json	


aprS=open("vulnData/aprSvulns.json", "r")
aprSdata= aprS.read()
aprS_vuln = json.loads(aprSdata)

mayS=open("vulnData/maySvulns.json", "r")
maySdata= mayS.read()
mayS_vuln = json.loads(maySdata)


jun=open("vulnData/junvulns.json", "r")
jundata= jun.read()
jun_vuln = json.loads(jundata)

junC=open("vulnData/junvulnsClosed.json", "r")
jundataC= junC.read()
jun_vuln_Closed = json.loads(jundataC)

jul=open("vulnData/julvulns.json", "r")
juldata= jul.read()
jul_vuln = json.loads(juldata)

julC=open("vulnData/julvulnsClosed.json", "r")
juldataC= julC.read()
jul_vuln_Closed = json.loads(juldataC)

augR = open("vulnData/augvulns.json", "r")
augvulns = augR.read()
aug_vuln = json.loads(augvulns)

sepR = open("vulnData/sepvulns.json", "r")
sepvulns = sepR.read()
sep_vuln = json.loads(sepvulns)

octR = open("vulnData/octvulns.json", "r")
octvulns = octR.read()
oct_vuln = json.loads(octvulns)

novR = open("vulnData/novvulns.json", "r")
novvulns = novR.read()
nov_vuln = json.loads(novvulns)

decR = open("vulnData/decvulns.json", "r")
decvulns = decR.read()
dec_vuln = json.loads(decvulns)

janR = open("vulnData/janvulns.json", "r")
janvulns = janR.read()
jan_vuln = json.loads(janvulns)

febR = open("vulnData/febvulns.json", "r")
febvulns = febR.read()
feb_vuln = json.loads(febvulns)

marR = open("vulnData/marvulns.json", "r")
marvulns = marR.read()
mar_vuln = json.loads(marvulns)

aprR = open("vulnData/aprvulns.json", "r")
aprvulns = aprR.read()
apr_vuln = json.loads(aprvulns)

mayR = open("vulnData/mayvulns.json", "r")
mayvulns = mayR.read()
may_vuln = json.loads(mayvulns)


aprSC = open("vulnData/aprSvulnsClosed.json", "r")
aprSvulnsC = aprSC.read()
aprS_vuln_Closed = json.loads(aprSvulnsC)

maySC = open("vulnData/maySvulnsClosed.json", "r")
maySvulnsC = maySC.read()
mayS_vuln_Closed = json.loads(maySvulnsC)

augC = open("vulnData/augvulnsClosed.json", "r")
augvulnsC = augC.read()
aug_vuln_Closed = json.loads(augvulnsC)

sepC = open("vulnData/sepvulnsClosed.json", "r")
sepvulnsC = sepC.read()
sep_vuln_Closed = json.loads(sepvulnsC)

octC = open("vulnData/octvulnsClosed.json", "r")
octvulnsC = octC.read()
oct_vuln_Closed = json.loads(octvulnsC)

novC = open("vulnData/novvulnsClosed.json", "r")
novvulnsC = novC.read()
nov_vuln_Closed = json.loads(novvulnsC)

decC = open("vulnData/decvulnsClosed.json", "r")
decvulnsC = decC.read()
dec_vuln_Closed = json.loads(decvulnsC)

janC = open("vulnData/janvulnsClosed.json", "r")
janvulnsC = janC.read()
jan_vuln_Closed = json.loads(janvulnsC)

febC= open("vulnData/febvulnsClosed.json", "r")
febvulnsC = febC.read()
feb_vuln_Closed = json.loads(febvulnsC)

marC = open("vulnData/marvulnsClosed.json", "r")
marvulnsC = marC.read()
mar_vuln_Closed = json.loads(marvulnsC)

aprC = open("vulnData/aprvulnsClosed.json", "r")
aprvulnsC = aprC.read()
apr_vuln_Closed = json.loads(aprvulnsC)

mayC = open("vulnData/mayvulnsClosed.json", "r")
mayvulnsC = mayC.read()
may_vuln_Closed = json.loads(mayvulnsC)
