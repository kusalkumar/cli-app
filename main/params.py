""" all the common strings or parameters """

BASE_URL = "http://services.odata.org/TripPinRESTierService"
CONTEXT = "@odata.context"
GET_ENTITY_URL = "http://services.odata.org/TripPinRESTierService/{}/People('{}')"
FILTER_BY_FNAME_URL = "https://services.odata.org/TripPinRESTierService/{}/People?$filter=FirstName eq '{}'"
FILTER_BY_GENDER_URL = "https://services.odata.org/TripPinRESTierService/{}/People?$filter=Gender eq '{}'"
CREATE_ENTITY_URL = "https://services.odata.org/TripPinRESTierService/{}/People"

BASIC_INFO_QUESTIONS = {
        "UserName": "Username: ",
        "FirstName": "Firstname: ",
        "LastName": "Lastname: "
        }

ADDRESS_INFO_QUESTIONS = [
        {
            "key": "Address",
            "question": "proved you address (eg:87 Suffolk Ln.): ",
            "is_parent_key": True
        },
        {
            "key":"Name",
            "question": "Enter city name: ",
            "is_parent_key": False,
            "parent_key": "City",
        },
        {
            "key":"CountryRegion",
            "question": "Enter country: ",
            "is_parent_key": False,
            "parent_key": "City",
        },
        {
            "key":"Region",
            "question": "Enter city region id: ",
            "is_parent_key": False,
            "parent_key": "City",
        },
        ]

#messages
WELCOME_MESSAGE = """Welcome to CLI application.
To know more about application. 
please refere for user manual guide:
https://docs.google.com/document/d/1psrxaVwLwfmVU0CvcI393Dx9ENfB1w4n31CejDFc-7Y/edit?usp=sharing

exit is a hidden command in every step
user exit or ctrl+c or ctrl+d to exit from application"""

SOMETHING_WENT_WRONG = "Something went wrong. Please contact support"
OBJECT_NOT_FOUND = "Your requested input are not found. Please verify your input"
WAITING_MESSAGE = "This take few moments. Please wait..."
ADRESS_MESSAGE = """Note: You can enter multiple address. once you are done please
press enter keyword or n/N as input"""


regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
