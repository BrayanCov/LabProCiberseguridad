#!/usr/bin/env bash
user=$1
function respuesta(){
  echo "https://api.github.com/users/$user"
  curl "https://api.github.com/users/$user"
  echo  "-------------------------------------------------"
  echo "https://api.github.com/users/$user/repos"
  curl "https://api.github.com/users/$user/repos"
  echo  "-------------------------------------------------"
  echo "https://www.passwordrandom.com/query?command=ip"
  curl --GET "https://www.passwordrandom.com/query?command=ip"
  echo ""
}
respuesta