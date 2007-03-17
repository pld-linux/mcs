# TODO:
# - pl description and summary
# - build GConf and Kconfig backends (?)
#
Summary:	mcs - simple, abstractable configuration library
Name:		mcs
Version:	0.4.1
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://sacredspiral.co.uk/~nenolod/mcs/%{name}-%{version}.tgz
# Source0-md5:	d09b42e9d51ea32c6326f0bbcad86c9e
URL:		http://sacredspiral.co.uk/~nenolod/mcs/
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications. It is hoped
that by using mcs, that the applications which use it will generally
have a more congruent feeling in regards to settings. There have been
other projects like this before (such as GConf), but unlike those
projects, mcs strictly handles abstraction. It doesn't impose any
specific data storage requirement, nor is it tied to any desktop
environment or software suite.

%package libs
Summary:	mcs library
Summary(pl.UTF-8):	Biblioteka mcs
Group:		Libraries

%description libs
mcs library.

%description libs -l pl.UTF-8
Biblioteka mcs.

%package devel
Summary:	Header files for mcs
Summary(pl.UTF-8):	Pliki nagłówkowe mcs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for mcs.

%description devel -l pl.UTF-8
Pliki nagłówkowe mcs.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}-getconfval
%attr(755,root,root) %{_bindir}/%{name}-info
%attr(755,root,root) %{_bindir}/%{name}-query-backends
%attr(755,root,root) %{_bindir}/%{name}-setconfval

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmcs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmcs.so.[0-9]
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libkeyfile.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmcs.so
%{_includedir}/libmcs
%{_pkgconfigdir}/libmcs.pc
