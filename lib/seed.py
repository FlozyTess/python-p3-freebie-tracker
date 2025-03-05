#!/usr/bin/env python3
from models import Company, Dev, Freebie
from database import Session
# Script goes here!
#sample companies
safaricom = Company(name="Safaricom", founding_year="2004")
gonline = Company(name="Gonline",founding_year="2023")
#sample devs
rency = Dev(name="Rency")
edith = Dev(name="Edith")
# Assign freebies
freebie1 = Freebie(item_name="Safaricom data"value=1000, dev=rency,company=safaricom)
freebie2 = Freebie(item_name="Gonline T-shirt"value=100, dev=edith,company=gonline)
session.add_all([safaricom,gonline,rency,edith,freebie1,freebie2])
session.commit()
session.close()
