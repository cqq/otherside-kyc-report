from cmath import e
import csv
from tkinter import E
from attr import validate
import os
import requests
#data from https://etherscan.io/exportData?type=tokenholders&contract=0x960b236A07cf122663c4303350609A66A7B288C0&decimal=18
totalAddess=0
approved=0
depost=0
valid=0

def check(url) :
    try :
        #print('url = ' + 'https://kyc-api.animocabrands.com/v1.0/profile/?walletAddress=' + url)
        response = requests.get('https://kyc-api.animocabrands.com/v1.0/profile/?walletAddress=' + url)
        json = response.json()
        print(json)
        if json['status'] == "APPROVED" :
            return True
        else:
            return False    
    except e:
        print('error ' + e)
        return False

testcheck= check('0x043c1Cb1F42da2FaDA62650d3D1A647dEf3A5d25')
print(testcheck)

with open('landaddress.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)   
      
        for row in reader:
            totalAddess+=1
            print(row['HolderAddress'], row['Balance'],reader.line_num)
            cheked = check(row['HolderAddress'])
            if cheked:
                approved+=1 
            # if approved > 1:
            #     print('total address持币地址 ' + str(totalAddess) + " kyc  通过 " +  str(approved) +  " valid 充值KYC地址 " + str(valid))                
            #     os._exit()
            if  float(row['Balance']) >= 305:
                depost= depost+1
                if cheked:
                    valid = valid+1
        rows = list(reader)            
        totalrows = len(rows)
        print(totalrows)
        print('total address持币地址 ' + str(totalAddess) + " kyc  通过 " +  str(approved) +  " valid 充值KYC地址 " + str(valid))                

            
