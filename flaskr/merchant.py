from flask import Flask
import http.client
import os
import requests
from flask import Blueprint

bp = Blueprint("blog", __name__)

@bp.route('/search/<search>')
def search(search):
    secret_key = os.getenv("GSE_SECRET_KEY")
    gse_id = os.getenv("GSE_ID")

    params = {"key": secret_key, "cx": gse_id, "q": search, "gl": "br"}
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)

    return response.json()
