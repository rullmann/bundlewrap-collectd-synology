pkg_dnf = {
    'collectd-snmp': {
        'needs': [
            'pkg_dnf:collectd',
        ],
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
}

files = {
    '/etc/collectd.d/synology.conf': {
        'source': 'synology.conf',
        'mode': '0600',
        'content_type': 'mako',
        'needs': [
            'pkg_dnf:collectd-snmp',
        ],
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-DISK-MIB.txt': {
        'source': 'mibs/SYNOLOGY-DISK-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-ISCSILUN-MIB.txt': {
        'source': 'mibs/SYNOLOGY-ISCSILUN-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-RAID-MIB.txt': {
        'source': 'mibs/SYNOLOGY-RAID-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SERVICES-MIB.txt': {
        'source': 'mibs/SYNOLOGY-SERVICES-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SMART-MIB.txt': {
        'source': 'mibs/SYNOLOGY-SMART-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SPACEIO-MIB.txt': {
        'source': 'mibs/SYNOLOGY-SPACEIO-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-STORAGEIO-MIB.txt': {
        'source': 'mibs/SYNOLOGY-STORAGEIO-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-SYSTEM-MIB.txt': {
        'source': 'mibs/SYNOLOGY-SYSTEM-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
    '/usr/share/snmp/mibs/SYNOLOGY-UPS-MIB.txt': {
        'source': 'mibs/SYNOLOGY-UPS-MIB.txt',
        'mode': '0644',
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    },
}
