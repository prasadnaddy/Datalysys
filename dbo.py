import pyodbc,json,decimal,string

class DecimalEncoder(json.JSONEncoder):                         #Class to add up the decimals to our JSON conversion
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)                     
        return super(DecimalEncoder, self).default(o)

#Connecting to our SQL Server Database using pyodbc
conn = pyodbc.connect('Driver={SQL Server};' 
'Server=192.168.0.117,3133;' 
'Database=unityprod_17092019;'
'uid=unityAppUser;pwd=Winter@2019')

command= ("SELECT * FROM UNITY.Claims_Actuals WHERE VoucherNumber='3197870';")

cursor= conn.cursor().execute(command)                      #Executing the SQL command

results = []

columns = [column[0] for column in cursor.description]      #Fetching the column headers

for row in cursor.fetchall():
    results.append(dict(zip(columns,row)))                  #Key -> Col Header and value is the Table row Values


# with open("db.txt", "w", encoding="utf-8") as writeJsonfile:
#     json.dump(results, writeJsonfile, indent=4,cls=DecimalEncoder,default=str)                     #Writing the JSON format to a file

with open("db.txt", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Database File for processing
    jsonFile=json.load(readJsonfile)

for i in jsonFile: 
    first,second,third, fourth, fifth, sixth = jsonFile[0:6]        #Fetching the serviceCodeLines separately
    
    fServiceId=first['ServiceId']                                   #Extracting Required Attributes
    DOB=first['DateOfBirth']
    Gender=first['Gender']
    ServiceDate=first['ServiceDate']
    fProCode=first['PROCode']
    fModifier=first['Modifier']
    fICDCode=first['ICDCode']
    fServiceFee=first['ServiceFee']
    fServiceUnits=first['ServiceUnits']
    fReasonCode=first['ReasonCodeId']
    fTimeStamp=first['TimeStamp']
    fCarrierId=first['CarrierId']
    PrimaryDiagnosis=(first['PrimaryDiagnosisCode']).strip()
    fServicePlaceId=first['ServicePlaceID_Old']
    fProcessed=first['Processed']

    sServiceId=second['ServiceId']                                   #Extracting Required Attributes
    sProCode=second['PROCode']
    sModifier=second['Modifier']
    sICDCode=second['ICDCode']
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
    tICDCode=third['ICDCode']
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
    fourthICDCode=fourth['ICDCode']
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
    fifthICDCode=fifth['ICDCode']
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
    sixthICDCode=sixth['ICDCode']
    sixthServiceFee=sixth['ServiceFee']
    sixthServiceUnits=sixth['ServiceUnits']
    sixthReasonCode=sixth['ReasonCodeId']
    sixthTimeStamp=sixth['TimeStamp']
    sixthCarrierId=sixth['CarrierId']
    sixthServicePlaceId=sixth['ServicePlaceID_Old']
    sixthProcessed=sixth['Processed']

claimTotal= fServiceFee + sServiceFee + tServiceFee + fourthServiceFee + fifthServiceFee + sixthServiceFee

ICDCodes=(fICDCode.strip()+sICDCode.strip()+tICDCode.strip()+fourthICDCode.strip()+fifthICDCode.strip()+sixthICDCode.strip())
ICDCodes=ICDCodes.replace(".","")
ICDList=list(ICDCodes.split(','))

for i in ICDList:
    if(i==''):
        ICDList.remove(i)


ICDCodes = (sorted(set(ICDList), key=ICDList.index))        #To Remove duplicates in the List and maintain Order of List

print(ICDCodes)

#Our Request Data
{
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
        "claimChargeAmount": claimTotal,
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
                "diagnosisCode": PrimaryDiagnosis,
                "diagnosisTypeCode": "ABK"
            },
            {
                "diagnosisCode": "C44310",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "E119",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "E669",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "E785",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "I10",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "L821",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "M25561",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "M25562",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "N3281",
                "diagnosisTypeCode": "ABF"
            },
            {
                "diagnosisCode": "Z794",
                "diagnosisTypeCode": "ABF"
            }
        ],
        "patientAmountPaid": "",
        "patientControlNumber": "",
        "patientWeight": "",
        "placeOfServiceCode": "11",
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
                    "lineItemChargeAmount": "209",
                    "measurementUnit": "UN",
                    "placeOfServiceCode": "",
                    "procedureCode": "99214",
                    "procedureIdentifier": "HC",
                    "serviceUnitCount": "1",
                    "procedureModifier1": ""
                },
                "providerControlNumber": "",
                "serviceDate": "20190130"
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
                    "lineItemChargeAmount": "0",
                    "measurementUnit": "UN",
                    "placeOfServiceCode": "",
                    "procedureCode": "S9470",
                    "procedureIdentifier": "HC",
                    "serviceUnitCount": "1",
                    "procedureModifier1": ""
                },
                "providerControlNumber": "",
                "serviceDate": "20190130"
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
                    "lineItemChargeAmount": "11",
                    "measurementUnit": "UN",
                    "placeOfServiceCode": "",
                    "procedureCode": "82947",
                    "procedureIdentifier": "HC",
                    "serviceUnitCount": "1",
                    "procedureModifier1": ""
                },
                "providerControlNumber": "",
                "serviceDate": "20190130"
            }
        ],
        "signatureIndicator": "Y"
    },
    "controlNumber": "3197870",
    "date": "",
    "dependent": {
        "dateOfBirth": "19360701",
        "firstName": "John ",
        "gender": "M",
        "lastName": "Doe",
        "middleName": "",
        "relationshipToSubscriberCode": "",
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
        "dateOfBirth": "19360701",
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










    
    




