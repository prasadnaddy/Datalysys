import pyodbc,json,decimal,string

class DecimalEncoder(json.JSONEncoder):                         #Class to add up the decimals to our JSON conversion
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)                     
        return super(DecimalEncoder, self).default(o)

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
    
    command1=("SELECT * FROM UNITY.Claims_HeaderLevelPredictions WHERE VoucherNumber='3197870';")

    cursor= conn.cursor().execute(command)                      #Executing the SQL Command

    results = []

    columns = [column[0] for column in cursor.description]      #Fetching the column headers

    for row in cursor.fetchall():
        results.append(dict(zip(columns,row)))                  #Key -> Col Header and value is the Table row Values
    
    with open("db.txt", "w", encoding="utf-8") as writeJsonfile:
        json.dump(results, writeJsonfile, indent=4,cls=DecimalEncoder,default=str)                     #Writing the JSON format to a file
        
    cursor1= conn.cursor().execute(command1)
    
    results1= []
    
    columns1 = [column1[0] for column1 in cursor1.description]      #Fetching the column headers

    for row1 in cursor1.fetchall():
        results1.append(dict(zip(columns1,row1)))                  #Key -> Col Header and value is the Table row Values
    
    with open("db1.txt", "w", encoding="utf-8") as writeJsonfile:
        json.dump(results1, writeJsonfile, indent=4,cls=DecimalEncoder,default=str)  
    

connect_db()
def calc_logic():
    with open("db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
        jsonFile=json.load(readJsonfile)

    for i in jsonFile: 
        first,second,third, fourth, fifth, sixth = jsonFile[0:6]        #Fetching the serviceCodeLines separately
        
        centerId=first['CENTERID']
        voucherNumber=first['VoucherNumber']
        userId=first['UserId']
        fServiceId=first['ServiceId']                                   #Extracting Required Attributes
        DOB=first['DateOfBirth']
        Gender=first['Gender']
        ServiceDate=first['ServiceDate']
        fProCode=first['PROCode']
        fModifier=first['Modifier']
        fICDCode=first['ICDCode']+','
        fServiceFee=first['ServiceFee']
        fServiceUnits=first['ServiceUnits']
        fReasonCode=first['ReasonCodeId']
        fTimeStamp=first['TimeStamp']
        fCarrierId=first['CarrierId']
        PrimaryDiagnosis=(first['PrimaryDiagnosisCode']).strip()
        fServicePlaceId=first['ServicePlaceID_Old']
        fProcessed=first['Processed']
        VoucherCode=first['VoucherId']
        Relationship=first['RelationShipToSubscriber']

        sServiceId=second['ServiceId']                                   #Extracting Required Attributes
        sProCode=second['PROCode']
        sModifier=second['Modifier']
        sICDCode=second['ICDCode']+','
        sServiceFee=second['ServiceFee']
        sServiceUnits=second['ServiceUnits']
        sReasonCode=second['ReasonCodeId']
        sTimeStamp=second['TimeStamp']
        sCarrierId=second['CarrierId']
        sServicePlaceId=second['ServicePlaceID_Old']
        sProcessed=second['Processed']

        tServiceId=third['ServiceId']                                   #Extracting Required Attributes
        tProCode=third['PROCode']
        tModifier=third['Modifier']
        tICDCode=third['ICDCode']+','
        tServiceFee=third['ServiceFee']
        tServiceUnits=third['ServiceUnits']
        tReasonCode=third['ReasonCodeId']
        tTimeStamp=third['TimeStamp']
        tCarrierId=third['CarrierId']
        tServicePlaceId=third['ServicePlaceID_Old']
        tProcessed=third['Processed']

        fourthServiceId=fourth['ServiceId']                                   #Extracting Required Attributes
        fourthProCode=fourth['PROCode']
        fourthModifier=fourth['Modifier']
        fourthICDCode=fourth['ICDCode']+','
        fourthServiceFee=fourth['ServiceFee']
        fourthServiceUnits=fourth['ServiceUnits']
        fourthReasonCode=fourth['ReasonCodeId']
        fourthTimeStamp=fourth['TimeStamp']
        fourthCarrierId=fourth['CarrierId']
        fourthServicePlaceId=fourth['ServicePlaceID_Old']
        fourthProcessed=fourth['Processed']

        fifthServiceId=fifth['ServiceId']                                   #Extracting Required Attributes
        fifthProCode=fifth['PROCode']
        fifthModifier=fifth['Modifier']
        fifthICDCode=fifth['ICDCode']+','
        fifthServiceFee=fifth['ServiceFee']
        fifthServiceUnits=fifth['ServiceUnits']
        fifthReasonCode=fifth['ReasonCodeId']
        fifthTimeStamp=fifth['TimeStamp']
        fifthCarrierId=fifth['CarrierId']
        fifthServicePlaceId=fifth['ServicePlaceID_Old']
        fifthProcessed=fifth['Processed']

        sixthServiceId=sixth['ServiceId']                                   #Extracting Required Attributes
        sixthProCode=sixth['PROCode']
        sixthModifier=sixth['Modifier']
        sixthICDCode=sixth['ICDCode']+','
        sixthServiceFee=sixth['ServiceFee']
        sixthServiceUnits=sixth['ServiceUnits']
        sixthReasonCode=sixth['ReasonCodeId']
        sixthTimeStamp=sixth['TimeStamp']
        sixthCarrierId=sixth['CarrierId']
        sixthServicePlaceId=sixth['ServicePlaceID_Old']
        sixthProcessed=sixth['Processed']

    PrimaryDiagnosis=PrimaryDiagnosis.replace(".","")
    claimTotal= float(fServiceFee) + float(sServiceFee) + float(tServiceFee) + float(fourthServiceFee) + float(fifthServiceFee) + float(sixthServiceFee)
    print(claimTotal)
    ICDCodes=(fICDCode.strip()+sICDCode.strip()+tICDCode.strip()+fourthICDCode.strip()+fifthICDCode.strip()+sixthICDCode.strip())
    ICDCodes=ICDCodes.replace(".","")
    ICDList=list(ICDCodes.split(','))

    for i in ICDList:
        if(i==''):
            ICDList.remove(i)


    ICDCodes = (sorted(set(ICDList), key=ICDList.index))        #To Remove duplicates in the List and maintain Order of List
    
    if PrimaryDiagnosis in ICDCodes:
        ICDCodes.remove(PrimaryDiagnosis)
    print(ICDCodes)
    date=fTimeStamp.split(' ')
    ServiceDate=date[0].replace('-','')                         #Replacing the "-" in dates

    PatientDob=DOB.replace('-','')

    #Our Request Data
    data={
        "precisionThreshold": 0.85,
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
                "validContact": True
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
            "validBillingProvider": True,
            "validProvider": True
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
            "healthCareCodeInformation": [
                {
                    "diagnosisCode": str(PrimaryDiagnosis),
                    "diagnosisTypeCode": "ABK"
                },
                {
                    "diagnosisCode": str(ICDCodes[0]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[1]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[2]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[3]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[4]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[5]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[6]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[7]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[8]),
                    "diagnosisTypeCode": "ABF"
                },
                {
                    "diagnosisCode": str(ICDCodes[9]),
                    "diagnosisTypeCode": "ABF"
                }
            ],
            "patientAmountPaid": "",
            "patientControlNumber": "",
            "patientWeight": "",
            "placeOfServiceCode": str(fServiceId),
            "planParticipationCode": "A",
            "propertyCasualtyClaimNumber": "",
            "releaseInformationCode": "Y",
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
            "serviceLines": [
                {
                    "assignedNumber": "1",
                    "professionalService": {
                        "compositeDiagnosisCodePointers": {
                            "diagnosisCodePointers": [
                                "2",
                                "3",
                                "4",
                                "5",
                                "1",
                                "6",
                                "7",
                                "8",
                                "9",
                                "10",
                                "11"
                            ]
                        },
                        "description": "",
                        "lineItemChargeAmount": str(fServiceFee),
                        "measurementUnit": "UN",
                        "placeOfServiceCode": "",
                        "procedureCode": str(fProCode),
                        "procedureIdentifier": "HC",
                        "serviceUnitCount": str(fServiceUnits),
                        "procedureModifier1": ""
                    },
                    "providerControlNumber": "",
                    "serviceDate": str(ServiceDate)
                },
                {
                    "assignedNumber": "2",
                    "professionalService": {
                        "compositeDiagnosisCodePointers": {
                            "diagnosisCodePointers": [
                                "4"
                            ]
                        },
                        "description": "",
                        "lineItemChargeAmount": str(sServiceFee),
                        "measurementUnit": "UN",
                        "placeOfServiceCode": "",
                        "procedureCode": str(sServiceFee),
                        "procedureIdentifier": "HC",
                        "serviceUnitCount": str(sServiceUnits),
                        "procedureModifier1": ""
                    },
                    "providerControlNumber": "",
                    "serviceDate": str(ServiceDate)
                },
                {
                    "assignedNumber": "3",
                    "professionalService": {
                        "compositeDiagnosisCodePointers": {
                            "diagnosisCodePointers": [
                                "3",
                                "11"
                            ]
                        },
                        "description": "",
                        "lineItemChargeAmount": str(tServiceFee),
                        "measurementUnit": "UN",
                        "placeOfServiceCode": "",
                        "procedureCode": str(tProCode),
                        "procedureIdentifier": "HC",
                        "serviceUnitCount": str(tServiceUnits),
                        "procedureModifier1": ""
                    },
                    "providerControlNumber": "",
                    "serviceDate": str(ServiceDate)
                }
            ],
            "signatureIndicator": "Y"
        },
        "controlNumber": str(VoucherCode),
        "date": "",
        "dependent": {
            "dateOfBirth": str(PatientDob),
            "firstName": "John ",
            "gender": "M",
            "lastName": "Doe",
            "middleName": "",
            "relationshipToSubscriberCode": str(Relationship),
            "ssn": "",
            "address": {
                "state": "OH"
            }
        },
        "providers": [
            {
                "address": {
                    "address1": "2365",
                    "address2": "INNIS RD",
                    "city": "COLUMBUS",
                    "postalCode": "432243730",
                    "state": "OH"
                },
                "commercialNumber": "",
                "contactInformation": {
                    "email": "",
                    "faxNumber": "",
                    "name": "",
                    "phoneNumber": "",
                    "validContact": True
                },
                "employerId": "383765547",
                "firstName": "",
                "lastName": "HOFHC",
                "locationNumber": "",
                "middleName": "",
                "npi": "",
                "organisationName": "HOFHC",
                "providerType": "",
                "providerUpinNumber": "",
                "ssn": "",
                "stateLicenseNumber": "",
                "taxonomyCode": "",
                "validBillingProvider": True,
                "validProvider": True
            }
        ],
        "receiver": {
            "organizationName": "HOFHC",
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
                "validContact": True
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
            "validBillingProvider": True,
            "validProvider": True
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
                "validContact": True
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
            "validBillingProvider": True,
            "validProvider": True
        },
        "segmentCount": "",
        "submitter": {
            "contactInformation": {
                "email": "",
                "faxNumber": "",
                "name": "",
                "phoneNumber": "123456",
                "validContact": True
            },
            "organizationName": "",
            "taxId": ""
        },
        "submitterId": "",
        "subscriber": {
            "address": {
                "address1": "1234",
                "address2": "ABCD Street",
                "city": "COLUMBUS",
                "postalCode": "43232",
                "state": "OH"
            },
            "dateOfBirth": str(PatientDob),
            "firstName": "John",
            "gender": "M",
            "groupNumber": "",
            "lastName": "Doe",
            "memberId": "911111731240",
            "middleName": "",
            "paymentResponsibilityLevelCode": "P",
            "policyNumber": "",
            "ssn": "",
            "standardHealthId": ""
        },
        "time": "",
        "tradingPartnerId": "",
        "tradingPartnerName": "Anthem Blue Cross Blue Shield Ohio",
        "tradingPartnerServiceId": "SB338",
        "validSubscriber": True
    }

    print("Writing the file now..")

    with open("fileTest.txt", "w", encoding="utf-8") as writeJsonfile:
        json.dump(data, writeJsonfile, indent=4,cls=DecimalEncoder,default=str)

calc_logic()

def db_operations2():
    try:
        conn = pyodbc.connect('Driver={SQL Server};' 
        'Server=183.83.217.150,35001;' 
        'Database=unityprod_17092019;'
        'uid=unityAppUser;pwd=Winter@2019')
                
    except:
        print("The connection to the DB failed")
        
    with open("fileTest.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Request and Response File for Insertions
        requestJson=json.load(readJsonfile)
        
    with open("test.txt", "r", encoding="utf-8") as readJsonfile:
        responseJson=json.load(readJsonfile)
        
    
    values=(responseJson['claims'][0].values())
    values=list(values)
    print(values)                   #We get all the Values as dict_values here
    
    with open("db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
        jsonFile=json.load(readJsonfile)
        
    first=jsonFile[0]
    
    centerId=first['CENTERID']+1
    voucherNumber=first['VoucherNumber']
    userId=first['UserId']
    daysToPay= str(values[0])            #Fetching the DaystoPay
    drg=str(int(values[3]))                   #Fetching the DRG from 4th value and False denotes to 0 by using the int function
    claimStatus=str(int(values[2]))
    missingRevenueStatus=str(int(values[5]['missing']))      #Fetching a value and inside it we have a dictionary that contains this value
    missingRevenueCodes=str(values[5]['codes'][::])
    missingProcedureStatus=str(int(values[6]['missing']))
    missingProcedureCodes=""
    errorResponse="0"
    responseJson=str(responseJson)
    requestJson=str(requestJson)
    
    cursor=conn.cursor()
    
    cursor.execute("INSERT INTO UNITY.Claims_HeaderLevelPredictions(CENTERID,VoucherNumber,UserId,DaysToPay,Drg,ClaimStatus,IsMissingRevenueCodes,MissingRevenueCodes,IsMissingProcedureCodes,missingProcedureCodes,ErrorResponse,ResponseJSON,RequestJSON) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(centerId,voucherNumber,userId,daysToPay,drg,claimStatus,missingRevenueStatus,missingRevenueCodes,missingProcedureStatus,missingProcedureCodes,errorResponse,responseJson,requestJson))       #Inserting the lines into the DB
    conn.commit()
    
    
db_operations2()

    







    
    




