import os
from rethinkdb import RethinkDB

maxAge = int(os.getenv("MAX_AGE_MILLIS"))
r = RethinkDB()
r.connect(os.getenv("HOST"), int(os.getenv("PORT"))).repl()
print(r.db("stf").table("logs").filter(r.js("(function (item) { return item.timestamp > Date.now() - %d;})"%(maxAge))).delete(durability="soft").run())
