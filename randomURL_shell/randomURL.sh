#!/bin/ash

wiki_url=$(curl -I https://en.wikipedia.org/wiki/Special:Random | grep location | cut -c 13-)
wiki_url=${wiki_url%?}
command="PGPASSWORD=$DB_PASSWORD psql -U postgres -d todo -c \"INSERT INTO Todos (todo) VALUES ('$wiki_url');\""
kubectl exec -i --namespace=project db-sts-0 -- bash -c "$command"