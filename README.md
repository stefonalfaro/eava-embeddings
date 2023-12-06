# About
This is a Docker image for HuggingFace embedding models exposed with a Python HTTP API 

## Docker
docker run -p 5000:5000 your-app-name python app.py custom-model-name

## Example Request
POST http://127.0.0.1:5000/embed
{
    "sentences": [
        "This is an example sentence", 
        "Each sentence is converted"
        ]
}