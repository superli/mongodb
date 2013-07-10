from pymongo import Connection #导入模块
con = Connection()
db = con.test #连接test数据库
posts = db.post #连接test中的post集合，相当于MySQL中的表
import time
post1 = {"title":"I Love Python",
          "slug":"i-love-python",
          "author":"SErHo",
          "content":"I Love Python....",
          "tags":["Love","Python"],
          "time":time.ctime()}

post2 = {"title":"Python and MongoDB",
         "slug":"python-mongodb",
         "author":"SErHo",
         "content":"Python and MongoDB....",
         "tags":["Python","MongoDB"],
         "time":time.ctime()}
 
post3 = {"title":"SErHo Blog",
         "slug":"serho-blog",
         "author":"Akio",
         "content":"SErHo Blog is OK....",
         "tags":["SErHo","Blog"],
         "time":time.ctime()}

posts.insert(post1)
posts.insert(post2)
posts.insert(post3)
posts = posts.find()
count = posts.count()
for post in posts:
    print post
    
post = posts.find_one({"slug":"python-mongodb"})

post["author"] = "HaHa Lu"
post["title"] = "Test Update"
post["title"] = "Test Update"


posts.update({"_id":post["_id"]},post)

post = posts.find_one({"_id":post["_id"]})
print post
# 只更新一个键，可以使用”$set”这个修改器;
# 指定一个键，如果不存在，就可以创建
posts.update({"_id":post["_id"]},{"$set":{"content":"Test Update SET...."}})
# $inc”修改器可以用来增加已有键的值，如果没有，则创建它
posts.update({"_id":post["_id"]},{"$inc":  {"views":1}})
# 数组的修改器:”$push”，可以在数组末尾添加一个元素
posts.update({"_id":post["_id"]},{"$push":{"tags":"Test"}})
# 避免加入了重复的，可以使用”$addToSet”
# 当需要添加多个值，配合”$each”来使用，可以添加不重复的进去
posts.update({"_id":post["_id"]},{"$addToSet":{"tags":{"$each":["Python","Each"]}}})
# 可以把数组看成栈和队列，使用”$pop”来删除：
# 例如下边代码会删除tags里面最后一个，改成-1则删除第一个
posts.update({"_id":post["_id"]},{"$pop":{"tags":1}})
# 直接定位修改，可以通过下标直接选择,就是tags[0]，然后使用上面的”$set”等修改器，如果不确定可以使用$来定位：
posts.update({"tags":"MongoDB"},{"$set":{"tags.$":"Hello"}})