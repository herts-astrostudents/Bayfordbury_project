import requests
import json
from .utilities import Filter


class ArchiveApi(object):
    def __init__(self, api_key=None, observer_id=None):
        """Bayfordbury Archive API layer. See documentation here: https://observatory.herts.ac.uk/wiki/API

        api_key, str : your API key

        observer_id, int : your observer ID
        """

        assert api_key is not None, "You need an API key to search and download from Bayfordbury servers. Get one from https://observatory.herts.ac.uk/telescopes/myaccount.php"
        assert observer_id is not None, "You need an Observer ID to search and download from Bayfordbury servers. You can find it at https://observatory.herts.ac.uk/telescopes/myaccount.php"

        self.api_key = api_key
        self.observer_id = observer_id

        self._search_url   = "https://observatory.herts.ac.uk/api/imagesearch.php"
        self._download_url = "https://observatory.herts.ac.uk/api/getfit.php"
    

    def search(self, ra, dec, radius, minjd=None, maxjd=None, minexp=None, maxexp=None, solved=False, mine=False):
        """Search for images in archive around coordinates, within a certain radius.

        ra, float       : right ascention of the search center, decimal degrees, required.

        dec, float      : declination of the search center, decimal degrees, required.

        radius, float   : search radius, decimal degrees, required.

        minjd, float    : earliest Julian date of the observation, optional.

        maxjd, float    : latest Julian date of the observation, optional.

        minexp, float   : shortest exposure time of the observation, seconds, optional.

        maxexp, float   : longest exposure time of the observation, seconds, optional.

        solved, boolean : must be plate solved, optional.

        mine, boolean   : return only your images.
        """
        assert ra is not None, "ra parameter is required."
        assert dec is not None, "dec parameter is required."
        assert radius is not None, "radius parameter is required."

        # construct a query parameters dictionary
        params = { # required parameters and those with a default value
            "key"    : self.api_key,
            "id"     : self.observer_id,
            "ra"     : ra,
            "dec"    : dec,
            "dist"   : radius,
            "solved" : solved,
            "mine"   : mine
        }

        if minjd is not None:
            params["minjd"] = minjd

        if maxjd is not None:
            params["maxjd"] = maxjd

        if minexp is not None:
            params["minexp"] = minexp

        if maxexp is not None:
            params["maxexp"] = maxexp
        
        # send the request
        response = requests.get(self._search_url, params)

        if not response.ok:  # something went wrong
            raise ConnectionError("Server responded with {} {}. Please check your request parameters and/ot refer to the documentation: https://observatory.herts.ac.uk/wiki/API".format(response.status_code, response.reason))
        
        return self._unpack_search_response(response.content)
    

    def _unpack_search_response(self, response):
        column_names = ["id", "ra", "dec", "dist", "exp", "tel", "bin", "jd", "filter"]
        response_dictionary = json.loads(response)
        
        # TODO : error here, test it
        if "Exception" in response_dictionary and response_dictionary["Exception"] == True:
            if "no_matching_images" in response_dictionary["ExceptionReason"]:
                return []
            if "verification_failed" in response_dictionary["ExceptionReason"]:
                raise PermissionError("Verification failed for the <observer_id> and <api_key> you provided.")
            else:
                raise NotImplementedError("Some error has occurred during your request, but was not handled here ¯\_(ツ)_/¯ .")

        images_data = response_dictionary["images"]

        return [value for key, value in images_data.items()]