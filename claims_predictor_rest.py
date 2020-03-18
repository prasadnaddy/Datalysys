import requests
import json

#Our JSON Data 
data = {
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
        "claimChargeAmount": "220",
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
                "diagnosisCode": "G8929",
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

#Login Details
data2={
    "client_id": "CG4HmDLlVfoXZmH8SrB70P8EG5C8bL38",
    "client_secret": "8iLetYBRyJbRAb6j",
    "grant_type": "client_credentials"
}

#Function to generate the token
def token_generator():
    try:
        t=requests.post('https://apis.changehealthcare.com/apip/auth/v2/token',json=data2,verify=False)

        # print(t.text)
        response=json.loads(t.text)
       
        token = response['access_token']
        print(token)
        print("Token has been generated successfully\n\n")
        return token

    except:
        print("Please enter the correct data format")

token = token_generator()

#Header for POST Request
headers = {
    "Authorization": "Bearer "+token,
    "Content-Type":"application/json",
}


#Function to perform POST operation for the provided endpoint
def post_request():
    try:
        s= requests.post('https://apis.changehealthcare.com/ai/claims-lifecycle/medical-network/v2/prediction',headers=headers, json=data,verify=False)

        response = json.loads(s.text)
        print(response)

        
        with open("test2.txt", "w", encoding="utf-8") as writeJsonfile:
            json.dump(response, writeJsonfile, indent=4)
        

    except:
        print("Check the data format and try again")

post_request()









