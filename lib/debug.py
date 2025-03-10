#!/usr/bin/env python3

from sqlalchemy import create_engine

from models import session,Company, Dev,Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    import ipdb; ipdb.set_trace()
    # Test Dev 
    njeri = session.query(Dev).filter_by(name="Njeri").first()
    if njeri:
        print(njeri.companies)
    else:
        print("Developer Njeri not found.")

    # Test Company 
    techSolutions = session.query(Company).filter_by(name="TechSolutions").first()
    if techSolutions:
        print(techSolutions.devs)
    else:
        print("Company TechSolutions not found.")

    # Test Freebie 
    freebie = session.query(Freebie).filter_by(item_name="T-Shirt").first()
    if freebie:
        print(freebie.print_details())
    else:
        print("Freebie T-Shirt not found.")