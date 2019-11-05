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

import sqlite3
import logging

SQL_SCHEMA = """
CREATE TABLE kvdb (
keyid text PRIMARY KEY,
content text NOT NULL,
datatype integer NOT NULL,
expire integer)"""

class KVdb:
    def __init__(self, db_loc = ':memory:'):
        try:
            self.conn = sqlite3.connect(db_loc)
            self.cur = self.conn.cursor()
        except sqlite3.Error:
            logging.critical("Failed to open database.")
            self.cleanup()
            return

        self.cur.execute(SQL_SCHEMA)

    def insert(self, keyid, text, dtype, expire):
        try:
            self.cur.executemany("""
            INSERT into kvdb values(?, ?, ?, ?)""", [(keyid, text, dtype, expire)])
            return True
        except sqlite3.IntegrityError:
            return False

    def get(self, keyid):
        val = self.cur.execute("""
                SELECT content FROM kvdb WHERE keyid=?""", 
                (keyid,)).fetchone()
        if val:
            return val[0]
        else:
            return False

    def cleanup(self):
        self.conn.close()