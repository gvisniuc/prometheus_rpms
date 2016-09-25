# Prometheus RPMS
Automated builds of Prometheus and friends for Enterprise Linux

## Releases
The RPMS from this project are available in a [packagecloud repo](https://packagecloud.io/promethean/prometheus):

* [prometheus-1.1.3-1.el7.centos.x86_64.rpm](https://packagecloud.io/promethean/prometheus/packages/el/7/prometheus-1.1.3-1.el7.centos.x86_64.rpm)
* [prometheus-1.1.3-1.el7.centos.src.rpm](https://packagecloud.io/promethean/prometheus/packages/el/7/prometheus-1.1.3-1.el7.centos.src.rpm)
* [prometheus-node_exporter-0.12.0-3.el7.centos.x86_64.rpm](https://packagecloud.io/promethean/prometheus/packages/el/7/prometheus-node_exporter-0.12.0-3.el7.centos.x86_64.rpm)
* [prometheus-node_exporter-0.12.0-3.el7.centos.src.rpm](https://packagecloud.io/promethean/prometheus/packages/el/7/prometheus-node_exporter-0.12.0-3.el7.centos.src.rpm)

## Package Repo
Use the following config for yum to access the repo:

    [promethean]
    name=prometheus metrics system
    baseurl=https://packagecloud.io/promethean/prometheus/el/7/x86_64
    repo_gpgcheck=1
    enabled=1
    gpgkey=https://packagecloud.io/promethean/prometheus/gpgkey
    gpgcheck=0
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300

    [promethean-source]
    name=promethean_prometheus-source
    baseurl=https://packagecloud.io/promethean/prometheus/el/7/SRPMS
    repo_gpgcheck=1
    enabled=0
    gpgkey=https://packagecloud.io/promethean/prometheus/gpgkey
    gpgcheck=0
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300

