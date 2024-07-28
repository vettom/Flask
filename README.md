<a href="https://vettom.github.io/"><img src="https://vettom.github.io/img/vettom-banner.jpg" alt="vettom.github.io" ></a>
# Flask App
 Simple flask app to run in Docker container. 

# Build Docker image
```bash
# Test the app
 python test_app.py
 docker build -t sample-flask:v1 .
 docker push <user>/sample-flask:v1
```


# Generate requirement.txt
```bash
python -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
deactivate
```
