
class ResourceBase(object):
    """
        Base class representing required methods to be implemented by all resource
        classes
        (if get_count(), get_resource_urls() and get_sample_data() this method is not in any resource class its showing
        NotImplementationError)
        second option is use abstraction - make same function and use

    """

    resources = ["planets", "starships", "people",
                 "vehicle", "films", "species"]

    def __init__(self) -> None:
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError

    def get_resource_urls(self):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError