# Prometheus RPMS
Prometheus monitoring systems packaged for Enterprise Linux

These packages are ready to run with systemd unit files and sysconfig
integration.

## Releases
The RPMS from this project are available via a the [Promethean RPM repo](https://packagecloud.io/promethean/prometheus).

## Promethean RPM Repository
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

