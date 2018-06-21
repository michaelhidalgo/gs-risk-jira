from app import app
from flask import render_template
import json
from collections import Counter
from readData import *
from chartdata import *
from chartvulns import *


@app.route('/')
def home():

	return render_template('home.html',)

@app.route('/charts')
def charts():

	return render_template('charts.html',							
							riskLow=riskLow,
							riskMedium=riskMedium,
							riskHigh=riskHigh,
							riskCritical=riskCritical,
							dummyLow=dummyLow,
							dummyMedium=dummyMedium,
							dummyHigh=dummyHigh,
							dummyCritical=dummyCritical,
							testLow=testLow,
							testMedium=testMedium,
							testHigh=testHigh,
							testCritical=testCritical,
							monthlyLow=monthlyLow,
							monthlyMedium=monthlyMedium,
							monthlyHigh=monthlyHigh,
							monthlyCritical=monthlyCritical,
							lowRisksClosed=lowRisksClosed,
							mediumRisksClosed=mediumRisksClosed,
							highRisksClosed=highRisksClosed,
							criticalRisksClosed=criticalRisksClosed,
							vulnLow=vulnLow,
							vulnMedium=vulnMedium,
							vulnHigh=vulnHigh,
							vulnCritical=vulnCritical,
							lowVulnsClosed=lowVulnsClosed,
							mediumVulnsClosed=mediumVulnsClosed,
							highVulnsClosed=highVulnsClosed,
							criticalVulnsClosed=criticalVulnsClosed,
							lowRisks=lowRisks,
							mediumRisks=mediumRisks,
							highRisks=highRisks,
							criticalRisks=criticalRisks
							)

@app.route('/mappings')
def mappings():

	return render_template('mappings/mappings.html',new_data=new_data)

@app.route('/mappingOne')
def mappingOne():

	return render_template('mappings/mappingOne.html',new_data=new_data)

@app.route('/mappingTwo')
def mappingTwo():

	return render_template('mappings/mappingTwo.html',new_data=new_data)

@app.route('/mappingThree')
def mappingThree():

	return render_template('mappings/mappingThree.html',new_data=new_data)


@app.route('/group')
def group():


	return render_template('group.html',new_data=new_data, 
										groupLowData=groupLowData, 
										groupMediumData=groupMediumData, 
										groupHighData=groupHighData, 
										groupCriticalData=groupCriticalData, 
										pbxtotalCount=pbxtotalCount)

@app.route('/photobox')
def photobox():

	return render_template('photobox.html',new_data=new_data, 
										   photoboxLowData = photoboxLowData,photoboxMediumData=photoboxMediumData,
										   photoboxHighData=photoboxHighData,photoboxCriticalData=photoboxCriticalData)


@app.route('/techops')
def techops():

	techopsRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
					techopsRisks+=1

	techopsCount = ("TechOps: {} Risks".format(techopsRisks))
	print(techopsCount)

	return render_template('pbx_group/techops.html',new_data=new_data,
											 techopsCount=techopsCount)

@app.route('/techopsmap')
def techopsmap():

	return render_template('pbx_group/techopsmap.html', new_data=new_data)

@app.route('/webops')
def webops():
	webopsRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Webops":
					webopsRisks+=1

	webopsCount = ("WebOps: {} Risks".format(webopsRisks))
	print(webopsCount)

	return render_template('photobox/webops.html',new_data=new_data,
										 webopsCount=webopsCount)

@app.route('/architecture')
def architecture():

	architectureRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Architecture":
					architectureRisks+=1

	architectureCount = ("Group Architecture: {} Risks".format(architectureRisks))
	print(architectureCount)

	return render_template('pbx_group/architecture.html',new_data=new_data,
											 architectureCount=architectureCount)


@app.route('/productioneng')
def productioneng():
	prodRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Production-Eng":
					prodRisks+=1

	prodCount = ("Production & Factories: {} Risks".format(prodRisks))
	print(prodCount)

	return render_template('pbx_group/productioneng.html',new_data=new_data,
									   prodCount=prodCount)

@app.route('/photoscience')
def photoscience():

	photoscienceRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-imageupload" or component['name'] == "PBX-Data":
					photoscienceRisks+=1
				

	photoscienceCount= ("AI Machine Learning & Images: {} Risks".format(photoscienceRisks))
	print(photoscienceCount)

	return render_template('pbx_group/photoscience.html',new_data=new_data,
											   photoscienceCount=photoscienceCount)

@app.route('/businessintel')
def businessintel():

	businessintelRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Data":
					businessintelRisks+=1
				

	businessintelCount= ("Business Data and Intelligence: {} Risks".format(businessintelRisks))
	print(businessintelCount)

	return render_template('pbx_group/businessintel.html',new_data=new_data,
												businessintelCount=businessintelCount)


@app.route('/groupsecurity')
def groupsecurity():

	groupSecurityRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Group-Security":
					groupSecurityRisks+=1
				

	groupSecurityCount= ("Group Security : {} Risks".format(groupSecurityRisks))
	print(groupSecurityCount)

	return render_template('pbx_group/groupsecurity.html',new_data=new_data,
												groupSecurityCount=groupSecurityCount)

@app.route('/hr')
def hr():

	hrRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Human Resources":
					hrRisks+=1
				

	hrCount= ("Human Resource: {} Risks".format(hrRisks))
	print(hrCount)

	return render_template('pbx_group/hr.html',new_data=new_data,
												hrCount=hrCount)

@app.route('/producteng')
def producteng():

	productengRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Babel" or component['name'] == "PBX-Studio" or component['name'] == "PBX-Shop" or component['name'] == "PBX-checkout" or component['name'] == "PBX-NativeApps":
					productengRisks+=1
				

	productCount= ("Product Engineering: {} Risks".format(productengRisks))
	print(productCount)

	return render_template('pbx_group/producteng.html',new_data=new_data,
												productCount=productCount)

@app.route('/productengVulns')
def productengVulns():

	productengVulns = 0

	counter=Counter()
	for item in vulnData['items']:
		if item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Babel" or component['name'] == "PBX-Studio" or component['name'] == "PBX-Shop" or component['name'] == "PBX-checkout" or component['name'] == "PBX-NativeApps":
					productengVulns+=1
				

	productCount= ("Product Engineering : {} Vulnerabilites".format(productengVulns))


	return render_template('pbx_group/productengVulns.html',vulnData=vulnData,
															productCount=productCount)



@app.route('/babel')
def babel():
	babelRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Babel":
					babelRisks+=1

	babelCount = ("Babel & BackOffice: {} Risks".format(babelRisks))
	print(babelCount)

	babelCritical = 0

	return render_template('photobox/babel.html',new_data=new_data,
										babelCount=babelCount)


@app.route('/studio')
def studio():
	studioRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Studio":
					studioRisks+=1

	studioCount = ("Studio: {} Risks".format(studioRisks))
	print(studioCount)

	return render_template('photobox/studio.html', new_data=new_data,
										  studioCount=studioCount)


@app.route('/shop')
def shop():
	shopRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX_shop":
					shopRisks+=1

	shopCount = ("Shop: {} Risks".format(shopRisks))
	print(shopCount)

	return render_template('photobox/shop.html',new_data=new_data,
									   shopCount=shopCount)


@app.route('/checkout')
def checkout():
	checkoutRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-checkout":
					checkoutRisks+=1

	checkoutCount = ("Supreme Checkout: {} Risks".format(checkoutRisks))
	print(checkoutCount)

	return render_template('photobox/checkout.html',new_data=new_data,
		                                   checkoutCount=checkoutCount)

@app.route('/mobile')
def mobile():
	mobileAppRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-NativeApps":
					mobileAppRisks+=1

	mobileAppCount = ("Mobile App: {} Risks".format(mobileAppRisks))
	print(mobileAppCount)

	return render_template('photobox/mobile.html',new_data=new_data,
										 mobileAppCount=mobileAppCount)


@app.route('/moonpigtech')
def moonpigtech():
	moonpigtechRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Moonpig-Risk":
					moonpigtechRisks+=1

	moonpigtechCount = ("Moonpig Tech: {} Risks".format(moonpigRisks))
	print(moonpigtechCount)

	return render_template('pbx_group/moonpigtech.html',new_data=new_data,
										 moonpigtechCount=moonpigCount)

@app.route('/postertech')
def postertech():
	postertechRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "posterXXL-Risk":
					postertechRisks+=1

	postertechCount = ("poster Tech: {} Risks".format(posterRisks))
	print(postertechCount)

	return render_template('pbx_group/postertech.html',new_data=new_data,
										 postertechCount=posterCount)

@app.route('/hofmanntech')
def hofmanntech():
	hofmanntechRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Hofmann-Risk":
					hofmanntechRisks+=1

	hofmanntechCount = ("hofmann Tech: {} Risks".format(hofmannRisks))
	print(hofmanntechCount)

	return render_template('pbx_group/hofmanntech.html',new_data=new_data,
										 hofmanntechCount=hofmannCount)

@app.route('/mpecommerce')
def mpecommerce():
	mpecommerceRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "mp-ecommerce":
					mpecommerceRisks+=1

	mpecommerceCount = ("Moonpig Ecommerce: {} Risks".format(mpecommerceRisks))
	print(mpecommerceCount)

	return render_template('moonpig/mpecommerce.html',new_data=new_data,
										 mpecommerceCount=mpecommerceCount)

@app.route('/mpmobile')
def mpmobile():
	mpMobileRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "MP-Mobile":
					mpMobileRisks+=1

	mpMobileCount = ("Moonpig Mobile: {} Risks".format(mpMobileRisks))
	print(mpMobileCount)

	return render_template('moonpig/mpMobile.html',new_data=new_data,
										 mpMobileCount=mpMobileCount)



@app.route('/brand')
def brand():


	return render_template('brand.html',new_data=new_data,
										groupData=groupData,
										photoboxData=photoboxData,
										moonpigData=moonpigData,
										hofmannData=hofmannData,
										posterData=posterData,
										gsData=gsData, 
										groupCount=groupCount,
										photoboxCount=photoboxCount,
										moonpigCount=moonpigCount,
										hofmannCount=hofmannCount,
										posterCount=posterCount,
										gsCount=gsCount,
										openRisks=openRisks
										)


@app.route('/riskdetail/<id>')
def riskdetail(id):

	for item in new_data['items']:
		if item['Key'] == (id):
			key = (item['Key'])
			summary = (item['Summary'])
			rating = (item['Rating'])
			status = (item['Status'])
			owner =(item['Risk Owner'])
		for link in item['parent']:
			parentItem = link['Key']
			if link['Key'] == (item['Key']):
				newItem = (item['Key'])
				newItemSummary = (item['Summary'])
			#print('Parent Link: ' + parentItem)
		for link in item['child']:
			childItem = link['Key']
			#print('Child Link: ' + childItem)	

	return render_template('riskdetail.html',new_data=new_data,
											 key=key,  
											 rating=rating,
											 summary=summary, 
											 status=status,
											 owner=owner,
											 childItem=childItem,
											 parentItem=parentItem)
