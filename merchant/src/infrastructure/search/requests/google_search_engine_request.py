from settings import GSE_SECRET_KEY, GSE_ID


class GoogleSearchEngineRequest:

    def __init__(self, search_term, location='br'):
        self.__search_term = search_term
        self.__location = location
        self.__secret_key = GSE_SECRET_KEY
        self.__search_engine_id = GSE_ID

    def get_params(self):
        return {"key": self.__secret_key, "cx": self.__search_engine_id, "q": self.__search_term, "gl": self.__location}
