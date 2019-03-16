 #!/usr/bin/python
import csv
from elasticsearch import Elasticsearch
from datetime import datetime
import decimal
import sys

usbank_file = sys.argv[1]
with open(usbank_file, 'rb') as f:
    reader = csv.reader(f)
    headers = next(reader, None)
    es = Elasticsearch()
    print('Loading transactions into elastic search')
    for row in reader:
        timestamp = datetime.strptime(row[0], '%m/%d/%Y')
        transaction_type = row[1]
        description = row[2]
        memo = row[3]
        amount = decimal.Decimal(row[4]).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP).copy_abs()
        body = {"timestamp":timestamp, "type":transaction_type, "description":description, "memo":memo, "amount":amount}
        print body
        es.index(index="wendy",doc_type="transaction",body=body)
    print 'Done loading transactions'
