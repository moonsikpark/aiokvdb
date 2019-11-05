"""
Copyright (c) 2019, Moonsik Park
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from aiohttp import web
import sqlite3
import logging
import atexit
import kvdb

logging.basicConfig(level=logging.DEBUG)

db = kvdb.KVdb()

routes = web.RouteTableDef()

@routes.get('/')
async def root(request):
    return web.Response(text="aiokvdb running...")

@routes.get('/api/insert/{keyid}/{data}/')
async def insert(request):
    res = db.insert(request.match_info['keyid'], request.match_info['data'], 0, 0)

    if res:
        return web.Response(status=201, text="201 Created")
    else:
        return web.Response(status=406, text="406 Not Acceptable")

@routes.get('/api/get/{keyid}/')
async def insert(request):
    val = db.get(request.match_info['keyid'])
    if val:
        return web.Response(text=f"{val}")
    else:
        return web.Response(status=404, text="404 Not Found")

    
def init_func(argv):
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)