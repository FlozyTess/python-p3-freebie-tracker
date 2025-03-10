from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

# Naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Base class
class Base(DeclarativeBase):
    metadata = metadata

# Database connection
engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session() 


# Many-to-Many association table
dev_company_association = Table(
    "dev_company", Base.metadata,
    Column("dev_id", Integer, ForeignKey("devs.id"),primary_key=True),
    Column("company_id", Integer, ForeignKey("companies.id"),primary_key=True)
)

class Freebie(Base):
    __tablename__ = "freebies"
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey("devs.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relationships
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        """Returns a formatted string with freebie details."""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    # Relationships
    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary=dev_company_association, back_populates="companies")

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, session, dev, item_name, value):
        """Creates a new freebie given to a developer by this company."""
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls, session):
        """Finds and returns the oldest company."""
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationships
    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship("Company", secondary=dev_company_association, back_populates="devs")

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        """Checks if the dev has received a freebie with a specific name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, session, dev, freebie):
        """Transfers a freebie from this dev to another dev."""
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()

Base.metadata.create_all(engine)
__all__ = ["Company", "Dev", "Freebie","dev_company_association"]