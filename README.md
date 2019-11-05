# aiokvdb

Simple python async Key-Value database with aiohttp and sqlite. 

## Usage

You need aiohttp and at least python 3.6 to run aiokvdb.

    git clone https://github.com/moonsikpark/aiokvdb.git
    cd aiokvdb
    pip install -r requirements.txt
    python -m aiohttp.web -H <host> -P <port> server:init_func

## Syntax

    [root@test ~]#curl localhost:8000/api/insert/hello/world/
    201 Created
    [root@test ~]#curl localhost:8000/api/get/hello/
    world

## Warning

Under development.