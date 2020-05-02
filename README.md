# Money keeper chatbot

## Description

The Telegram chatbot for watching for your money amount.

Link to the chatbot: <a href="t.me/money_amount_keeper_bot">Money Keeper</a>.

## Functionality

#### Main functions
- user auth
- set amount limit for food spending
- set amount limit for things (non-expensive staff) spending
- increase bank amount
- increase cash amount
- decrease the food money amount value by input value, informing about the rest.
- decrease the things money amount value by input value, informing about the rest.
- decrease bank amount
- decrease cash amount
- each month update amounts for spend

#### Additional functions that can be in future

- mail notification
- different currencies

## How to run

1. Rename `configs/db.py.example` to `configs/db.py` and set necessary configs there
2. Create network:
```bash
docker network create money_keeper
```
3. Run DB:
```bash
docker run \
    --name money_keeper-mongo \
    -h money_keeper-mongo \
    -e MONGO_INITDB_ROOT_USERNAME=<db username> \
    -e MONGO_INITDB_ROOT_PASSWORD=<db password> \
    --network money_keeper \
    -d mongo
```
4. Run server:
```
docker build . -t money_keeper-python && \
    docker run \
    -h money_keeper-python \
    --name money_keeper-python \
    --network money_keeper \
    -d money_keeper-python
