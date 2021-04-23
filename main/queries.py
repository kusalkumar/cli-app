"""
module where all the project specific functions available
"""
import json
import requests

import params


def get_token():
    """
    To get latest token to make different api requests

    Parameters
    ----------
    None

    Returns
    -------
    True, token / False, error
    """

    try:
        url = params.BASE_URL
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)
        base_url = response.get(params.CONTEXT)
        token = base_url.split("/")[-2]
        return (True, token)
    except Exception as e:
        return (False, str(e))


def get_entity_url(token, entity_id):
    """
    To get api url to get the entity information

    Parameters
    ----------
    token, str
        token to get authenticated
    entity_id: str,
        entity to which we need to get info

    Returns
    -------
    True, url / False, error
    """
    try:
        api_url = params.GET_ENTITY_URL.format(token, entity_id)
        return (True, api_url)
    except Exception as e:
        return (False, str(e))


def get_filter_fname_url(token, firstname):
    """
    To get api url to filter by firstname

    Parameters
    ----------
    token, str
        token to get authenticated
    firstname: str,
        firstname to get all the entry with that specific firstname

    Returns
    True, url / False, error
    """
    try:
        api_url = params.FILTER_BY_FNAME_URL.format(token, firstname)
        return (True, api_url)
    except Exception as e:
        return (False, str(e))


def get_filter_gender_url(token, gender):
    """
    To get api url to filter by gender

    Parameters
    ----------
    token, str
        token to get authenticated
    gender: str,
        gender to get all the entry with that specific gender

    Returns
    True, url / False, error
    """
    try:
        api_url = params.FILTER_BY_GENDER_URL.format(token, gender)
        return (True, api_url)
    except Exception as e:
        return (False, str(e))


def get_create_entity_url(token):
    """
    To get api url to create new entity

    Parameters
    ----------
    token, str
        token to get authenticated

    Returns
    True, url / False, error
    """
    try:
        api_url = params.CREATE_ENTITY_URL.format(token)
        return (True, api_url)
    except Exception as e:
        return (False, str(e))

