# Requête curl pour le déploiement CI

curl --request POST \
     --url "https://api.render.com/v1/services/"${RENDER_SERVICE_ID}"/deploys" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer "${RENDER_API_KEY} \
     --header "Content-Type: application/json" \
     --write-out "%{http_code}\n\n %{url}" \
     --silent \
     --output /dev/null


#- |
#  curl --fail --output "/dev/null" --silent --show-error --write-out "HTTP response: ${http_code}\n\n" \
#    --data "{\"tag_name\": \"${CI_COMMIT_TAG}\", \"name\": \"${CI_PROJECT_NAME} ${CI_COMMIT_TAG}\", \"description\": \"${CI_COMMIT_TAG_MESSAGE:-No release notes.}\"}" \
#    --header "Content-Type: application/json" \
#    --header "Private-Token: ${CI_PRIVATE_TOKEN}" \
#    --request POST \
#    "${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/releases"

