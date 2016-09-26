# vim:noexpandtab:nosmarttab:ts=8 sw=8

NAME := prometheus-blackbox_exporter
VERSION := 0.2.0
RELEASE := 1.el7.centos

GIT_HASH := 242bf8b
GIT_URL := https://github.com/prometheus/blackbox_exporter
SPECFILE := $(NAME).spec
RPM_TOPDIR := rpmdev
MOCK_CFG := mock-centos-7-x86_64.cfg
RPMBUILD := rpmbuild
CURL := curl
GIT := git
MOCK := /usr/bin/mock


$(NAME)-$(VERSION)-$(RELEASE).x86_64.rpm : $(NAME)-$(VERSION)-$(RELEASE).src.rpm $(MOCK_CFG)
	$(MOCK) -r $(MOCK_CFG) --rebuild $(NAME)-$(VERSION)-$(RELEASE).src.rpm
	mv /var/lib/mock/centos-7-x86_64/result/$@ .

$(NAME)-$(VERSION)-$(RELEASE).src.rpm : $(NAME)-$(VERSION).tar.gz $(NAME)-misc.tar.gz $(SPECFILE)
	rm -rf $(RPM_TOPDIR)
	mkdir -p $(RPM_TOPDIR)/{RPMS,SRPMS,SOURCES,SPECS}
	cp $(NAME)-$(VERSION).tar.gz $(RPM_TOPDIR)/SOURCES/
	cp $(NAME)-misc.tar.gz $(RPM_TOPDIR)/SOURCES/
	$(RPMBUILD) -D '_topdir $(abspath $(RPM_TOPDIR))' -bs $(SPECFILE)
	mv $(RPM_TOPDIR)/SRPMS/$@ .

$(NAME)-misc.tar.gz : misc/*
	tar czvf $@ misc

$(NAME)-$(VERSION).tar.gz :
	rm -rf src
	$(GIT) clone $(GIT_URL)
	cd blackbox_exporter && $(GIT) checkout $(GIT_HASH)
	mkdir -p src/github.com/prometheus
	mv blackbox_exporter src/github.com/prometheus/blackbox_exporter
	tar cvzf $@ src

.PHONY : clean
clean :
	rm -rf src
	rm -rf $(RPM_TOPDIR)
	rm -f $(NAME)-*.tar.gz
	rm -f *.rpm
