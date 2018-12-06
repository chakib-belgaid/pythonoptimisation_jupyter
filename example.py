import pymongo
from sys import argv

client = pymongo.MongoClient('172.16.45.8', 27017)
db = client.testo

if __name__=='__main__' : 
    target = argv[1]
    begin=argv[2]
    warmup = argv[3]
    execution = argv[4]
    end = argv[5]
    db.testcases.insert_one({'name':target,'warmup':warmup,'execution':execution,'begin':begin,'end':end})



