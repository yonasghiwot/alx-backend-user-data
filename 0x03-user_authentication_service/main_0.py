#!/usr/bin/env python3
"""
Main file for task 0
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
