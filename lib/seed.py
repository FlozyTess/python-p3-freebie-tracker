#!/usr/bin/env python3
from models import Company, Dev, Freebie
from database import Session
# Script goes here!
#sample companies
company1 = Company(name="Safaricom", founding_year="2004")
company2 = Company(name="Gonline",founding_year="2023")
#sample devs
dev1 = Dev(name="Rency")
dev2 = Dev(name="Edith")
# Assign freebies
freebie1 = Freebie(item_name="Safaricom data",value=1000,dev=dev1,company=company1)
freebie2 = Freebie(item_name="Gonline T-shirt",value=100, dev=dev2,company=company2)
session.add_all([company1,company2,dev1,dev2,freebie1,freebie2])
session.commit()
session.close()
