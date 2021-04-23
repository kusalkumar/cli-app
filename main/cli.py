import json

import queries
import params
import utility

from api_master import ApiMaster


def get_choice(options):
    """
    Function to get user input from option provided

    Parameters
    ----------
    options : list
        list of all options to user

    Returns
    -------
    user selected option
    """

    print("please choose the option:")
    for option in options:
        print("- {} - {}".format(option[0].upper(),option[1]))
    print("[]>",end =" ")
    choice = input()
    return choice


def menu_for_get():
    """
    Function to get user input from user

    Returns
    -------
    user input to get the entity details by id 
    """
    entity_id = None
    try:
        entity_id = str(input("Enter entity id to get details: "))
    except ValueError:
        print("Enter valid number")
    except (KeyboardInterrupt, EOFError) as error:
        print("\n")
        print("Thank You")
        return None
    except:
        print('You have entered an invalid value.')
    return entity_id


def menu_to_filter():
    """
    Function to get user input from options provided

    Returns
    -------
    user selected option to get filter result
    """
    try:
        print("\n")
        selected_option = {}
        options = [('FIRSTNAME', 'filter by firstname'), ('GENDER', 'filter by gender')]
        while 1:
            option = get_choice(options)
            if option.lower() == "firstname":
                firstname = str(input("Enter firstaname to filter: "))
                selected_option["firstname"] = firstname
                break
            elif option.lower() == "gender":
                gender = str(input("Enter gender to filter: "))
                selected_option["gender"] = gender
                break
            elif option.lower() == "exit":
                return "exit"
            else:
                print("choose proper option", end="\n\n")

        return selected_option
    except (KeyboardInterrupt, EOFError) as error:
        print("\n")
        print("Thank You")
        return None
    except ValueError:
        print("Enter valid number")
    except Exception as e:
        print('You have entered an invalid value.')
    return False


def get_basic_info():
    """
    Function to get user input from different questions

    Returns
    -------
    user provided answers 
    """
    print("\n")
    print("Please provide the below infomation\n")
    basic_questions = params.BASIC_INFO_QUESTIONS
    answers = {}
    for key, question in basic_questions.items():
        ans = input(question)
        answers[key] = ans
    return answers


def get_emails():
    """
    Function to get user email input and validate them

    Returns
    -------
    list of user provided mails
    """
    print("\n")
    print("Note: You can enter multiple emails. once you are done please press enter keyword")
    n = 1
    emails = []
    while 1:
        msg = "Enter your {} email address: ".format(utility.ordinal(n))
        email = input(msg)
        if not email:
            break
        validate = utility.check(email)
        if not validate:
            print("Please enter valid email address")
        else:
            emails.append(email)
            n += 1
    return emails

def get_address_info():
    """
    Function to get user input from address related questions

    Returns
    -------
    user provided answers  in the form of list
    """
    print("\n")
    address_queries = params.ADDRESS_INFO_QUESTIONS
    addresses_info = []
    n = 1
    print(params.ADRESS_MESSAGE)
    while 1:
        print("\n")
        msg = "Enter your {} address info (y/n): ".format(utility.ordinal(n))
        ans = input(msg)
        if ans.lower() == "n" or not ans:
            break
        address = {}
        for query in address_queries:
            answer = input(query.get("question"))
            if query.get("is_parent_key"):
                address[query.get("key")] = answer
            else:
                if query.get("parent_key") not in address.keys():
                    address[query.get("parent_key")] = {}

                address[query.get("parent_key")][query.get("key")] = answer
        addresses_info.append(address)
        n += 1
    return addresses_info

def menu_to_create():
    try:
        info = get_basic_info()
        emails = get_emails()
        addresses = get_address_info()
        info["Emails"] = emails
        info["AddressInfo"] = addresses
        return (True, info)
    except Exception as e:
        print(str(e))
        print(params.SOMETHING_WENT_WRONG)
        return(False, str(e))


if __name__ == '__main__':
    print(params.WELCOME_MESSAGE)
    print("")
    menu_options = [('GET', 'get entity details by id'), \
            ('CREATE', 'Create new entity'), ('FILTER', 'get entities by filter')]
    details = None
    create_entity = False
    entity_id = None
    filter_entity = None

    while 1:
        try:
            list_array = None
            choice = get_choice(menu_options)
            if choice.lower() == "get":
                entity_id = menu_for_get()
                break
            elif choice.lower() == "create":
                create_entity, details = menu_to_create()
                break
            elif choice.lower() == "filter":
                filter_entity = menu_to_filter()
                if filter_entity == "exit":
                    print("\n")
                    continue
                break
            elif choice.lower() == "exit":
                print("\n")
                print("Thank You ")
                break
            else:
                print("choose proper option", end="\n\n")
        except (KeyboardInterrupt, EOFError) as e:
            print("\n")
            print("Thank You")
            break

    if create_entity:
        success, token = queries.get_token()
        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()

        success, api_url = queries.get_create_entity_url(token)
        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()

        headers = {
                'Content-Type': 'application/json'
                }
        payload = json.dumps(details)
        api_call = ApiMaster()
        success, response = api_call.make_request(api_url, "POST", headers=headers, body=payload)
        if success:
            print("Your entry created successfully. Below are the details")
        print(response)

    if filter_entity:
        success, token = queries.get_token()

        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()
        if filter_entity.get("firstname"):
            success, api_url = queries.get_filter_fname_url(token, filter_entity.get("firstname"))
        elif filter_entity.get("gender"):
            success, api_url = queries.get_filter_gender_url(token, filter_entity.get("gender"))
        else:
            print(params.SOMETHING_WENT_WRONG)
            exit()

        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()

        payload={}
        headers = {}
        api_call = ApiMaster()
        success, response = api_call.make_request(api_url, "GET", headers=headers, body=payload)
        if success:
            print("Your request to filter happened successfully")
        print(response)

    if entity_id:
        print("")
        print(params.WAITING_MESSAGE)
        print("Requesting to get entity with bwlow id: {}".format(entity_id))
        success, token = queries.get_token()
        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()
        success, api_url = queries.get_entity_url(token, entity_id)
        if not success:
            print(params.SOMETHING_WENT_WRONG)
            exit()
        payload={}
        headers = {}

        api_call = ApiMaster()
        success, response = api_call.make_request(api_url, "GET", headers=headers, body=payload)
        if success:
            print("Your request to get data successfully")
        print(response)
