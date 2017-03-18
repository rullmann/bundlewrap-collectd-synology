# collectd-synology

This bundle retrieves data from Synology NAS with SNMP.

MIB files are described by Synology in the [MIB Guide](https://global.download.synology.com/download/Document/MIBGuide/Synology_DiskStation_MIB_Guide.pdf).
The actual [MIB files](http://dedl.synology.com/download/Document/MIBGuide/Synology_MIB_File.zip) are managed by this bundle and can be found within `files/mibs`.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedora 25   | `[x]` |
| Fedberry 24 | `[x]` |

## Requirements

* Bundles:
  * [collectd](https://github.com/rullmann/bundlewrap-collectd)

## Metadata

    'metadata': {
        'bundle': {
			...
            ... # optional
        },
    }
