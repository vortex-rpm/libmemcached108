Name:      libmemcached108
Summary:   Client library and command line tools for memcached server
Version:   1.0.8
Release:   1.vortex%{?dist}
License:   BSD
Group:     System Environment/Libraries
URL:       http://libmemcached.org/libMemcached.html
Conflicts: libmemcached
BuildRequires: libevent-devel

Source0: libmemcached-%{version}.tar.gz

# checked during configure (for test suite)
#BuildRequires: memcached108

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
libmemcached is a C client library to the memcached server
(http://danga.com/memcached). It has been designed to be light on memory
usage, and provide full access to server side methods.

It also implements several command line tools:

memcat - Copy the value of a key to standard output.
memflush - Flush the contents of your servers.
memrm - Remove a key(s) from the server.
memstat - Dump the stats of your servers to standard output.
memslap - Generate testing loads on a memcached cluster.
memcp - Copy files to memcached servers.
memerror - Creates human readable messages from libmemcached error codes.


%package devel
Summary: Header files and development libraries for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Conflicts: libmemcached-devel

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.


%prep
%setup -q -n libmemcached-%{version}


%build
%configure
%{__make} %{_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""


%check
# For documentation only:
# test suite cannot run in mock (same port use for memcache servers on all arch)
# All tests completed successfully
# diff output.res output.cmp fails but result depend on server version
#%{__make} test


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig
 

%files
%defattr (-,root,root,-) 
%doc AUTHORS COPYING README THANKS TODO ChangeLog
%{_bindir}/mem*
%exclude %{_libdir}/libmemcached.a
%exclude %{_libdir}/libmemcached.la
%exclude %{_libdir}/libmemcachedutil.a
%exclude %{_libdir}/libmemcachedutil.la
%exclude %{_libdir}/libmemcachedprotocol.a
%exclude %{_libdir}/libmemcachedprotocol.la
%exclude %{_libdir}/libhashkit.a
%exclude %{_libdir}/libhashkit.la
%{_libdir}/libmemcached.so.*
%{_libdir}/libmemcachedutil.so.*
%{_libdir}/libmemcachedprotocol.so*
%{_libdir}/libhashkit.so*
%{_mandir}/man1/mem*
%{_mandir}/man3/mem*
%{_mandir}/man3/*hash*


%files devel
%defattr (-,root,root,-) 
%{_includedir}/libmemcached
%{_includedir}/libhashkit
%{_includedir}/libhashkit-1.0
%{_includedir}/libmemcached-1.0
%{_includedir}/libmemcachedprotocol-0.0
%{_includedir}/libmemcachedutil-1.0
%{_libdir}/libmemcached.so
%{_libdir}/libmemcachedutil.so
%{_libdir}/pkgconfig/libmemcached.pc
%{_libdir}/libmemcached.so
%{_mandir}/man3/libmemcached*.3.gz
%{_mandir}/man3/memcached_*.3.gz


%changelog
* Mon Jun 18 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.0.8-1.vortex
- Initial release. Based on Fedora version.
