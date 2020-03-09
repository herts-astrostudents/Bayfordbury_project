import requests
import tempfile
import json
from astropy.io import fits

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
        self._handle_bad_response(response)
        
        return self._unpack_search_response(response.content)


    def download(self, image_id, saveto=None):
        """
        Download an image from Bayfordbury Archive.

        image_id, int : database ID in the archive.

        saveto, str : path to save the .fits file to. If None, creates a temporary file (in /tmp if you're using Linux)

        Returns an Astropy FITS image.
        """
        assert isinstance(image_id, int), "image_id must be an integer number."

        # construct a query parameters dictionary
        params = { # required parameters and those with a default value
            "key"    : self.api_key,
            "id"     : self.observer_id,
            "dbid"   : image_id
        }

        # send the request
        response = requests.get(self._download_url, params, stream=True)
        self._handle_bad_response(response)

        # create the file handle
        file_handle = tempfile.NamedTemporaryFile(mode="wb") if saveto is None else open(saveto, "wb")
        # write the bytes to the new file
        with file_handle as handle:
            for block in response.iter_content(1024):
                handle.write(block)
            file_path = file_handle.name if saveto is None else saveto
            file_instance = fits.open(file_path, ignore_missing_end=True, cache=False)

        return file_instance
        

    def _handle_bad_response(self, response):
        """
        Raises:
            HTTPStatus errors if any.
            PermissionError if credentials are wrong.
            FileNotFoundError if image ID is not in the Bayfordbury archive.
        """
        response.raise_for_status()
        # wrap this in try/catch in case the response is not actual JSON (could be file data, for instance)
        try:
            response_dictionary = json.loads(response.content)
        except:
            return

        if "Exception" in response_dictionary and response_dictionary["Exception"] == True:
            if "verification_failed" in response_dictionary["ExceptionReason"]:
                raise PermissionError("Verification failed for the <observer_id> and <api_key> you provided.")
            elif "image_id_not_found" in response_dictionary["ExceptionReason"]:
                raise FileNotFoundError("File with a supplie ID not found in Bayfordbury archive.")


    def _unpack_search_response(self, response):
        """
        Converts json returned by the server's 'search' API to a list of dictionaries.

        response, byte array : server response

        Returns a list of images found.
        """
        column_names = ["id", "ra", "dec", "dist", "exp", "tel", "bin", "jd", "filter"]
        response_dictionary = json.loads(response)
        
        if "Exception" in response_dictionary and response_dictionary["Exception"] == True:
            if "no_matching_images" in response_dictionary["ExceptionReason"]:
                return []
            else:
                raise NotImplementedError("Server returned an error <{}>, but it was not handled here ¯\_(ツ)_/¯ .".format(response_dictionary["ExceptionReason"]))
    
        return [value for key, value in response_dictionary["images"].items()]