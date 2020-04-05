import pyodbc,json,decimal,string

true=True

# class DecimalEncoder(json.JSONEncoder):                         #Class to add up the decimals to our JSON conversion
#     def default(self, o):
#         if isinstance(o, decimal.Decimal):
#             return float(o)                     
#         return super(DecimalEncoder, self).default(o)

#Connecting to our SQL Server Database using pyodbc
def connect_db():
    try:
        conn = pyodbc.connect('Driver={SQL Server};' 
        'Server=183.83.217.150,35001;' 
        'Database=unityprod_17092019;'
        'uid=unityAppUser;pwd=Winter@2019')
            
    except:
        print("The connection to the DB failed")
    
    command= ("SELECT * FROM UNITY.Claims_Actuals WHERE VoucherNumber='3197870';")
    # command= ("SELECT * FROM UNITY.Claims_Actuals WHERE VoucherNumber='3318330';")
    
    cursor= conn.cursor().execute(command)                      #Executing the SQL Command

    results = []

    columns = [column[0] for column in cursor.description]      #Fetching the column headers

    for row in cursor.fetchall():
        results.append(dict(zip(columns,row)))                  #Key -> Col Header and value is the Table row Values
    
    with open("Data_from_db.txt", "w", encoding="utf-8") as writeJsonfile:
        json.dump(results, writeJsonfile, indent=4,default=str)                     #Writing the JSON format to a file
    
# connect_db()
def calc_logic():
    with open("Data_from_db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
        jsonFile=json.load(readJsonfile)
        lenJsonFile=len(jsonFile)
        centerId=voucherNumber=userId=fServiceFee=fServiceId=DOB=Gender=ServiceDate=fProCode=fModifier=fICDCode=fServiceUnits=fReasonCode=fTimeStamp=fCarrierId=PrimaryDiagnosis=fServicePlaceId=fProcessed=VoucherCode=Relationship=""
        claimTotal=0
        ICDCodes=""
        records = jsonFile[0:lenJsonFile]        #Fetching the serviceCodeLines separately
        # print(records[0])
    for i in records:
        centerId=centerId+(str(i['CENTERID'])+',')
        centerIdList=list(centerId.split(','))
        
        voucherNumber=voucherNumber+(str(i['VoucherNumber'])+',')
        voucherNumberList=list(voucherNumber.split(','))
        
        userId=userId+(str(i['UserId'])+',')
        userIdList=list(userId.split(','))
        
        fServiceId=fServiceId+(str(i['ServiceId'])+',')     
        fServiceIdList=list(fServiceId.split(','))  
                                                                        #Extracting Required Attributes
        DOB=DOB+(str(i['DateOfBirth'])+',')
        DOBList=list(DOB.split(','))
        
        Gender=Gender+(str(i['Gender'])+',')
        GenderList=list(Gender.split(','))
        
        ServiceDate=ServiceDate+(str(i['ServiceDate'])+',')
        serviceDateList=list(ServiceDate.split(','))
        
        fProCode=fProCode+(str(i['PROCode'])+',')
        fProCodeList=list(fProCode.split(','))
        
        fModifier=fModifier+(str(i['Modifier'])+',')
        fModifierList=list(fModifier.split(','))
        
        fICDCode=fICDCode+(str(i['ICDCode'])+',')
        fICDCodeList=list(fICDCode.split(','))
        
        fServiceFee=fServiceFee+(str(i['ServiceFee'])+',')
        fServiceFeeList=list(fServiceFee.split(','))
        
        fServiceUnits=fServiceUnits+(str(i['ServiceUnits'])+',')
        fServiceUnitsList=list(fServiceUnits.split(','))
        
        fReasonCode=fReasonCode+(str(i['ReasonCodeId'])+',')
        fReasonCodeList=list(fReasonCode.split(','))
        
        fTimeStamp=fTimeStamp+(str(i['TimeStamp'])+',')
        fTimeStampList=list(fTimeStamp.split(','))
        
        fCarrierId=fCarrierId+(str(i['CarrierId'])+',')
        fCarrierIdList=list(fCarrierId.split(','))
        
        PrimaryDiagnosis=PrimaryDiagnosis+(str((i['PrimaryDiagnosisCode']).strip())+',')
        PrimaryDiagnosisList=list(PrimaryDiagnosis.split(','))
        
        fServicePlaceId=fServicePlaceId+(str(i['ServicePlaceID_Old'])+',')
        fServicePlaceIdList=list(fServicePlaceId.split(','))
        
        fProcessed=fProcessed+(str(i['Processed'])+',')
        fProcessedList=list(fProcessed.split(','))
        
        VoucherCode=VoucherCode+(str(i['VoucherId'])+',')
        VoucherCodeList=list(VoucherCode.split(','))
        
        Relationship=Relationship+(str(i['RelationShipToSubscriber'])+',')
        RelationshipList=list(Relationship.split(','))
        

    PrimaryDiagnosisList=PrimaryDiagnosisList[0].replace(".","")
    ServiceFeeAmounts = (sorted(set(fServiceFeeList), key=fServiceFeeList.index))
    for i in ServiceFeeAmounts:
        if(i==''):
            ServiceFeeAmounts.remove(i)
        
    for i in ServiceFeeAmounts:
        claimTotal+=float(i)    
        
    fICDCodeList = (sorted(set(fICDCodeList), key=fICDCodeList.index))

    ICDCodes= str(fICDCodeList)
    
    ICDCodesList=ICDCodes.replace(".","")
    ICDCodesList=eval(ICDCodesList)                 #Converting String to List without Splitting
    
    if PrimaryDiagnosisList in ICDCodesList:
        ICDCodesList.remove(PrimaryDiagnosisList)
        
    for i in ICDCodesList:
        if(i==''):
            ICDCodesList.remove(i)
        
    
    EmptyStrings=["","","","","","","","","","",""]
    EmptyProCodes=["00000","00000","00000","00000","00000","00000","00000","00000","00000","00000","00000"]
    # for i in EmptyStrings:
    #     ICDCodesList.append(i)
        
    # print(ICDCodesList)

    
    fTimeStampList=fTimeStampList[0].replace(".","")            #Fetching the ServiceDate Time Stamp
    date=fTimeStampList.split(" ")
    date=date[0].replace("-","")
    # print(date)
    
    DOBList=DOBList[0].replace("-","")
    # print(DOBList)
    
    primarycode={}
    primarycode['diagnosisCode']=PrimaryDiagnosisList
    primarycode['diagnosisTypeCode']="ABK"
    
    healthCareCodeInformation=[]
    healthCareCodeInformation.append(primarycode)
    
    lenICD=len(ICDCodesList)
    
    icdcodesdict={}
    
    for i in range(lenICD):
        icdcodesdict['diagnosisCode']=ICDCodesList[i]
        icdcodesdict['diagnosisTypeCode']="ABF"
        icddict=icdcodesdict.copy()
        icddict1=json.dumps(icddict)
        healthCareCodeInformation.append(icddict)
        # healthCareCodeInformation1=json.dumps(healthCareCodeInformation)
        
    # print(healthCareCodeInformation)               #The Diagnosis codes are in JSON format now
    
    fProCodes = (sorted(set(fProCodeList), key=fProCodeList.index))         #Removing duplicate PROCODES
    
    for i in fProCodes:
        if(i==''):
            fProCodes.remove(i)
    # print(fProCodes)
    
    servicelinescount=len(fProCodes)
    
    #Generating the service lines based on the PROCODE
    servicelineslist=[]
    for i in range(1,servicelinescount+1):
        
        servicelinesdict={
                        "assignedNumber": str(i),
                        "professionalService": {
                        "compositeDiagnosisCodePointers": {
                            "diagnosisCodePointers": [
                            ""
                            ]
                        },
                        "description": "",
                        "lineItemChargeAmount": str(fServiceFeeList[i]),
                        "measurementUnit": "UN",
                        "placeOfServiceCode": "11",
                        "procedureCode": str(fProCodeList[i]),
                        "procedureIdentifier": "HC",
                        "procedureModifier1": "GP",
                        "serviceUnitCount": str(fServiceUnitsList[i])
                        },
                        "providerControlNumber": "",
                        "serviceDate": str(date)
                    }
        
        servicedict=servicelinesdict.copy()
        servicedict1=json.dumps(servicedict)
        servicelineslist.append(servicedict)
        # servicelineslist1=json.dumps(servicelineslist)
    # print(servicelineslist)
    
    #Our JSON Data
    data = {
        "precisionThreshold": 0.95,
        "billerId": "",
        "billing": {
            "address": {
            "address1": "",
            "address2": "",
            "city": "",
            "postalCode": "029193228",
            "state": ""
            },
            "commercialNumber": "",
            "contactInformation": {
            "email": "",
            "faxNumber": "",
            "name": "",
            "phoneNumber": "",
            "validContact": true
            },
            "employerId": "",
            "firstName": "",
            "lastName": "",
            "locationNumber": "",
            "middleName": "",
            "npi": "",
            "organisationName": "",
            "providerType": "",
            "providerUpinNumber": "",
            "ssn": "",
            "stateLicenseNumber": "",
            "taxonomyCode": "225100000X",
            "validBillingProvider": true,
            "validProvider": true
        },
        "claimInformation": {
            "benefitsAssignmentCertificationIndicator": "Y",
            "claimChargeAmount": str(claimTotal),
            "claimContractInformation": {
            "contractAmount": "",
            "contractCode": "",
            "contractPercentage": "",
            "contractTypeCode": "",
            "contractVersionIdentifier": "",
            "termsDiscountPercentage": ""
            },
            "claimDateInformation": {
            "accidentDate": "",
            "acuteManifestationDate": "",
            "admissionDate": "",
            "assumedAndRelinquishedCareBeginDate": "",
            "assumedAndRelinquishedCareEndDate": "",
            "authorizedReturnToWorkDate": "",
            "disabilityBeginDate": "",
            "disabilityEndDate": "",
            "dischargeDate": "",
            "firstContactDate": "",
            "hearingAndVisionPrescriptionDate": "",
            "initialTreatmentDate": "",
            "lastMenstrualPeriodDate": "",
            "lastSeenDate": "",
            "lastWorkedDate": "",
            "lastXRayDate": "",
            "repricerReceivedDate": "",
            "symptomDate": ""
            },
            "claimFilingCode": "CI",
            "claimFrequencyCode": "1",
            "claimSupplementalInformation": {
            "carePlanOversightNumber": "",
            "claimControlNumber": "",
            "claimNumber": "",
            "cliaNumber": "",
            "demoProjectIdentifier": "",
            "investigationalDeviceExemptionNumber": "",
            "mammographyCertificationNumber": "",
            "medicalRecordNumber": "",
            "medicareCrossoverReferenceId": "",
            "priorAuthorizationNumber": "",
            "referralNumber": "",
            "reportInformation": {
                "attachmentControlNumber": "",
                "attachmentReportTypeCode": "",
                "attachmentTransmissionCode": ""
            },
            "repricedClaimNumber": "",
            "serviceAuthorizationExceptionCode": ""
            },
            "healthCareCodeInformation": healthCareCodeInformation,
            "patientAmountPaid": "",
            "patientControlNumber": "",
            "patientWeight": "",
            "placeOfServiceCode": "11",
            "planParticipationCode": "A",
            "propertyCasualtyClaimNumber": "",
            "releaseInformationCode": "",
            "serviceFacilityLocation": {
            "address": {
                "address1": "",
                "address2": "",
                "city": "",
                "postalCode": "",
                "state": ""
            },
            "organizationName": ""
            },
            "serviceLines": servicelineslist,
            "signatureIndicator": ""
        },
        "controlNumber": str(voucherNumberList[0]),
        "date": "",
        "dependent": {
            "dateOfBirth": str(DOBList),
            "firstName": "",
            "gender": "F",
            "lastName": "",
            "middleName": "",
            "relationshipToSubscriberCode": str(RelationshipList[0]),
            "ssn": "",
            "address": {
            "state": "OH"
            }
        },
        "providers": [
            {
            "address": {
                "address1": "",
                "address2": "",
                "city": "",
                "postalCode": "",
                "state": ""
            },
            "commercialNumber": "",
            "contactInformation": {
                "email": "",
                "faxNumber": "",
                "name": "",
                "phoneNumber": "",
                "validContact": true
            },
            "employerId": "",
            "firstName": "",
            "lastName": "",
            "locationNumber": "",
            "middleName": "",
            "npi": "",
            "organisationName": "",
            "providerType": "",
            "providerUpinNumber": "",
            "ssn": "",
            "stateLicenseNumber": "",
            "taxonomyCode": "",
            "validBillingProvider": true,
            "validProvider": true
            }
        ],
        "receiver": {
            "organizationName": "",
            "taxId": ""
        },
        "referring": {
            "address": {
            "address1": "",
            "address2": "",
            "city": "",
            "postalCode": "",
            "state": ""
            },
            "commercialNumber": "",
            "contactInformation": {
            "email": "",
            "faxNumber": "",
            "name": "",
            "phoneNumber": "",
            "validContact": true
            },
            "employerId": "",
            "firstName": "",
            "lastName": "",
            "locationNumber": "",
            "middleName": "",
            "npi": "",
            "organisationName": "",
            "providerType": "",
            "providerUpinNumber": "",
            "ssn": "",
            "stateLicenseNumber": "",
            "taxonomyCode": "",
            "validBillingProvider": true,
            "validProvider": true
        },
        "rendering": {
            "address": {
            "address1": "",
            "address2": "",
            "city": "",
            "postalCode": "",
            "state": ""
            },
            "commercialNumber": "",
            "contactInformation": {
            "email": "",
            "faxNumber": "",
            "name": "",
            "phoneNumber": "",
            "validContact": true
            },
            "employerId": "",
            "firstName": "",
            "lastName": "",
            "locationNumber": "",
            "middleName": "",
            "npi": "",
            "organisationName": "",
            "providerType": "",
            "providerUpinNumber": "",
            "ssn": "",
            "stateLicenseNumber": "",
            "taxonomyCode": "",
            "validBillingProvider": true,
            "validProvider": true
        },
        "segmentCount": "",
        "submitter": {
            "contactInformation": {
            "email": "",
            "faxNumber": "",
            "name": "",
            "phoneNumber": "",
            "validContact": true
            },
            "organizationName": "",
            "taxId": ""
        },
        "submitterId": "",
        "subscriber": {
            "address": {
            "address1": "",
            "address2": "",
            "city": "",
            "postalCode": "",
            "state": "OH"
            },
            "dateOfBirth": str(DOBList),
            "firstName": "",
            "gender": "",
            "groupNumber": "",
            "lastName": "",
            "memberId": "",
            "middleName": "",
            "paymentResponsibilityLevelCode": "P",
            "policyNumber": "",
            "ssn": "",
            "standardHealthId": ""
        },
        "time": "",
        "tradingPartnerId": "",
        "tradingPartnerName": "",
        "tradingPartnerServiceId": "60054",
        "validSubscriber": true
    }

    print("\nFiles are written..\n\nDatabase has been modified now..")
    with open("Request_Json_File.json", "w", encoding="utf-8") as writeJsonfile:
        json.dump(data, writeJsonfile, indent=4,default=str)

# calc_logic()

def db_operations2():
    try:
        conn = pyodbc.connect('Driver={SQL Server};' 
        'Server=183.83.217.150,35001;' 
        'Database=unityprod_17092019;'
        'uid=unityAppUser;pwd=Winter@2019')
                
    except:
        print("The connection to the DB failed")
        
    with open("Request_Json_File.json", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Request and Response File for Insertions
        requestJson=json.load(readJsonfile)
        
    with open("Response_Json_File.json", "r", encoding="utf-8") as readJsonfile:
        responseJson=json.load(readJsonfile)
        
    
    values=(responseJson['claims'][0].values())
    values=list(values)
    # print(values)                   #We get all the Values as dict_values here
    
    with open("Data_from_db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
        jsonFile=json.load(readJsonfile)
        
    lenJsonFile=len(jsonFile)
    records = jsonFile[0:lenJsonFile]
    
    for i in records:
        centerId=i['CENTERID']+1
        voucherNumber=i['VoucherNumber']
        userID=i['UserId']
    
    daysToPay= str(values[0])                               #Fetching the DaystoPay
    drg=str(int(values[3]))                                 #Fetching the DRG from 4th value and False denotes to 0 by using the int function
    claimStatus=str(int(values[2]))
    missingRevenueStatus=str(int(values[5]['missing']))      #Fetching a value and inside it we have a dictionary that contains this value
    missingRevenueCodes=str(values[5]['codes'][::])
    missingProcedureStatus=str(int(values[6]['missing']))
    missingProcedureCodes=""
    errorResponse="0"
    responseJson=str(responseJson)
    requestJson=str(requestJson)
    
    if missingRevenueCodes=='[]':
        missingRevenueCodes=missingRevenueCodes.replace('[]','')        #By default [] is returned from API, we are changing it to ""
    
    cursor=conn.cursor()
    print("Header Table is updated with CENTERID : "+str(centerId))
    cursor.execute("INSERT INTO UNITY.Claims_HeaderLevelPredictions(CENTERID,VoucherNumber,UserId,DaysToPay,Drg,ClaimStatus,IsMissingRevenueCodes,MissingRevenueCodes,IsMissingProcedureCodes,missingProcedureCodes,ErrorResponse,ResponseJSON,RequestJSON) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(centerId,voucherNumber,userID,daysToPay,drg,claimStatus,missingRevenueStatus,missingRevenueCodes,missingProcedureStatus,missingProcedureCodes,errorResponse,responseJson,requestJson))       #Inserting the lines into the DB
    conn.commit()
     
# db_operations2()

def dboperations3():
    try:
        conn = pyodbc.connect('Driver={SQL Server};' 
        'Server=183.83.217.150,35001;' 
        'Database=unityprod_17092019;'
        'uid=unityAppUser;pwd=Winter@2019')
                
    except:
        print("The connection to the DB failed")
        
    with open("Request_Json_File.json", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Request and Response File for Insertions
        requestJson=json.load(readJsonfile)
        
    with open("Response_Json_File.json", "r", encoding="utf-8") as readJsonfile:
        responseJson=json.load(readJsonfile)
        
    
    values=(responseJson['claims'][0].values())
    values=list(values)
    # print(values)                   #We get all the Values as dict_values here
    
    with open("Data_from_db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
        jsonFile=json.load(readJsonfile)
        
    lenJsonFile=len(jsonFile)
    records = jsonFile[0:lenJsonFile]
    counter=0
    lenlines=len(values[4])
    # print(lenlines)
    ReasonList=[]
    ReasonProb=[]
    ECarcCodes=[]
    
    for i in records:
        centerId=i['CENTERID']+100                                       #First Line Output to DB
        voucherNumber=i['VoucherNumber']
        userId=i['UserId']
        serviceId=i['ServiceId']
        centerId+=1
        
    for j in range(0,lenlines):
        try:
            lineId1=str(values[4][j]['lineId'])
            lineStatus1=str(int(values[4][j]['lineDenied']))
            allowedAmount1=str(values[4][j]['allowedAmount'])
            denialReason=(values[4][j]['denialReasons'])
            for k in denialReason:
                ReasonList.append(k['reason'])
                ReasonProb.append(k['probability'])
                ECarcCodes.append(k['eraCarcCodes'])
            
            for k in ReasonList:
                R1=ReasonList[0]
                R2=ReasonList[1]
                R3=ReasonList[2]
                
            for k in ReasonProb:
                R1P=float(ReasonProb[0])
                R2P=float(ReasonProb[1])
                R3P=float(ReasonProb[2])
                
            for k in ECarcCodes:
                R1C1=ECarcCodes[0][0]['code']
                R1C1P=float(ECarcCodes[0][0]['probability'])                   #R1 Results
                R1C2=ECarcCodes[0][1]['code']
                R1C2P=float(ECarcCodes[0][1]['probability'])
                R1C3=ECarcCodes[0][2]['code']
                R1C3P=float(ECarcCodes[0][2]['probability'])
                
                R2C1=ECarcCodes[1][0]['code']
                R2C1P=float(ECarcCodes[1][0]['probability'])
                R2C2=ECarcCodes[1][1]['code']                           #R2 Results
                R2C2P=float(ECarcCodes[1][1]['probability'])
                R2C3=ECarcCodes[1][2]['code']
                R2C3P=float(ECarcCodes[1][2]['probability'])
                
                R3C1=ECarcCodes[2][0]['code']
                R3C1P=float(ECarcCodes[2][0]['probability'])
                R3C2=ECarcCodes[2][1]['code']                           #R3 Results
                R3C2P=float(ECarcCodes[2][1]['probability'])
                R3C3=ECarcCodes[2][2]['code']
                R3C3P=float(ECarcCodes[2][2]['probability'])
            
            centerId+=1
            
            # print(type(R1))
            
        except(KeyError):
            denialReason="{}"
            # R1=R1P=R1C1=R1C1P=R1C2=R1C2P=R1C3=R1C3P=R2=R2P=R2C1=R2C1P=R2C2=R2C2P=R2C3=R2C3P=R3=R3P=R3C1=R3C1P=R3C2=R3C2P=R3C3=R3C3P="NULL"
            centerId+=1
            print("Line Levels are updated with CENTER ID : "+str(centerId))
            cursor=conn.cursor()
        
            cursor.execute("INSERT INTO UNITY.Claims_LineLevelPredictions(CENTERID,VoucherNumber,UserId,ServiceID,LineId,LineStatus,AllowedAmount,DenialReasons) VALUES (?,?,?,?,?,?,?,?)",(centerId,voucherNumber,userId,serviceId,lineId1,lineStatus1,allowedAmount1,denialReason))       #Inserting the lines into the DB
            conn.commit()
            # centerId+=1
            continue
              
        print("Line Levels are updated with CENTER ID : "+str(centerId))
        # print(denList)
        denialReason=str(values[4][j]['denialReasons'])
        cursor=conn.cursor()
        cursor.execute("INSERT INTO UNITY.Claims_LineLevelPredictions(CENTERID,VoucherNumber,UserId,ServiceID,LineId,LineStatus,AllowedAmount,DenialReasons,R1,R1P,R1C1,R1C1P,R1C2,R1C2P,R1C3,R1C3P,R2,R2P,R2C1,R2C1P,R2C2,R2C2P,R2C3,R2C3P,R3,R3P,R3C1,R3C1P,R3C2,R3C2P,R3C3,R3C3P) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(centerId,voucherNumber,userId,serviceId,lineId1,lineStatus1,allowedAmount1,denialReason,R1,R1P,R1C1,R1C1P,R1C2,R1C2P,R1C3,R1C3P,R2,R2P,R2C1,R2C1P,R2C2,R2C2P,R2C3,R2C3P,R3,R3P,R3C1,R3C1P,R3C2,R3C2P,R3C3,R3C3P))       #Inserting the lines into the DB
        # # cursor.execute("INSERT INTO UNITY.Claims_LineLevelPredictions(CENTERID,VoucherNumber,UserId,ServiceID,LineId,LineStatus,AllowedAmount,DenialReasons) VALUES (?,?,?,?,?,?,?,?)",(centerId,voucherNumber,userId,serviceId,lineId1,lineStatus1,allowedAmount1,denialReason))       #Inserting the lines into the DB
        conn.commit()
    
        
# dboperations3()

    







    
    




