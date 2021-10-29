#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-api-core
Version  : 1.31.1
Release  : 14
URL      : https://files.pythonhosted.org/packages/84/10/8e2eef7293e29f223aea3a67186aea0f42bc219ecb415edfffaa798ea804/google-api-core-1.31.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/84/10/8e2eef7293e29f223aea3a67186aea0f42bc219ecb415edfffaa798ea804/google-api-core-1.31.1.tar.gz
Summary  : Google API client core library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-api-core-license = %{version}-%{release}
Requires: google-api-core-python = %{version}-%{release}
Requires: google-api-core-python3 = %{version}-%{release}
Requires: google-auth
Requires: googleapis-common-protos
Requires: grpcio
Requires: packaging
Requires: protobuf
Requires: pytz
Requires: requests
Requires: setuptools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : google-auth
BuildRequires : googleapis-common-protos
BuildRequires : grpcio
BuildRequires : packaging
BuildRequires : protobuf
BuildRequires : pytz
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six

%description
Core Library for Google Client Libraries
========================================

%package license
Summary: license components for the google-api-core package.
Group: Default

%description license
license components for the google-api-core package.


%package python
Summary: python components for the google-api-core package.
Group: Default
Requires: google-api-core-python3 = %{version}-%{release}

%description python
python components for the google-api-core package.


%package python3
Summary: python3 components for the google-api-core package.
Group: Default
Requires: python3-core
Provides: pypi(google_api_core)
Requires: pypi(google_auth)
Requires: pypi(googleapis_common_protos)
Requires: pypi(packaging)
Requires: pypi(protobuf)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(setuptools)
Requires: pypi(six)

%description python3
python3 components for the google-api-core package.


%prep
%setup -q -n google-api-core-1.31.1
cd %{_builddir}/google-api-core-1.31.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627685986
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-api-core
cp %{_builddir}/google-api-core-1.31.1/LICENSE %{buildroot}/usr/share/package-licenses/google-api-core/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-api-core/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
