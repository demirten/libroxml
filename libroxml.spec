%define name blunderer
%define version 1.3
%define release 1

Summary: a light and powerfull xml parsing library
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://code.google.com/p/libroxml/source/checkout
Vendor: blunderer
URL:  http://code.google.com/p/libroxml/
License: LGPL
Group: System Environment/Libraries
Prefix: %{_prefix}

%description
libroxml is a very light, low fingerprint, fast, and powerfull
library designed for parsing XML files. This is perfectly suitable
for little embeded systems but you also use it widely in various
application for xml configuration file reading for example.

%package devel
Summary: development file for libroxml
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS debian/changelog COPYING INSTALL NEWS README TODO
%{_prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS debian/changelog COPYING INSTALL NEWS README TODO
%{_prefix}/bin/*
%{_prefix}/lib/lib*.so
%{_prefix}/include/*
%{_prefix}/lib/pkgconfig/*

