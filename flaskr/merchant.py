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

    params = {"key": secret_key, "cx": gse_id, "q": search}
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)

    return response.json()
    # conn = http.client.HTTPSConnection("https://www.googleapis.com/customsearch/v1?")
    #
    # conn.request("GET", "/storeproduct/search/?q=coca", headers=headers)
    #
    # res = conn.getresponse()
    # data = res.read()
    #
    # return data.decode("utf-8")


# AIzaSyBs9BPEh4dKKatxU5YMj1_8nfWcKm7YL_g