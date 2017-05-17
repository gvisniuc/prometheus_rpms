%define debug_package %{nil}

Name:           prometheus-blackbox_exporter
Version:        0.5.0
Release:        1%{?dist}
Summary:        Prometheus blackbox probe exporter

License:        Apache 2.0
URL:            https://github.com/prometheus/node_exporter
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git
Requires:       glibc

%description
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS,
DNS, TCP and ICMP.

%prep
%setup -q -n src/github.com/prometheus/blackbox_exporter
%setup -n src/github.com/prometheus/blackbox_exporter -T -D -a 1


%build
GOPATH=%{_builddir} make LDFLAGS+=--build-id


%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D blackbox_exporter $RPM_BUILD_ROOT/usr/bin/blackbox_exporter
install -m644 -D misc/blackbox_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/blackbox_exporter.service
install -m644 -D misc/blackbox_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/blackbox_exporter
install -m644 -D blackbox.yml $RPM_BUILD_ROOT/etc/prometheus/exporters/blackbox.yml


%files
/usr/bin/blackbox_exporter
/usr/lib/systemd/system/blackbox_exporter.service
%config /etc/sysconfig/blackbox_exporter
%config /etc/prometheus/exporters/blackbox.yml
%doc LICENSE
%doc NOTICE
%doc README.md
%doc VERSION

%changelog
* Sun Sep 25 2016 Joshua Hoffman <joshua@joshua.net> - 0.2.0-1
- Initial commit

