%define debug_package %{nil}

Name:           prometheus
Version:        1.4.1
Release:        1%{?dist}
Summary:        Prometheus metrics system

License:        Apache 2.0
URL:            https://github.com/prometheus/prometheus
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git
Requires:       glibc

%description
Prometheus metrics systemd.

%prep
%setup -q -n src/github.com/prometheus/prometheus
%setup -n src/github.com/prometheus/prometheus -T -D -a 1


%build
GOPATH=%{_builddir} make LDFLAGS+=--build-id


%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D promtool $RPM_BUILD_ROOT/usr/bin/promtool
install -m755 -D prometheus $RPM_BUILD_ROOT/usr/bin/prometheus
install -m644 -D misc/prometheus.yml $RPM_BUILD_ROOT/etc/prometheus/prometheus.yml
install -m644 -D misc/prometheus.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/prometheus
install -m644 -D misc/prometheus.service $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus.service
mkdir -p $RPM_BUILD_ROOT/usr/{share,lib}/prometheus
cp -av consoles $RPM_BUILD_ROOT/usr/share/prometheus/
cp -av console_libraries $RPM_BUILD_ROOT/usr/lib/prometheus/


%files
/usr/bin/prometheus
/usr/bin/promtool
/usr/lib/systemd/system/prometheus.service
%config /etc/sysconfig/prometheus
%config /etc/prometheus/prometheus.yml
%doc LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc NOTICE
%doc README.md
%doc VERSION
%dir /usr/lib/prometheus/console_libraries
%dir /usr/share/prometheus/consoles
/usr/lib/prometheus/console_libraries/menu.lib
/usr/lib/prometheus/console_libraries/prom.lib
/usr/share/prometheus/consoles/aws_elasticache.html
/usr/share/prometheus/consoles/aws_elb.html
/usr/share/prometheus/consoles/aws_redshift-cluster.html
/usr/share/prometheus/consoles/aws_redshift.html
/usr/share/prometheus/consoles/blackbox.html
/usr/share/prometheus/consoles/cassandra.html
/usr/share/prometheus/consoles/cloudwatch.html
/usr/share/prometheus/consoles/haproxy-backend.html
/usr/share/prometheus/consoles/haproxy-backends.html
/usr/share/prometheus/consoles/haproxy-frontend.html
/usr/share/prometheus/consoles/haproxy-frontends.html
/usr/share/prometheus/consoles/haproxy.html
/usr/share/prometheus/consoles/index.html.example
/usr/share/prometheus/consoles/node-cpu.html
/usr/share/prometheus/consoles/node-disk.html
/usr/share/prometheus/consoles/node-overview.html
/usr/share/prometheus/consoles/node.html
/usr/share/prometheus/consoles/prometheus-overview.html
/usr/share/prometheus/consoles/prometheus.html
/usr/share/prometheus/consoles/snmp-overview.html
/usr/share/prometheus/consoles/snmp.html

%changelog
* Sun Sep 25 2016 Joshua Hoffman <joshua@joshua.net> - 1.1.3-1
- Initial build

