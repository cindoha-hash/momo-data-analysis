#!/bin/bash
python -c "
from etl.load_db import get_connection
import json
from etl.config import DASHBOARD_JSON_PATH

conn = get_connection()
conn.row_factory = None
rows = conn.execute('SELECT * FROM transactions').fetchall()
conn.close()

with open(DASHBOARD_JSON_PATH, 'w') as f:
    json.dump(rows, f, indent=2)

print('Exported dashboard.json')
"
