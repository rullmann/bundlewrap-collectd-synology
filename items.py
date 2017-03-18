pkg_dnf = {
    'collectd-snmp': {
        'needs': [
            "pkg_dnf:collectd",
        ],
    },
}

files = {
    '/etc/collectd.d/synology.conf': {
        'source': "synology.conf",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:collectd-snmp",
        ],
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-DISK-MIB.txt': {
        'source': "mibs/SYNOLOGY-DISK-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-ISCSILUN-MIB.txt': {
        'source': "mibs/SYNOLOGY-ISCSILUN-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-RAID-MIB.txt': {
        'source': "mibs/SYNOLOGY-RAID-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SERVICES-MIB.txt': {
        'source': "mibs/SYNOLOGY-SERVICES-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SMART-MIB.txt': {
        'source': "mibs/SYNOLOGY-SMART-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SPACEIO-MIB.txt': {
        'source': "mibs/SYNOLOGY-SPACEIO-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-STORAGEIO-MIB.txt': {
        'source': "mibs/SYNOLOGY-STORAGEIO-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SYSTEM-MIB.txt': {
        'source': "mibs/SYNOLOGY-SYSTEM-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-UPS-MIB.txt': {
        'source': "mibs/SYNOLOGY-UPS-MIB.txt",
        'owner': "root",
        'group': "root",
        'mode': "0644",
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    },
}