import os

import dns.resolver
import whois


def resolveDNS(domain, type):
    try:
        domain = domain
        resolver = dns.resolver.Resolver();
        answer = resolver.query(domain, type)
        return answer
    except:
        return ""


def creatDnsZone(domain):
    array: list = ["A", "TXT", "MX", "NS", "AAAA", "cname"]
    zoneDNS: dict = {}
    for i in array:
        answer = ''
        resultDNS = resolveDNS(domain, i)
        resultant_string = ''
        for item in resultDNS:
            resultant_str = ','.join([str(item), answer])

            answer = resultant_str
        zoneDNS[i] = answer
    answer = ''
    resultDNS = resolveDNS("_dmarc." + domain, "TXT")
    resultant_string = ''
    for item in resultDNS:
        resultant_str = ','.join([str(item), answer])
        answer = resultant_str
    zoneDNS["DMARC"] = answer
    return zoneDNS


def whoisDomain(domain):
    w = whois.whois(domain)
    print(whois)
    return w


def ping(ip):
    response = os.system("ping -c 1 " + ip)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False
