from flask import Flask

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
    return ideas

if __name__ == "__main__":
    app.run(port=8080)
