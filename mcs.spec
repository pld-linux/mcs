# TODO:
# - build GConf backend (?)
#
Summary:	mcs - simple, abstractable configuration library
Summary(pl.UTF-8):	mcs - prosta, abstrakcyjna biblioteka konfiguracji
Name:		mcs
Version:	0.7.0
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://distfiles.atheme.org/lib%{name}-%{version}.tgz
# Source0-md5:	0f0c779609b3481a79937c2e86660a99
URL:		http://www.atheme.org/projects/mcs.shtml
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libmowgli-devel >= 0.4.0
BuildRequires:	qt-devel
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

This package contains userland tools.

%description -l pl.UTF-8
mcs to biblioteka i zbiór narzędzi tworzących abstrakcję
przechowywania ustawień konfiguracyjnych dla aplikacji użytkownika.
Przy użyciu mcs aplikacje mają mieć bardziej zgodne odczucia odnośnie
ustawień. Wcześniej istniały już podobne projekty (jak GConf), ale w
przeciwieństwie do nich mcs ściśle obsługuje abstrakcję. Nie nakłada
żadnych konkretnych wymagań co do przechowywania danych ani nie jest
związana z żadnym środowiskiem graficznym czy pakietem oprogramowania.

Ten pakiet zawiera narzędzia przestrzeni użytkownika.

%package backend-gconf
Summary:	The gconf backend for mcs
Summary(pl.UTF-8):	Backend gconf dla mcs
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Provides:	%{name}-backend = %{version}-%{release}

%description backend-gconf
The gconf backend for mcs. It uses the GConf configuration system to
store configuration and provides integration into the GNOME desktop
environment.

%description backend-gconf -l pl.UTF-8
Backend gconf dla mcs. Używa systemu konfiguracji GConf do
przechowywania konfiguracji i zapewnia intergrację ze środowiskiem
GNOME.

%package backend-kconfig
Summary:	The kconfig backend for mcs
Summary(pl.UTF-8):	Backend kconfig dla mcs
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Provides:	%{name}-backend = %{version}-%{release}

%description backend-kconfig
The kconfig backend for mcs. It uses the KDE configuration system to
store configuration and provides integration into the KDE desktop
environment.

%description backend-kconfig -l pl.UTF-8
Backend kconfig dla mcs. Używa systemu konfiguracji KDE do
przechowywania konfiguracji i zapewnia intergrację ze środowiskiem
KDE.

%package devel
Summary:	Header files for mcs
Summary(pl.UTF-8):	Pliki nagłówkowe mcs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for mcs.

%description devel -l pl.UTF-8
Pliki nagłówkowe mcs.

%package libs
Summary:	mcs library
Summary(pl.UTF-8):	Biblioteka mcs
Group:		Libraries

%description libs
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications. It is hoped
that by using mcs, that the applications which use it will generally
have a more congruent feeling in regards to settings. There have been
other projects like this before (such as GConf), but unlike those
projects, mcs strictly handles abstraction. It doesn't impose any
specific data storage requirement, nor is it tied to any desktop
environment or software suite.

This package contains mcs library.

%description libs -l pl.UTF-8
mcs to biblioteka i zbiór narzędzi tworzących abstrakcję
przechowywania ustawień konfiguracyjnych dla aplikacji użytkownika.
Przy użyciu mcs aplikacje mają mieć bardziej zgodne odczucia odnośnie
ustawień. Wcześniej istniały już podobne projekty (jak GConf), ale w
przeciwieństwie do nich mcs ściśle obsługuje abstrakcję. Nie nakłada
żadnych konkretnych wymagań co do przechowywania danych ani nie jest
związana z żadnym środowiskiem graficznym czy pakietem oprogramowania.

Ten pakiet zawiera bibliotekę mcs.

%prep
%setup -q -n lib%{name}-%{version}

%build
QTDIR=%{_prefix}
CFLAGS="$CFLAGS -I%{_includedir}/qt"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/qt"
export CFLAGS CPPFLAGS QTDIR
%{__aclocal} -I m4
%{__autoconf}
%configure
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
%attr(755,root,root) %{_bindir}/%{name}-walk-config

%files backend-gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/gconf.so

%files backend-kconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/kconfig.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmcs.so
%{_includedir}/libmcs
%{_pkgconfigdir}/libmcs.pc

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmcs.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libmcs.so.?
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/keyfile.so
