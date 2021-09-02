#Take the official nginx image
FROM nginx

#Remove the default nginx.conf file 
RUN rm /etc/nginx/conf.d/default.conf

#Replace it with our own configuration file

COPY nginx.conf /etc/nginx/conf.d/