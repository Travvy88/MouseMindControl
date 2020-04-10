import json

data = {"id": 1,"jsonrpc": "2.0",
        "method": "querySessions",
        "params": { "cortexToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS5oc2VzdHVkZW50LmRlYWRpbnNpZ2h0LTIiLCJhcHBWZXJzaW9uIjoiMS4wIiwiZXhwIjoxNTgxNTA1MDkyLCJuYmYiOjE1ODEyNDU4OTIsInV zZXJJZCI6IjhhZjI2ZmQ1LTJmZmItNDhhYi04MmFjLTc4MGIwMWY5NDc4MSIsInVzZXJuYW1lIjoiaHNlc3R1ZGVudCIsInZlcnNpb2 4iOiIyLjAifQ==.fajpYIjuAyOmeA2QPzqhjrnOGNXdO492SkglC6dJeZI="}}
d = json.dumps(data, indent = 4)
print(d)

data = '{"id":1,"jsonrpc":"2.0","result":[]}'
d = json.loads(data)
print(d['id'])