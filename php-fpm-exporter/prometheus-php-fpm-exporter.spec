%define debug_package %{nil}

Name:           prometheus-php-fpm-exporter
Version:        0.3.0
Release:        1%{?dist}
Summary:        Prometheus php-fpm exporter

License:        Apache 2.0
URL:            https://github.com/bakins/php-fpm-exporter
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git

%description
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS,
DNS, TCP and ICMP.

%prep
%setup -q -n src/github.com/bakins/php-fpm-exporter
%setup -n src/github.com/bakins/php-fpm-exporter -T -D -a 1

%build
GOPATH=%{_builddir} ./script/build

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D php-fpm-exporter.linux.amd64 $RPM_BUILD_ROOT/usr/bin/php-fpm-exporter
install -m644 -D misc/php-fpm-exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/php-fpm-exporter.service
install -m644 -D misc/php-fpm-exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/php-fpm-exporter


%files
/usr/bin/php-fpm-exporter
/usr/lib/systemd/system/php-fpm-exporter.service
%config /etc/sysconfig/php-fpm-exporter


%changelog
* Wed Aug 16 2017 George Visniuc <george@usabilla.com> - 0.3.0-1
- Initial commit

