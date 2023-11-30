# Activate the virtual enviroment venv: 
    source documentation-env/bin/activate

# Run the server with: 
    uvicorn main:app --reload
    uvicorn blog.main:app --reload

# FastAPI guidance:
    https://www.youtube.com/watch?v=7t2alSnE2-I&t=1032s

# Create a venv (virtual enviroment):
    python -m venv <venv-name>

# Check the local Git link repository:
    git remote -v

# Delete the local Git link repository:
    git remote rm origin

# Open the project in the browser
    localhost:8000
    localhost:8000/docs