from pysnmp.hlapi import *

def walk(host, oid, user, authkey, privkey):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        UsmUserData(user, authkey, privkey, authProtocol=usmHMACSHAAuthProtocol, privProtocol=usmAesCfb128Protocol),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
        lookupMib=False,
        lexicographicMode=False
    ):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break
        else:
            for varBind in varBinds:
                print('%s = %s' % varBind)

# Replace 'your_switch_ip' with the IP address of your switch
# Replace 'start_oid' and 'end_oid' with the range of OIDs you want to scan
# Replace 'user', 'authkey', and 'privkey' with your SNMPv3 credentials
start_oid = '1.3.6.1.2.1.1.1.0'
end_oid = '1.3.6.1.2.1.1.9.1.2'
current_oid = start_oid

while current_oid <= end_oid:
    walk('196.168.40.10', current_oid, 'monitor-1', 'authkey', 'privkey')
    # Increment the OID. This is a simplification; you'll need to implement actual OID incrementing logic here.
    current_oid += '.1'
