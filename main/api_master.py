"""A module where all the api calls get handled"""

import json
import requests

import params

class ApiMaster(object):
    """
    A class to represent all the apicalls.

    ...

    Methods
    -------
    make_requests(url, method, headers=None, body=None, query_params=None):
        makes the api request and return the response
    """

    def make_request(self, url, method, headers=None, body=None, query_params=None):
        """
        Return response after making api call with requested params

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        url : str
            api url that need to be requeted
        headers: json, optional
            What the headers required to make a request
        params: str, optional
            Any query parameters
        body: str, optional
            The required api body for request

        Returns
        -------
        Api response or error message
        """

        try:
            response = requests.request(method, url, headers=headers, params=query_params, \
                    data=body)
        except Exception as error:
            print(str(error))
            return (True, params.SOMETHING_WENT_WRONG)
        if response.status_code == 400:
            return (False, params.SOMETHING_WENT_WRONG)
        if response.status_code == 404:
            return (False, params.OBJECT_NOT_FOUND)
        if response.status_code == 500:
            return (False, params.SOMETHING_WENT_WRONG)
        if response.status_code == 201:
            try:
                return (True, json.dumps(json.loads(response.text), indent=4, sort_keys=True))
            except:
                return (False, params.SOMETHING_WENT_WRONG)
        if response.status_code == 200:
            try:
                return (True, json.dumps(json.loads(response.text), indent=4, sort_keys=True))
            except:
                return (False, params.SOMETHING_WENT_WRONG)
        else:
            return (False, params.SOMETHING_WENT_WRONG)
