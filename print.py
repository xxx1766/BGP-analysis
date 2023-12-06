#!/usr/bin/env python

import pybgpstream
stream = pybgpstream.BGPStream(
    from_time="2017-07-07 00:00:00", until_time="2017-07-07 00:00:30 UTC",
    collectors=["route-views.sg", "route-views.eqix"],
    record_type="updates"
    #filter="peer 11666 and prefix more 210.180.0.0/16"
)
stream.set_data_interface_option("broker", "cache-dir", "cache")

for elem in stream:
    # record fields can be accessed directly from elem
    # e.g. elem.time
    # or via elem.record
    # e.g. elem.record.time
    # print(elem.time)
    print()
    print(elem)
    #print(elem.project, elem.router, elem.collector, elem.peer_address)
    #print(elem.peer_address, elem.peer_asn, elem.fields)
    print(elem.peer_address)
    print(elem.peer_asn)
    print(elem.fields)
