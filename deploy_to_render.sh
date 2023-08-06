# Requête curl pour le déploiement CI

curl --request POST \
     --url "https://api.render.com/v1/services/${RENDER_SERVICE_ID}/deploys" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer '${RENDER_API_KEY}'" \
     --header "Content-Type: application/json" \
     --write-out '%{http_code}' \
     --silent \
     --output /dev/null
