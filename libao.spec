Name:           libao
Version:        1.2.0
Release:        14
Summary:        A cross platform audio library
License:        GPLv2+
URL:            http://xiph.org/ao/
Source0:        http://downloads.xiph.org/releases/ao/libao-%{version}.tar.gz
Patch1:         0001-ao_pulse.c-fix-latency-calculation.patch
Patch2:         d5221655dfd1a2156aa6be83b5aadea7c1e0f5bd.diff
BuildRequires:  gcc alsa-lib-devel pkgconfig(libpulse)

%description
Libao is a cross-platform audio library that allows programs to output audio
using a simple API on a wide variety of platforms.


%package        devel
Summary:        Including header files and library for the developing of libao
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This contains header files and dynamic libraries for the developing applications
that use libao.


%package help
Summary:        Man files for libao
Requires:       man
BuildArch:      noarch

%description help
This contains man files for the using of libao.


%prep
%autosetup -p1
sed -i "s/-O20 -ffast-math//" configure


%build
%configure
%disable_rpath
%make_build


%install
%make_install INSTALL="install -p"
%delete_la
rm -rf %{buildroot}/%{_docdir}/libao*

%ldconfig_scriptlets


%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/ao
%{_libdir}/libao.so.*

%files devel
%doc doc/*.html doc/*.c doc/*.css
%{_datadir}/aclocal/*
%{_includedir}/ao
%{_libdir}/ckport
%{_libdir}/*.so
%{_libdir}/pkgconfig

%files help
%{_mandir}/man*/*


%changelog
* Thu Nov 28 2019 huyan <hu.huyan@huawei.com> - 1.2.0-14
- Package Initialization
