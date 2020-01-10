Name:		tmon
Version:	0.9
Release:	4%{?dist}
Summary:	Thermal monitoring utility	
Group:		System Environment/Base
License:	GPLv2
URL:		https://kernel.org

BuildRequires: ncurses-devel

Requires: ncurses

# The source for this package was pullled from upstreams vcs.  Specifically it
# was pulled from the projects github site using the following dynamic tarball
# generating url:
# https://github.com/jrfastab/cgdcbxd/zipball/v1.0.1
Source0:	%{name}-%{version}.tar.bz2
Source1:	tmon.8

Patch0: tmon-log-secutiry.patch
Patch1: tmon-umask-fix.patch

# The service file was created locally for the fedora project, but will be sent
# upstream shortly

%description
Utility to query the thermal monitoring system of the linux kernel

%prep
%setup -q -n tmon
%patch0 -p4
%patch1 -p4

%build
%{__make} %{_smp_mflags}

%install
export INSTALL_ROOT=%{buildroot}
make install
mkdir -p %{buildroot}%{_datadir}/man/man8
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/man/man8/

%files
%{_bindir}/tmon
%{_datadir}/man/man8/*

%changelog
* Thu Aug 07 2014 Neil Horman <nhorman@redhat.com> - 0.9-4
- Added tmon man page (bz 1127904)

* Fri Jun 20 2014 Neil Horman <nhorman@redhat.com> - 0.9-3
- Fixed some security issues (bz 1110489)

* Fri Jun 06 2014 Neil Horman <nhorman@redhat.com> - 0.9-2
- Fixed a missing dependency

* Mon Apr 14 2014 Neil Horman <nhorman@redhat.com> - 0.9-1
- Initial build
