from netifaces import interfaces, ifaddresses, AF_INET

def my_local_ip():
    for ifacename in interfaces():
        addresse = [i['addr'] for i in ifaddresses(ifacename).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    ip4 = (', '.join(addresse))
    return ip4

def local_ip_splited():

    ip4 = my_local_ip()

    ip4 = ip4.split('.')

    ip_splited = ''

    for i in range(3):
        ip_splited += ip4[i]
        ip_splited += '.'
    return ip_splited
