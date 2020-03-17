import requests
import json

#Our JSON Data 
data = {

  "precisionThreshold": 0.95,
  "billerId": "",
  "billing": {
    "address": {
      "addressTrue": "",
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
    "claimChargeAmount": "",
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
    "claimFrequencyCode": "True",
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
        "diagnosisCode": "S76111D",
        "diagnosisTypeCode": ""
      },
      {
        "diagnosisCode": "M25551",
        "diagnosisTypeCode": ""
      }
    ],
    "patientAmountPaid": "",
    "patientControlNumber": "",
    "patientWeight": "",
    "placeOfServiceCode": "11",
    "planParticipationCode": "",
    "propertyCasualtyClaimNumber": "",
    "releaseInformationCode": "",
    "serviceFacilityLocation": {
      "address": {
        "addressTrue": "",
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
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97110",
          "procedureIdentifier": "HC",
          "procedureModifier1": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      },
      {
        "assignedNumber": "2",
        "professionalService": {
          "compositeDiagnosisCodePointers": {
            "diagnosisCodePointers": [
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97140",
          "procedureIdentifier": "HC",
          "procedureModifierTrue": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      },
      {
        "assignedNumber": "3",
        "professionalService": {
          "compositeDiagnosisCodePointers": {
            "diagnosisCodePointers": [
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97035",
          "procedureIdentifier": "HC",
          "procedureModifierTrue": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      },
      {
        "assignedNumber": "4",
        "professionalService": {
          "compositeDiagnosisCodePointers": {
            "diagnosisCodePointers": [
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97110",
          "procedureIdentifier": "HC",
          "procedureModifierTrue": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      },
      {
        "assignedNumber": "5",
        "professionalService": {
          "compositeDiagnosisCodePointers": {
            "diagnosisCodePointers": [
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97140",
          "procedureIdentifier": "HC",
          "procedureModifierTrue": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      },
      {
        "assignedNumber": "6",
        "professionalService": {
          "compositeDiagnosisCodePointers": {
            "diagnosisCodePointers": [
              ""
            ]
          },
          "description": "",
          "lineItemChargeAmount": "",
          "measurementUnit": "",
          "placeOfServiceCode": "11",
          "procedureCode": "97035",
          "procedureIdentifier": "HC",
          "procedureModifierTrue": "GP",
          "serviceUnitCount": ""
        },
        "providerControlNumber": "",
        "serviceDate": ""
      }
    ],
    "signatureIndicator": ""
  },
  "controlNumber": "EP031618788465567",
  "date": "",
  "dependent": {
    "dateOfBirth": "",
    "firstName": "",
    "gender": "F",
    "lastName": "",
    "middleName": "",
    "relationshipToSubscriberCode": "18",
    "ssn": "",
    "address": {
      "state": "RI"
    }
  },
  "providers": [
    {
      "address": {
        "addressTrue": "",
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
    }
  ],
  "receiver": {
    "organizationName": "",
    "taxId": ""
  },
  "referring": {
    "address": {
      "addressTrue": "",
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
      "addressTrue": "",
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
      "phoneNumber": "",
      "validContact": True
    },
    "organizationName": "",
    "taxId": ""
  },
  "submitterId": "",
  "subscriber": {
    "address": {
      "addressTrue": "",
      "address2": "",
      "city": "",
      "postalCode": "",
      "state": "RI"
    },
    "dateOfBirth": "",
    "firstName": "",
    "gender": "",
    "groupNumber": "",
    "lastName": "",
    "memberId": "",
    "middleName": "",
    "paymentResponsibilityLevelCode": "",
    "policyNumber": "",
    "ssn": "",
    "standardHealthId": ""
  },
  "time": "",
  "tradingPartnerId": "",
  "tradingPartnerName": "",
  "tradingPartnerServiceId": "60054",
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









