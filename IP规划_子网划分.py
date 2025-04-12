import ipaddress

def list_subnets(network_str, subnet_mask):
    # 将输入的网段转换为 IPv4Network 对象
    network = ipaddress.ip_network(network_str, strict=False)
    
    # 遍历网络中的所有子网
    for subnet in network.subnets(new_prefix=subnet_mask):
        # 打印子网的网络地址和广播地址
        print(f"Subnet: {subnet}")
        print(f"   Network Address: {subnet.network_address}")
        # 打印子网中的网络主机
        for i, ip in enumerate(subnet.hosts(), start=1):#ip in enumerate(subnet.hosts()) 来遍历 subnet.hosts() 返回的迭代器，并同时获取每个主机地址的索引（i）和主机地址（ip）。enumerate() 函数会为每个元素提供一个计数（从0开始
            print(f"   Host {i}: {ip}")
        print(f"   Broadcast Address: {subnet.broadcast_address}")
        print("-" * 40)

# 输入网段
network_str = "21.144.189.0/24"
subnet_mask = 30

list_subnets(network_str, subnet_mask)