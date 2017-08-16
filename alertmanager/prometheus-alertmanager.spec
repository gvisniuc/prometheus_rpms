%define debug_package %{nil}

Name:           prometheus-alertmanager
Version:        0.8.0
Release:        1%{?dist}
Summary:        Prometheus alertmanager

License:        Apache 2.0
URL:            https://github.com/prometheus/alertmanager
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-misc.tar.gz

BuildRequires:  golang
BuildRequires:  git

%description
The Alertmanager handles alerts sent by client applications such as the Prometheus server.
It takes care of deduplicating, grouping, and routing them to the correct receiver integrations such as email, PagerDuty, or OpsGenie.
It also takes care of silencing and inhibition of alerts.

%prep
%setup -q -n src/github.com/prometheus/alertmanager
%setup -n src/github.com/prometheus/alertmanager -T -D -a 1


%build
GOPATH=%{_builddir} make LDFLAGS+=--build-id

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D alertmanager $RPM_BUILD_ROOT/usr/bin/alertmanager
install -m644 -D misc/alertmanager.yml $RPM_BUILD_ROOT/etc/prometheus/alertmanager.yml
install -m644 -D misc/alertmanager.service $RPM_BUILD_ROOT/usr/lib/systemd/system/alertmanager.service
install -m644 -D misc/alertmanager.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/alertmanager

%files
/usr/bin/alertmanager
/usr/lib/systemd/system/alertmanager.service
%config /etc/sysconfig/alertmanager
%config /etc/prometheus/alertmanager.yml
%doc LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc NOTICE
%doc README.md
%doc VERSION

%changelog
* Wed Aug 16 2017 George Visniuc <george@usabilla.com> - 0.8.0-1
- Initial commit

