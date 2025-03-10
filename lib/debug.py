#!/usr/bin/env python3

from sqlalchemy import create_engine

from models import Company, Dev
from database import Session
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/freebies.db')
    #import ipdb; ipdb.set_trace()
session = Session()
rency = session.query(Dev).filter_by(name="Rency").first()
print(rency.companies)  
