Summary:	Configuration file parser library
Summary(pl.UTF-8):	Biblioteka analizująca pliki konfiguracyjne
Name:		dotconf
Version:	1.3
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://github.com/williamh/dotconf/tarball/v%{version}?/%{name}-%{version}.tar.gz
# Source0-md5:	36bfdde245072fc2f4f5766b7db97c45
URL:		http://www.azzit.de/dotconf/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.2
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
%setup -q -n williamh-dotconf-4cd7b3a

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

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_docdir}/dotconf/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/dotconf/dotconf*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libdotconf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdotconf.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/dotconf*.txt
%attr(755,root,root) %{_libdir}/libdotconf.so
%{_libdir}/libdotconf.la
%{_includedir}/dotconf.h
%{_pkgconfigdir}/dotconf.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libdotconf.a
