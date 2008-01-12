Summary:	Configuration file parser library
Summary(pl.UTF-8):	Biblioteka analizująca pliki konfiguracyjne
Name:		dotconf
Version:	1.0.13
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.azzit.de/dotconf/download/v1.0/%{name}-%{version}.tar.gz
# Source0-md5:	bbf981a5f4a64e94cc6f2a693f96c21a
Patch0:		%{name}-am18.patch
URL:		http://www.azzit.de/dotconf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dot.conf is a simple-to-use and powerful configuration-file parser
library written in C. The configuration files created for dot.conf
look very similar to those used by the Apache Webserver. Even
Container-Directives known from httpd.conf can easily be used in the
exact same manner as for Apache-Modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass
very long ARG_STR data to your app, and on-the-fly inclusion of
additional config files.

%description -l pl.UTF-8
dot.conf to prosta w użyciu i mająca duże możliwości, napisana w C
biblioteka analizująca pliki konfiguracyjne. Pliki tworzone dla
dot.conf wyglądają podobnie do używanych przez serwer WWW Apache.
Nawet dyrektywy kontenerowe znane z httpd.conf mogą być z łatwością
używane w taki sam sposób, jak dla modułów Apache'a. Biblioteka
obsługuje różne typy argumentów, dynamicznie ładowane moduły
tworzące w locie własne opcje konfiguracyjne, tekst wklejany
(here-document) do przekazywania bardzo długich danych ARG_STR do
aplikacji oraz włączanie w locie dodatkowych plików konfiguracyjnych.

%package devel
Summary:	Header files for dot.conf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dot.conf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for dot.conf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dot.conf.

%package static
Summary:	Static dot.conf library
Summary(pl.UTF-8):	Statyczna biblioteka dot.conf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dot.conf library.

%description static -l pl.UTF-8
Statyczna biblioteka dot.conf.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*.txt examples
%attr(755,root,root) %{_libdir}/libdotconf-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdotconf-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dotconf-config
%attr(755,root,root) %{_libdir}/libdotconf.so
%{_libdir}/libdotconf.la
%{_libdir}/libpool.a
%{_includedir}/dotconf.h
%{_includedir}/libpool.h
%{_aclocaldir}/dotconf.m4
%{_pkgconfigdir}/dotconf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdotconf.a
