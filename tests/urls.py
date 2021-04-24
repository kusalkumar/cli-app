BASE_URL = "http://services.odata.org/TripPinRESTierService"
GET_POS_TEST_URL = "http://services.odata.org/TripPinRESTierService/{}/People('russellwhyte')"
GET_NEG_TEST_URL = "http://services.odata.org/TripPinRESTierService/{}/People('')"
FILTER_POS_TEST_URL = "https://services.odata.org/TripPinRESTierService/{}/People?$filter=Gender eq 'Male'"
FILTER_NEG_TEST_URL = "https://services.odata.org/TripPinRESTierService/{}/People?$filter=Gender eq ''"
CREATE_API_URL = "https://services.odata.org/TripPinRESTierService/{}/People"

CREATE_POS_jSON = {
  "UserName": "kusal",
  "FirstName": "kusalkumar",
  "LastName": "jalli",
  "Emails": [
    "kusal@gmail.com"
  ],
  "AddressInfo": [
    {
      "Address": "tirupati",
      "City": {
        "Name": "tirupati",
        "CountryRegion": "india",
        "Region": "524132"
      }
    }
  ]
}

CREATE_NEG_JSON = {
  "UserName": "kusal",
  "FirstName": "kusalkumar",
  "LastName": "jalli",
  "gender":"Male",
  "Emails": [
    "kusal@gmail.com"
  ],
  "AddressInfo": [
    {
      "Address": "tirupati",
      "City": {
        "Name": "tirupati",
        "CountryRegion": "india",
        "Region": "524132"
      }
    }
  ]
}

