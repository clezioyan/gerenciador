#!/bin/bash
# Executa o WebGrab+Plus com o arquivo de configuração
webgrabplus --config config.xml

# Faz commit e push do arquivo EPG atualizado para o GitHub
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git add epg.xml
git commit -m "Atualização automática do EPG"
git push origin gh-pages
