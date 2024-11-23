#!/bin/bash

# Create the Chinook DB with init data
sqlite3 -init Chinook_Sqlite.sql Chinook.db .quit