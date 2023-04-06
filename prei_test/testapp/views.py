from django.shortcuts import render
import random

# Create your views here.

questions=[
    ['Pakistan Land ownership is record based on',['Registry','FARD','Allotment Letter','Stamp Paper'],'FARD'],
    ['The distribution of Land in a Map is called',['Layout Plan','Khasra Number','Aks shajrah','Dawa-e-taqseem'],'Aks Shajrah'],
    ['Existing Land Record System was originated in which century',['19','18','17','16'],'16'],
    ['Khatooni is term used for',['Owners','Tenants','Shareholders','Family Tree'],'Tenants'],
    ['Passbook is used to maintain',['Properties','Tenants record','Crops Yield record','Personal Savings'],'Crops Yield record'],
    ['Patwari comes under direct supervision of',['Tehsildar','Girdawari','Deputy commissioner','NAB'],'Tehsildar'],
    ['Registry is a type of Transfer which is',['Permanent','Temporary','For a specific time','None of the above'],'Temporary'],
    ['The process of transfer completion in Land via Fard takes ',['1 day when seller gives his statement to approve transfer','10 Days after seller gives his statement to approve transfer','1 month','6 months approx'],'6 months approx'],
    ['We pay transfer fee of our land according to',['Sale Agreement','Market Price','DC Value','Any Price we want'],'Dc Value'],
    ['The transfer fee is paid to the govt by',['cash','Bank Deposit','Capital value Tax(Duty)','Purchasing Stamp papers'],'Purchasing Stamp papers'],
    ['As a Broker you are allowed to make agreement as a seller with any property which is being undersold',['Right','Wrong'],'Wrong'],
    ['As a Broker you can keep a certian top in any transaction to make extra money in sales transactions',['Right','Wrong'],'Wrong'],
    ['It is ok to give wrong property address to buyers just to engage their interest',['Right','Wrong'],'Wrong'],
    ['To Call Other agents party either buyer or seller is',['Right','Wrong'],'Wrong'],
    ['To split commission with other agents to close the deal is',['Right','Wrong'],'Right'],
    ['Off Plan sales is When',['Property is under construction','Property is ready','property is advertiesd Publicly','Property NOC is available'],'Property is under construction'],
    ['Horizontal Development means',['Housing Scheme','Apartments Complex','Shopping Plaza','Developer With High reputation'],'Housing Scheme'],
    ['if a seller don\'t give you the promised commission upon successful transaction you will do',['Court case against him','file a complaint in Police station agianst him','Abouse or Threat him','Leave him and move on'],'Leave him and move on'],
    ['It is ok to fix appointments with multiple clients at one time for viewing',['Right','Wrong'],'Wrong'],
    ['It is ok to charge additional commission to clients by telling the high prices',['Right','Wrong'],'Wrong'],
    ['Prospecting Means Asking questions from Buyers about his budget',['Right','Wrong'],'Wrong'],
    ['The only legislation for real estate commission in Pakistan is declared by',['Ministry of Housing','FBR','Excise & Taxation','Real estate Associations'],'Excise & Taxation'],
    ['Standard commission in Sales Transaction is from one side is',['1%','2%','5%','As Many as I can earn'],'1%'],
    ['Balloting is a way of selling more files than the developers capacity and is totally legal in Pakistan',['Right','Wrong'],'Right'],
    ['At which stage the developer is allowed to market and sell the inventory of the project',['After getting the Techniacl NOC','After getting the Planning Letter','After getting the Advertisement NOC','Immediately after purchasing land'],'After getting the techincal NOC'],
    ['On average there are how many NOC;s required to start a housing scheme',['One','Five','Seven','Nine'],'Nine'],
    ['ROI is calculated on the basis of',['Capital Gain','Purchase Price','Rental value','None of the above'],'Rental Value'],
    ['When X Purchase a Property in year 2010, now he wants to sell in year 2020 the increase in the sales price will be called',['Inflation','Profit','Capital Gain','Commisson'],'Capital Gain'],
    ['Convincing people to invest in a certain project just because you have an understanding with the developer of getting high commission is',['Right','Wrong'],'Wrong'],
    ['Once the appointment is fixed with client for viewing, its ok to reach a little late than client',['Right','Wrong'],'Wrong'], 
    ['Thullay ka Qabza is a term used for',['Legal Possession','Temporary possession','illegal possession','None of the above'],'Temporary possession'],
    ['Owner ship land record system lacks one major element that is',['Possession','Owners CNIC and picture','Actual Location of the land','History of sale and purchase'],'Possession'],
    ['Developers are the one who drive and control the real estate market',['Right','Wrong'],'Wrong'],
    ['Khewat contains the record of',['Land owners','Labour','Tenants','Childrens and Parents'],'Land owners'],
    ['In order to become the property dealer it is mandatory to get license',['Right','Wrong'],'Wrong'],
    ['In Brokerage the strongest and closest point to fulfil the transaction is',['Marketing Professionally','Viewing Commitment','Negotiation Follow up','Enquiries Follow up'],'Negotiation Follow up'],
    ['Conflict of interest is allowed and a standard practice in real estate',['Yes','No'],'No'],
    ['Taking commission in Cash and not issuing the receipt to the client is',['Legal','Illegal'],'Illegal'],
    ['Real estate transactions in Pakistan happens mostly due to',['Personal relationship','Linkedin Network','Social Media advertisement','Website and project knowledge'],'Personal relationship'],
    ['Working with a certified and licensed real estate agent is',['Legal','Illgel'],'Legal'],
]


def test(request):
    if request.POST:
        if 'name' in request.POST:
            request.session['name']=request.POST['name']
            print('done')
        elif 'marks' in request.POST:
            request.session['marks']=request.POST['marks']
            print(request.POST['marks'])
    question=random.sample(questions,20)
    session=request.session.get('name')
    marks=request.session.get('marks')
    # request.session.flush()
    return render(request,'fron_end.html',{
        'questions':question,
        's':session,
        'm':marks,
    })

def fields(request):
    return render(request,'test.html')