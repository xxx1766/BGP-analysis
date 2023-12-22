import pybgpstream
import networkx as nx
from collections import defaultdict
from itertools import groupby
import matplotlib.pyplot as plt


# Create an instance of a simple undirected graph
#as_graph = nx.Graph()
as_graph = nx.DiGraph()
# f = open("2021-08-01-1.txt","w")
# f = open("2019-06-25-1min.txt","w")
# f = open("2018-04-25-1min.txt","w")
f = open("2017-08-26-1min.txt","w")
bgp_lens = defaultdict(lambda: defaultdict(lambda: None))

stream = pybgpstream.BGPStream(
    # Consider this time interval:
    # Sat, 01 Aug 2015 7:50:00 GMT -  08:10:00 GMT
    # from_time="2021-08-01 07:59:00", until_time="2021-08-01 08:00:00",
    # 2017-8-25 12:50
    # from_time="2017-08-25 07:59:00", until_time="2017-08-25 08:00:00",
    # from_time="2019-06-25 07:59:00", until_time="2019-06-25 08:00:00",
    # from_time="2018-04-25 07:59:00", until_time="2018-04-25 08:00:00",
    from_time="2017-08-26 08:00:00", until_time="2017-08-26 08:01:00",
    collectors=["rrc00","rrc01"],
    record_type="ribs",
    #record_type="updates",
)
stream.set_data_interface_option("broker", "cache-dir", "cache")

for rec in stream.records():
    for elem in rec:
        # Get the peer ASn
        peer = str(elem.peer_asn)
        # Get the array of ASns in the AS path and remove repeatedly prepended ASns
        hops = [k for k, g in groupby(elem.fields['as-path'].split(" "))]
        if len(hops) > 1 and hops[0] == peer:
            # Get the origin ASn
            origin = hops[-1]
            # Add new edges to the NetworkX graph
            for i in range(0,len(hops)-1):
                as_graph.add_edge(hops[i+1],hops[i])
                f.write(str(hops[i+1])+','+str(hops[i])+'\n')
            # Update the AS path length between 'peer' and 'origin'
            bgp_lens[peer][origin] = \
                min(list(filter(bool,[bgp_lens[peer][origin],len(hops)])))

# For each 'peer' and 'origin' pair
#for peer in bgp_lens:
#    for origin in bgp_lens[peer]:
 #       # compute the shortest path in the NetworkX graph
#        nxlen = len(nx.shortest_path(as_graph, peer, origin))
#        # and compare it to the BGP hop length
#        print((peer, origin, bgp_lens[peer][origin], nxlen))
#
# 绘制图形
#nx.draw(as_graph, with_labels=False, arrows=True)

# 显示图形
#plt.show()
