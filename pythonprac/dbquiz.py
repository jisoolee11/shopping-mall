from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# # quiz1
# movie = db.movies.find_one({'title':'매트릭스'})
# # print(movie['star'])
# target_star = movie['star']
#
# # quiz2
# target_movies = list(db.movies.find({'star':target_star},{'_id':False}))
#
# for target in target_movies:
#     print(target['title'])

# quiz3
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})