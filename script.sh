#!/bin/bash
echo $(date) && sudo rm $HOME/data/data.csv && echo "Data data.csv berhasil dihapus"
echo $(date) && curl -X DELETE http://52.139.171.12:5000/api/delete
echo $(date) && wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/1WmJEoyHQb6Q4EOfM2jxVUtezitlpvL9WZ-0iD3qEFLA/export?format=csv&gid=267379021" -O "$HOME/data/data.csv" && echo "Data data.csv berhasil didownload"
echo $(date) && curl -X POST http://52.139.171.12:5000/api/loaddata
echo " "