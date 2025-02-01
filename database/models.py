# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  February 01, 2025 06:17:01
# Database: sqlite:////tmp/tmp.gI8scnqlYt-01JK02E5MT5311C6RY0AK39E66/CMDB_Data_Models/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Application(Base):  # type: ignore
    """
    description: This class represents the applications being managed in the CMDB.
    """
    __tablename__ = 'application'
    _s_collection_name = 'Application'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ApplicationServerList : Mapped[List["ApplicationServer"]] = relationship(back_populates="application")
    IncidentList : Mapped[List["Incident"]] = relationship(back_populates="application")



class ConfigurationItem(Base):  # type: ignore
    """
    description: General representation of configuration items not covered by specific entities above.
    """
    __tablename__ = 'configuration_item'
    _s_collection_name = 'ConfigurationItem'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ci_type = Column(String)
    operational_status = Column(String)
    owner = Column(String)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class DataCenter(Base):  # type: ignore
    """
    description: Represents information about different data centers.
    """
    __tablename__ = 'data_center'
    _s_collection_name = 'DataCenter'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class NetworkDevice(Base):  # type: ignore
    """
    description: Detailed information about network devices.
    """
    __tablename__ = 'network_device'
    _s_collection_name = 'NetworkDevice'  # type: ignore

    id = Column(Integer, primary_key=True)
    type = Column(String)
    model = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Server(Base):  # type: ignore
    """
    description: Describes the details of physical or virtual servers in the data center.
    """
    __tablename__ = 'server'
    _s_collection_name = 'Server'  # type: ignore

    id = Column(Integer, primary_key=True)
    hostname = Column(String)
    ip_address = Column(String)
    os = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ApplicationServerList : Mapped[List["ApplicationServer"]] = relationship(back_populates="server")
    BackupScheduleList : Mapped[List["BackupSchedule"]] = relationship(back_populates="server")
    DatabaseList : Mapped[List["Database"]] = relationship(back_populates="server")
    IncidentList : Mapped[List["Incident"]] = relationship(back_populates="server")
    SoftwareLicenseList : Mapped[List["SoftwareLicense"]] = relationship(back_populates="server")



class User(Base):  # type: ignore
    """
    description: Represents users who have access to the CMDB.
    """
    __tablename__ = 'user'
    _s_collection_name = 'User'  # type: ignore

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    role = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Vendor(Base):  # type: ignore
    """
    description: Stores vendor details related to various systems and assets.
    """
    __tablename__ = 'vendor'
    _s_collection_name = 'Vendor'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_email = Column(String)
    phone_number = Column(String)
    updated_at = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class ApplicationServer(Base):  # type: ignore
    """
    description: A link table connecting applications to the servers they reside on.
    """
    __tablename__ = 'application_server'
    _s_collection_name = 'ApplicationServer'  # type: ignore

    id = Column(Integer, primary_key=True)
    application_id = Column(ForeignKey('application.id'))
    server_id = Column(ForeignKey('server.id'))
    relation_type = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)
    application : Mapped["Application"] = relationship(back_populates=("ApplicationServerList"))
    server : Mapped["Server"] = relationship(back_populates=("ApplicationServerList"))

    # child relationships (access children)



class BackupSchedule(Base):  # type: ignore
    """
    description: Describes backup schedules for servers.
    """
    __tablename__ = 'backup_schedule'
    _s_collection_name = 'BackupSchedule'  # type: ignore

    id = Column(Integer, primary_key=True)
    server_id = Column(ForeignKey('server.id'))
    schedule_time = Column(DateTime)
    frequency = Column(String)
    last_backup = Column(DateTime)

    # parent relationships (access parent)
    server : Mapped["Server"] = relationship(back_populates=("BackupScheduleList"))

    # child relationships (access children)



class Database(Base):  # type: ignore
    """
    description: Represents different databases in the system.
    """
    __tablename__ = 'database'
    _s_collection_name = 'Database'  # type: ignore

    id = Column(Integer, primary_key=True)
    db_name = Column(String)
    db_type = Column(String)
    server_id = Column(ForeignKey('server.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # parent relationships (access parent)
    server : Mapped["Server"] = relationship(back_populates=("DatabaseList"))

    # child relationships (access children)



class Incident(Base):  # type: ignore
    """
    description: Records incidents related to servers or applications.
    """
    __tablename__ = 'incident'
    _s_collection_name = 'Incident'  # type: ignore

    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)
    priority = Column(String)
    creation_date = Column(DateTime)
    closure_date = Column(DateTime)
    server_id = Column(ForeignKey('server.id'))
    application_id = Column(ForeignKey('application.id'))

    # parent relationships (access parent)
    application : Mapped["Application"] = relationship(back_populates=("IncidentList"))
    server : Mapped["Server"] = relationship(back_populates=("IncidentList"))

    # child relationships (access children)



class SoftwareLicense(Base):  # type: ignore
    """
    description: Details of software licenses in use within the organization.
    """
    __tablename__ = 'software_license'
    _s_collection_name = 'SoftwareLicense'  # type: ignore

    id = Column(Integer, primary_key=True)
    software_name = Column(String)
    license_key = Column(String)
    number_of_users = Column(Integer)
    expiration_date = Column(DateTime)
    purchase_date = Column(DateTime)
    server_id = Column(ForeignKey('server.id'))

    # parent relationships (access parent)
    server : Mapped["Server"] = relationship(back_populates=("SoftwareLicenseList"))

    # child relationships (access children)
