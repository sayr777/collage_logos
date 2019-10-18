from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"openstreetmap+logo,  nominatim+logo,  JOSM+logo,  MAPS.ME +logo,  carto+db+logo,  прогород+cdcom+logo,  osrm+logo,  overpass+api+logo,  qgis+logo,  postgis+logo,  MongoDB+logo,  MongoChef+logo,  GDAL+logo,  PyMongo+logo,  RabbitMQ+logo,  MQTT+logo,  Postgresql+logo,  Redis+logo,  REST API+logo,  Docker+logo,  Rancher+logo,  JSON+logo,  GEOJSON+logo,  Google+Protobuf+logo,  ЕГТС+ERA+GLONASS+logo,  git+logo,  github+logo,  atlassian+jira+logo,  power+bi+logo,  atlassian+jira+service+desk+logo,  atlassian+confluence+logo,  javascript+logo,  tableau+logo,  linux+logo,  ubuntu+logo,  corel+draw+logo,  adobe+photoshop+logo,  red+hat +logo,  neo4j+logo,  cypher+logo,  solidworks+logo,  autocad+logo,  prometheus.io+logo,  grafana+logo","limit":5,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images