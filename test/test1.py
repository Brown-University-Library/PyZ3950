#!/usr/bin/env python

import logging, os
from PyZ3950 import zoom


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
    filename=os.environ['LOG_PATH'] )
log = logging.getLogger(__name__)
log.debug( 'logging ready' )


conn = zoom.Connection ('z3950.loc.gov', 7090)
log.debug( 'conn type, `{typ}`; conn, ```{val}```'.format( typ=type(conn), val=conn ) )
conn.databaseName = 'VOYAGER'
conn.preferredRecordSyntax = 'USMARC'

query = zoom.Query ('CCL', 'ti="1066 and all that"')
log.debug( 'query type, `{typ}`; query, ```{val}```'.format( typ=type(query), val=query ) )

res = conn.search (query)
log.debug( 'res type, `{typ}`; res, ```{val}```'.format( typ=type(res), val=res ) )

for r in res:
    log.debug( 'r type, `{typ}`; r, ```{val}```'.format( typ=type(r), val=r ) )
    print r
    break
conn.close ()

