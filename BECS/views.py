import datetime
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from numpy import integer
from BECS.models import Donator, BloodStock, AuditTrail
from fpdf import FPDF
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd
import re 
import numpy as np
# from BECS.models import Donator
todaydt = timezone.now()
# Create your views here.

class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 8, 'Header', 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

def index(request):
    bloodlst = BloodStock.objects.all()
    bc = BloodStock.objects.filter(bid = 1)
    if bc.exists():
        return render(request,'index.html', {"bloodlst":bloodlst})
    else:
        makebl = BloodStock(bid = 1)
        makebl.save()
        return render(request,'index.html', {"bloodlst":bloodlst})
        

def trauma(request):
    bloodlst = BloodStock.objects.all()
    request = checkbox(request)
    return render(request,'trauma.html', {"bloodlst":bloodlst})

def auditrail(request):
    bloodlst = BloodStock.objects.all()
    return render(request,'auditrail.html', {"bloodlst":bloodlst})

def donators(request):
    dntlst = Donator.objects.all()
    bloodlst = BloodStock.objects.all()
    return render(request,'donators.html', {"dntlst":dntlst, "bloodlst":bloodlst})

def emergency(request):
    bloodlst = BloodStock.objects.all()
    return render(request,'emergency.html', {"bloodlst":bloodlst})

# --- Fonctions calculator --- #
def takeallom(request):
    if request.method=='POST':
        bldadd = BloodStock.objects.get(bid = 1)
        if bldadd.om > 0:
            at_emergency(bldadd.om)
            messages.success(request, 'Total O- taken : ' + str(bldadd.om))
            BloodStock.objects.filter(bid = 1).update(om = 0)
            return emergency(request)
        else:
            messages.error(request, 'No O- any more...')
            return emergency(request)
        
def add_donator(request):
    if request.method=='POST':
        save_record=Donator()
        bldadd = BloodStock.objects.get(bid = 1)
        save_record.did = request.POST.get('idn')
        save_record.fname = request.POST.get('fn')
        save_record.lname = request.POST.get('ln')
        save_record.bloodtype = request.POST.get('Bloods')
        save_record.donation_date = timezone.now()
        at_donator(save_record.bloodtype)
        if save_record.bloodtype == "A+":
            bld1 = bldadd.ap +1
            BloodStock.objects.filter(bid = 1).update(ap = bld1)
        elif save_record.bloodtype == "O+":
            bld1 = bldadd.op +1
            BloodStock.objects.filter(bid = 1).update(op = bld1)
        elif save_record.bloodtype == "B+":
            bld1 = bldadd.bp +1
            BloodStock.objects.filter(bid = 1).update(bp = bld1)
        elif save_record.bloodtype == "AB+":
            bld1 = bldadd.abp +1
            BloodStock.objects.filter(bid = 1).update(abp = bld1)
        elif save_record.bloodtype == "A-":
            bld1 = bldadd.am +1
            BloodStock.objects.filter(bid = 1).update(am = bld1)
        elif save_record.bloodtype == "O-":
            bld1 = bldadd.om +1
            BloodStock.objects.filter(bid = 1).update(om = bld1)
        elif save_record.bloodtype == "B-":
            bld1 = bldadd.bm +1
            BloodStock.objects.filter(bid = 1).update(bm = bld1)
        elif save_record.bloodtype == "AB-":
            bld1 = bldadd.abm +1
            BloodStock.objects.filter(bid = 1).update(abm = bld1)
        save_record.save()
        
        messages.success(request, 'A new donator has been added successfully :)')
        return donators(request)
    else:
        return donators(request)
    
def checkbox(request):
    Blood_rarity={
    'O+':32,
    'A+':34,
    'B+':17,
    'AB+':7,
    'O-':3,
    'A-':4,
    'B-':2,
    'AB-':1
    }
    Blood_Receive_from={
    'O+':["O-"],
    'A+':["A-","O+","O-"],
    'B+':["B-","O+","O-"],
    'AB+':["O-","A-","O+","B-","B+","AB-"],
    'O-':["O-"],
    'A-':["O-"],
    'B-':["O-"],
    'AB-':["O-","B-","A-"]
    }
    if request.method=='POST':
        bldadd = BloodStock.objects.get(bid = 1)
        bloodnum = request.POST.get('tbloodnumber')
        blood= request.POST.get('Bloods')
        print(blood)
        bld1 = 0
        at_trauma(blood, bloodnum)
        if blood == "A+":
            bld1 = bldadd.ap - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(ap = bld1)
        elif blood == "O+":
            bld1 = bldadd.op  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(op = bld1)
        elif blood == "B+":
            bld1 = bldadd.bp  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(bp = bld1)
        elif blood == "AB+":
            bld1 = bldadd.abp  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(abp = bld1)
        elif blood == "A-":
            bld1 = bldadd.am  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(am = bld1)
        elif blood == "O-":
            bld1 = bldadd.om  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(om = bld1)
        elif blood == "B-":
            bld1 = bldadd.bm  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(bm = bld1)
        elif blood == "AB-":
            bld1 = bldadd.abm  - int(bloodnum)
            if bld1 >= 0:
                BloodStock.objects.filter(bid = 1).update(abm = bld1)
        else:
            Receive_from=(Blood_Receive_from[blood])
            print(Receive_from)
            for i in range(0,len(Receive_from)-1):
                for k in range(i+1,len(Receive_from)):
                    if Blood_rarity[Receive_from[k]] > Blood_rarity[Receive_from[i]]:
                        temp=Receive_from[i]
                        Receive_from[i]=Receive_from[k]
                        Receive_from[k]=temp
            print(Receive_from)
            messages.error(request, 'Not ' + str(blood) + "You can use :" + str(Receive_from) + " In this order.")
    return request

def takeblood(request):
    Blood_rarity={
    'O+':32,
    'A+':34,
    'B+':17,
    'AB+':7,
    'O-':3,
    'A-':4,
    'B-':2,
    'AB-':1
    }
    if request.method=='POST':
         blood= request.POST.getlist('Bloods')
         
# Auditrail

def at_emergency(q):
    save_record=AuditTrail()
    save_record.type = "Emergency"
    save_record.btype = "om"
    save_record.qtts = q
    save_record.dt = todaydt
    save_record.save()
    
         
def at_donator(bl):
    save_record=AuditTrail()
    save_record.type = "AddDonator"
    save_record.btype = bl
    save_record.qtts = 1
    save_record.dt = todaydt
    save_record.save()
    
def at_trauma(bl, q):
    save_record=AuditTrail()
    save_record.type = "Trauma"
    save_record.btype = bl
    save_record.qtts = q
    save_record.dt = todaydt
    save_record.save()
    
# Copies

def copyall(request):
    if request.method=='POST':
        doctype = request.POST.get('doctype')
        docopy = {
        "Id": [],
        "Type": [],
        "BloodType": [],
        "Quantity": [],
        "Date": []
        }
        at_db = AuditTrail.objects.all()
        bc = AuditTrail.objects.filter(aid = 1)
        df = pd.DataFrame(list(AuditTrail.objects.all()))
        if bc.exists():
            for i, row in tqdm(df.iterrows()):
                a = row[0] # Id
                b = row[1] # type
                c = row[2] # bloodtype
                d = row[3] # quantity
                e = row[4] # date
                docopy.iloc[i] = [a, b, c, d, e]
            if doctype == "pdf":
                pdf = PDF()
                pdf.add_page()
                ch = 50
                pdf.set_font('Arial', 'B', 24)
                pdf.cell(w=0, h=20, txt="Audit Trail Copy", ln=1)
                pdf.set_font('Arial', '', 16)
                pdf.cell(w=30, h=ch, txt="Date: ", ln=0)
                pdf.cell(w=30, h=ch, txt=str(todaydt), ln=1)
                pdf.cell(w=30, h=ch, txt="Project: ", ln=0)
                pdf.cell(w=30, h=ch, txt="BECS", ln=1)
                pdf.ln(ch)
                # Table Header
                pdf.set_font('Arial', 'B', 16)
                pdf.cell(w=40, h=ch, txt='Id', border=1, ln=0, align='C')
                pdf.cell(w=40, h=ch, txt='Type', border=1, ln=1, align='C')
                pdf.cell(w=40, h=ch, txt='Blood Type', border=1, ln=2, align='C')
                pdf.cell(w=40, h=ch, txt='Quantity', border=1, ln=3, align='C')
                pdf.cell(w=40, h=ch, txt='Date', border=1, ln=4, align='C')
                # Table contents
                pdf.set_font('Arial', '', 16)
                for i in range(0, len(df)):
                    pdf.cell(w=40, h=ch, 
                            txt=df['Id'].iloc[i], 
                            border=1, ln=0, align='C')
                    pdf.cell(w=40, h=ch, 
                            txt=df['type'].iloc[i], 
                            border=1, ln=1, align='C')
                    pdf.cell(w=40, h=ch, 
                            txt=df['btype'].iloc[i], 
                            border=1, ln=1, align='C')
                    pdf.cell(w=40, h=ch, 
                            txt=df['qtts'].iloc[i], 
                            border=1, ln=1, align='C')
                    pdf.cell(w=40, h=ch, 
                            txt=df['dt'].iloc[i], 
                            border=1, ln=1, align='C')
                pdf.output(f'./AuditTrail.pdf', 'F')
            elif doctype == "xlsx":
                df.to_excel("AuditTrail.xlsx")

                
        else:
            pass
        
    
