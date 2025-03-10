from models import session, Company, Dev, Freebie

# Test Company creation
company = Company(name="Google", founding_year=1998)
session.add(company)
session.commit()

print(session.query(Company).all())  # returns the company object
