FROM nginx:latest
ADD app.py /apps/
ADD *.html /usr/share/nginx/html/
EXPOSE 80