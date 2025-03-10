#!/usr/bin/env python3

from models import session, Company, Dev, Freebie,dev_company_association

# Clear existing data
session.execute(dev_company_association.delete())
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Create Companies
techSolutions = Company(name="TechSolutions", founding_year=1995)
innovationx = Company(name="InnovationX", founding_year=2010)

# Create Devs
njeri = Dev(name="Njeri")
joyce = Dev(name="Joyce")
 
 # Create Many-to-Many relationships
njeri.companies.append(techSolutions)
joyce.companies.append(innovationx)

# Create Freebies
freebie1 = Freebie(item_name="T-Shirt", value=500, company=techSolutions, dev=njeri)
freebie2 = Freebie(item_name="Mug", value=100, company=innovationx, dev=joyce)

session.add_all([techSolutions,innovationx , njeri, joyce, freebie1, freebie2])
session.commit()

