@metadata_processor
def dnf(metadata):
    if node.has_bundle('dnf'):
        metadata.setdefault('dnf', {})
        metadata['dnf'].setdefault('extra_packages', [])
        for package in ['net-snmp', 'net-snmp-utils']:
            if package not in metadata['dnf']['extra_packages']:
                metadata['dnf']['extra_packages'].append(package)
    return metadata, DONE
