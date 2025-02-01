# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Application(Base):
    """description: This class represents the applications being managed in the CMDB."""
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Server(Base):
    """description: Describes the details of physical or virtual servers in the data center."""
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String)
    ip_address = Column(String)
    os = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Database(Base):
    """description: Represents different databases in the system."""
    __tablename__ = 'database'
    id = Column(Integer, primary_key=True, autoincrement=True)
    db_name = Column(String)
    db_type = Column(String)
    server_id = Column(Integer, ForeignKey('server.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class NetworkDevice(Base):
    """description: Detailed information about network devices."""
    __tablename__ = 'network_device'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    model = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class User(Base):
    """description: Represents users who have access to the CMDB."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    role = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class ApplicationServer(Base):
    """description: A link table connecting applications to the servers they reside on."""
    __tablename__ = 'application_server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('application.id'))
    server_id = Column(Integer, ForeignKey('server.id'))
    relation_type = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Incident(Base):
    """description: Records incidents related to servers or applications."""
    __tablename__ = 'incident'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    status = Column(String)
    priority = Column(String)
    creation_date = Column(DateTime)
    closure_date = Column(DateTime)
    server_id = Column(Integer, ForeignKey('server.id'))
    application_id = Column(Integer, ForeignKey('application.id'))

class SoftwareLicense(Base):
    """description: Details of software licenses in use within the organization."""
    __tablename__ = 'software_license'
    id = Column(Integer, primary_key=True, autoincrement=True)
    software_name = Column(String)
    license_key = Column(String)
    number_of_users = Column(Integer)
    expiration_date = Column(DateTime)
    purchase_date = Column(DateTime)
    server_id = Column(Integer, ForeignKey('server.id'))

class DataCenter(Base):
    """description: Represents information about different data centers."""
    __tablename__ = 'data_center'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class BackupSchedule(Base):
    """description: Describes backup schedules for servers."""
    __tablename__ = 'backup_schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    schedule_time = Column(DateTime)
    frequency = Column(String)
    last_backup = Column(DateTime)

class ConfigurationItem(Base):
    """description: General representation of configuration items not covered by specific entities above."""
    __tablename__ = 'configuration_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    ci_type = Column(String)
    operational_status = Column(String)
    owner = Column(String)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Vendor(Base):
    """description: Stores vendor details related to various systems and assets."""
    __tablename__ = 'vendor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    contact_email = Column(String)
    phone_number = Column(String)
    updated_at = Column(DateTime)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    app1 = Application(name="Inventory Management", description="Handles stock and supply chain activities.", created_at=date(2021, 1, 1), updated_at=date(2021, 6, 1))
    app2 = Application(name="HR Portal", description="Manages employee records and payments.", created_at=date(2020, 3, 15), updated_at=date(2021, 9, 30))
    server1 = Server(hostname="server1", ip_address="192.168.1.10", os="Linux", created_at=date(2021, 1, 20), updated_at=date(2021, 10, 20))
    server2 = Server(hostname="server2", ip_address="192.168.1.12", os="Windows Server 2016", created_at=date(2020, 2, 18), updated_at=date(2021, 7, 22))
    db1 = Database(db_name="app_db1", db_type="PostgreSQL", server_id=1, created_at=date(2021, 2, 1), updated_at=date(2021, 11, 1))
    db2 = Database(db_name="hr_db", db_type="Oracle", server_id=2, created_at=date(2020, 5, 10), updated_at=date(2021, 10, 10))
    network_device1 = NetworkDevice(type="Router", model="Cisco2900", ip_address="10.0.0.1", created_at=date(2019, 5, 4), updated_at=date(2021, 6, 30))
    network_device2 = NetworkDevice(type="Switch", model="Netgear24Port", ip_address="10.0.0.45", created_at=date(2021, 7, 15), updated_at=date(2021, 11, 10))
    user1 = User(username="john.doe", email="john.doe@example.com", role="Administrator", created_at=date(2021, 1, 1), updated_at=date(2021, 6, 1))
    user2 = User(username="jane.smith", email="jane.smith@example.com", role="User", created_at=date(2020, 3, 15), updated_at=date(2021, 9, 30))
    application_server1 = ApplicationServer(application_id=1, server_id=1, relation_type="Primary Host", created_at=date(2021, 3, 15), updated_at=date(2021, 7, 15))
    incident1 = Incident(title="Server Overload", status="Open", priority="High", creation_date=date(2021, 5, 21), closure_date=None, server_id=1, application_id=1)
    software_license1 = SoftwareLicense(software_name="MS Office", license_key="XXXXXXXXXX", number_of_users=50, expiration_date=date(2022, 8, 20), purchase_date=date(2020, 8, 20), server_id=2)
    data_center1 = DataCenter(name="London DC", location="London", capacity=500, created_at=date(2021, 3, 10), updated_at=date(2021, 11, 2))
    backup_schedule1 = BackupSchedule(server_id=1, schedule_time=date(2021, 3, 15), frequency="Weekly", last_backup=date(2021, 11, 1))
    configuration_item1 = ConfigurationItem(name="Firewall", ci_type="Security", operational_status="Operational", owner="Security Team", created_at=date(2021, 9, 1), deleted_at=None)
    vendor1 = Vendor(name="Amazon AWS", contact_email="aws_support@amazon.com", phone_number="+18005551234", updated_at=date(2021, 8, 5))
    
    
    
    session.add_all([app1, app2, server1, server2, db1, db2, network_device1, network_device2, user1, user2, application_server1, incident1, software_license1, data_center1, backup_schedule1, configuration_item1, vendor1])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
