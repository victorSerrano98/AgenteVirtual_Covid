#obtener la imagen elastic search docker 
docker pull elasticsearch:7.14.2

#ejecutar imagen
docker run -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.14.2

