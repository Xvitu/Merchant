from flask import current_app


class GoogleSearchEngineRequest:

    def __init__(self, search_term, location='br'):
        self.__search_term = search_term
        self.__location = location
        self.__secret_key = current_app.config.get("GSE_SECRET_KEY")
        self.__search_engine_id = current_app.config.get("GSE_ID")

    def get_params(self):
        return {"key": self.__secret_key, "cx": self.__search_engine_id, "q": self.__search_term, "gl": self.__location}
