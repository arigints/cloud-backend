# cloud-backend

Untuk menjalankan project ini, pastikan `docker` sudah terinstall pada komputer/laptop Anda.

---

Tata cara menjalankan project:

1. Create docker container using docker compose

```
docker compose up -d
```

2. Download csv file from google spreadsheets

```
wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/1WmJEoyHQb6Q4EOfM2jxVUtezitlpvL9WZ-0iD3qEFLA/export?format=csv&gid=267379021" -O "$HOME/data/data.csv"
```

3. Run flask api

```
run.sh
```