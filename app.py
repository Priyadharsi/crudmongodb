from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://127.0.0.1:27017")
@app.route("/",methods=["POST","GET"])
def showall():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.students
    collection=database.data
    result=collection.find()
    l=[]
    for i in result:
        l.append(i)
    client.close()
    return render_template("index.html",data=l)

@app.route("/add",methods=["POST","GET"])
def add():
    client=MongoClient("mongodb://127.0.0.1:27017")
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        title=request.form.get("title")
        author=request.form.get("author")
        database=client.students
        collection=database.data
        collection.insert_one({"id":id,"name":name,"title":title,"author":author})
        print("inserted")
        client.close()
        return redirect(url_for("showall"))
    return render_template("add.html")

@app.route("/update/<id>",methods=["POST","GET"])
def updateall(id):
     client=MongoClient("mongodb://127.0.0.1:27017")
     if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        title=request.form.get("title")
        author=request.form.get("author")
        client=MongoClient("mongodb://127.0.0.1:27017")
        database=client.students
        collection=database.data
        collection.update_many({"id":id},{"$set":{"name":name,"title":title}})
        client.close()
        return redirect(url_for("showall"))

     client=MongoClient("mongodb://127.0.0.1:27017")
     database=client.students
     collection=database.data
     a=collection.find_one({"id":id})
     dic={"id":a.get("id"),"name":a.get("name"),"title":a.get("title"),"author":a.get("author")}
     client.close()
     return render_template("edit.html",data=dic)

@app.route("/delete/<id>",methods=["POST","GET"])
def deleteall(id):
     client=MongoClient("mongodb://127.0.0.1:27017")
     database=client.students
     collection=database.data
     collection.delete_one({"id":id})
     client.close()
     return redirect(url_for("showall"))


if __name__=="__main__":
    app.run(debug=True)