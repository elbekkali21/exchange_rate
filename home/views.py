from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup
from django.shortcuts import render



def createdatabase():
    r = requests.get("https://api.frankfurter.app/2020-01-01..2020-12-11")
    data = r.json()
    rates = data["rates"]
    for i in rates:
        for a in rates[i]:
            print(a)
            print(rates[i][a])


