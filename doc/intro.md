## Problem
My wife is self-employed and every year we have to spend time looking through some of her expenses and decide which
can be considered business expenses.  This information is used when we file taxes.

The first part of this process is downloading transactions in a .csv format and loading that into Elasticsearch. The
format for the data in the csv file looks like the following:

| Date | Transaction | Name | Memo |  Amount
| 3/6/2018 | DEBIT | Kroger | 24445008067000429017102; 05411; | -31.7600

The goal is the read the data from the .csv and insert the data into an Elasticsearch index into the following
structure:

```
{
  "timestamp": "3/7/2018",
  "type": "DEBIT",
  "description": "Kroger",
  "memo": "24445008067000429017102; 05411;",
  "amount": 31.76
}
```

Even though I load transactions of both types ('DEBIT' or 'CREDIT'), I typically ignore `CREDIT` transactions when
I explore the data in Elasticsearch.