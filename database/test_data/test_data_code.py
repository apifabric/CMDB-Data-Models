import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -4072400417760347827 in succeeded_hashes:  # avoid duplicate inserts
            instance = app1 = Application(name="Inventory Management", description="Handles stock and supply chain activities.", created_at=date(2021, 1, 1), updated_at=date(2021, 6, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4072400417760347827)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8798357710598005551 in succeeded_hashes:  # avoid duplicate inserts
            instance = app2 = Application(name="HR Portal", description="Manages employee records and payments.", created_at=date(2020, 3, 15), updated_at=date(2021, 9, 30))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8798357710598005551)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5513636774175049999 in succeeded_hashes:  # avoid duplicate inserts
            instance = server1 = Server(hostname="server1", ip_address="192.168.1.10", os="Linux", created_at=date(2021, 1, 20), updated_at=date(2021, 10, 20))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5513636774175049999)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -386352874038373539 in succeeded_hashes:  # avoid duplicate inserts
            instance = server2 = Server(hostname="server2", ip_address="192.168.1.12", os="Windows Server 2016", created_at=date(2020, 2, 18), updated_at=date(2021, 7, 22))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-386352874038373539)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8131885899631642250 in succeeded_hashes:  # avoid duplicate inserts
            instance = db1 = Database(db_name="app_db1", db_type="PostgreSQL", server_id=1, created_at=date(2021, 2, 1), updated_at=date(2021, 11, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8131885899631642250)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5794342974323726522 in succeeded_hashes:  # avoid duplicate inserts
            instance = db2 = Database(db_name="hr_db", db_type="Oracle", server_id=2, created_at=date(2020, 5, 10), updated_at=date(2021, 10, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5794342974323726522)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5367034831618380169 in succeeded_hashes:  # avoid duplicate inserts
            instance = network_device1 = NetworkDevice(type="Router", model="Cisco2900", ip_address="10.0.0.1", created_at=date(2019, 5, 4), updated_at=date(2021, 6, 30))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5367034831618380169)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5161815097359071056 in succeeded_hashes:  # avoid duplicate inserts
            instance = network_device2 = NetworkDevice(type="Switch", model="Netgear24Port", ip_address="10.0.0.45", created_at=date(2021, 7, 15), updated_at=date(2021, 11, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5161815097359071056)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1848645890650245284 in succeeded_hashes:  # avoid duplicate inserts
            instance = user1 = User(username="john.doe", email="john.doe@example.com", role="Administrator", created_at=date(2021, 1, 1), updated_at=date(2021, 6, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1848645890650245284)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4186933393721913442 in succeeded_hashes:  # avoid duplicate inserts
            instance = user2 = User(username="jane.smith", email="jane.smith@example.com", role="User", created_at=date(2020, 3, 15), updated_at=date(2021, 9, 30))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4186933393721913442)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4398207380682442073 in succeeded_hashes:  # avoid duplicate inserts
            instance = application_server1 = ApplicationServer(application_id=1, server_id=1, relation_type="Primary Host", created_at=date(2021, 3, 15), updated_at=date(2021, 7, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4398207380682442073)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6195838579844440996 in succeeded_hashes:  # avoid duplicate inserts
            instance = incident1 = Incident(title="Server Overload", status="Open", priority="High", creation_date=date(2021, 5, 21), closure_date=None, server_id=1, application_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6195838579844440996)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1948854974507127199 in succeeded_hashes:  # avoid duplicate inserts
            instance = software_license1 = SoftwareLicense(software_name="MS Office", license_key="XXXXXXXXXX", number_of_users=50, expiration_date=date(2022, 8, 20), purchase_date=date(2020, 8, 20), server_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1948854974507127199)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 505293319238583145 in succeeded_hashes:  # avoid duplicate inserts
            instance = data_center1 = DataCenter(name="London DC", location="London", capacity=500, created_at=date(2021, 3, 10), updated_at=date(2021, 11, 2))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(505293319238583145)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5832073059693575877 in succeeded_hashes:  # avoid duplicate inserts
            instance = backup_schedule1 = BackupSchedule(server_id=1, schedule_time=date(2021, 3, 15), frequency="Weekly", last_backup=date(2021, 11, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5832073059693575877)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8368986030178069356 in succeeded_hashes:  # avoid duplicate inserts
            instance = configuration_item1 = ConfigurationItem(name="Firewall", ci_type="Security", operational_status="Operational", owner="Security Team", created_at=date(2021, 9, 1), deleted_at=None)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8368986030178069356)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5010689233352522825 in succeeded_hashes:  # avoid duplicate inserts
            instance = vendor1 = Vendor(name="Amazon AWS", contact_email="aws_support@amazon.com", phone_number="+18005551234", updated_at=date(2021, 8, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5010689233352522825)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
