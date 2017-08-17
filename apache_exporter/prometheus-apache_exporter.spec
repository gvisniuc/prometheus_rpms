%define debug_package %{nil}

Name:           prometheus-apache_exporter
Version:        0.3
Release:        2%{?dist}
Summary:        Prometheus apache exporter

License:        Apache 2.0
URL:            https://github.com/neezgee/apache_exporter
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git

%description
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS,
DNS, TCP and ICMP.

%prep
%setup -q -n src/github.com/neezgee/apache_exporter
%setup -n src/github.com/neezgee/apache_exporter -T -D -a 1


%build
GOPATH=%{_builddir} go get && GOPATH=%{_builddir} env GOOS=linux GOARCH=amd64 go build .

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D apache_exporter $RPM_BUILD_ROOT/usr/bin/apache_exporter
install -m644 -D misc/apache_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/apache_exporter.service
install -m644 -D misc/apache_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/apache_exporter


%files
/usr/bin/apache_exporter
/usr/lib/systemd/system/apache_exporter.service
%config /etc/sysconfig/apache_exporter


%changelog
* Thu Aug 17 2017 George Visniuc <george@usabilla.com> - 0.3-2
- Added scrape uri parameter
* Wed Aug 16 2017 George Visniuc <george@usabilla.com> - 0.3-1
- Initial commit

