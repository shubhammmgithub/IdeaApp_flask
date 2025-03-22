from flask import Flask,request

app = Flask(__name__)

# Create the idea repository. This is where the ideas will be stored.
ideas = {
    1: {
        "id": 1,
        "idea_name": "save earth",
        "idea_description": "compulsory to plant 5 trees by everyone",
        "idea_author": "Shubham",
    },
    2: {
        "id": 2,
        "idea_name": "save soil",
        "idea_description": "Details about saving soil",
        "idea_author": "Mohan",
    },
}

# Create a RESTful endpoint for fetching all the ideas.
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    # I need to read the query param
    idea_author=request.args.get('idea_author')
    
    if idea_author:
        #filter the ideas created by this author 
        idea_res={}
        for key , value in ideas.items():
            if value['idea_author']== idea_author:
                idea_res[key] = value
        return idea_res
        
    #Logic to support all the ideas and support query params
    return ideas



'''
Create a RESTful endpoint for creating a new idea 
'''
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #logic to create a new idea 
    try:
        
        #first read the request body
        request_body=request.get_json() # this represents the request body passed by the user
    
        #check if the idea id passed is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with the same id already present",400 # http status code = 400 (it tells the request is a bad request )
    
        #Insert the passed idea in the ideas dictionary
        ideas[request_body['id']]=request_body#id and request body is put into ideas 
    
    
        # return the response saying idea got saved
        return "dea created and saved successfully",201
    except KeyError:
        return "id is missing ",400
    except:
        return "some internal server error",500
    
    
    '''
    Endpoint to fetch idea based on the idea id
    '''
@app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
        try:
            if int(idea_id) in ideas:
                return ideas[int(idea_id)],200
            
            else:
                return"idea passed in not present ",400
            
        except:
            return "something internal error happened ",500    
        
        
        
        
        
if __name__ == "__main__":
    app.run(port=8080)
