#!/usr/bin/env python3

from sqlalchemy import create_engine

from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    #import ipdb; ipdb.set_trace()
    # Test Dev retrieval
njeri = session.query(Dev).filter_by(name="Njeri").first()
print(njeri.companies)  

# Test Company retrieval
techSolutions = session.query(Company).filter_by(name="TechSolutions").first()
print(google.devs)  

# Test Freebie retrieval
freebie = session.query(Freebie).filter_by(item_name="T-Shirt").first()
print(freebie.print_details())  