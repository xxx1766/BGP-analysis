# BGP-analysis
计网实验BPG分析
## BGP
BGP，全称边界网关协议（Border Gateway Protocol），是一种用来在路由选择域之间交换网络层可达性信息的路由选择协议。BGP是一种实现自治系统AS（Autonomous System）之间的路由可达，并选择最佳路由的距离矢量路由协议。
BGP有两种运行方式，当BGP运行于同一AS内部时，被称为IBGP（Internel BGP，内部边界网关协议）；当BGP运行于不同AS之间时，称为EBGP（Externel BGP，外部边界网关协议）。
BGP通过维护IP路由表或“前缀”表来实现自治系统（AS）之间的可达性，属于矢量路由协议。BGP主要用于与其他BGP线路建立网络连接、相互交换包括AS在内的信息。
BGP报文有5种消息类型：Open消息、Update消息、Keepalive消息、Notification消息和Route-Refresh消息。BGP有限状态机共有六种状态，分别是Idle、Connect、Active、OpenSent、OpenConfirm和Established。
## 实验要求
编写脚本程序处理上述数据，使用RIB和UPDATE中的AS_PATH属性构建任意时刻互联网AS级别拓扑，分析如下内容：
对比分析中国与美国的AS拓扑差别（选取任一时刻即可）
对比分析IPv4与IPv6网络的AS拓扑差别（选取任一时刻即可）
从AS拓扑上分析近两年来IPv6的部署情况（选取几个时刻即可）
BGP中存在BGP路由泄漏（BGP Route Leak，参考RFC 7908）的问题。
近年来有过多次因为BGP路由泄漏导致网络瘫痪的事件，例如2017
年由于Google工程师配置错误导致的BGP路由泄漏引起了日本发生大
规模网络故障。请从互联网上寻找三个BGP路由泄漏案例，在数据
集中分析BGP泄漏发生前、发生中、发生后，受影响AS的BGP RIB或
者受影响网络的AS拓扑的变化
• 提交：分析代码 & 分析报告

## ref
https://bgpstream.caida.org/docs/tutorials/pybgpstream
https://github.com/CAIDA/pybgpstream/tree/master/examples
