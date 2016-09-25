%define debug_package %{nil}

Name:           prometheus-node_exporter
Version:        0.12.0
Release:        3%{?dist}
Summary:        Prometheus exporter for machine metrics

License:        Apache 2.0
URL:            https://github.com/prometheus/node_exporter
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git
Requires:       glibc

%description
Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
%setup -q -n src/github.com/prometheus/node_exporter
%setup -n src/github.com/prometheus/node_exporter -T -D -a 1


%build
GOPATH=%{_builddir} make LDFLAGS+=--build-id


%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D node_exporter $RPM_BUILD_ROOT/usr/bin/node_exporter
install -m644 -D misc/node_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/node_exporter.service
install -m644 -D misc/node_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/node_exporter


%files
/usr/bin/node_exporter
/usr/lib/systemd/system/node_exporter.service
%config /etc/sysconfig/node_exporter
%doc LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc NOTICE
%doc README.md
%doc VERSION

%changelog
* Sun Sep 25 2016 Joshua Hoffman <joshua@joshua.net> - 0.12.0-3
- Added sysconfig style configuration


* Sun Sep 25 2016 Joshua Hoffman <joshua@joshua.net> - 0.12.0-2
- Initial build

