Summary: Linux kernel header for nxp-sdk
Name: linux-libc-headers-nxp-sdk-dev
Version: 6.12
Release: r0
License: GPL-2.0-only
Group: devel
URL: https://www.kernel.org/
Provides: linux-libc-headers-dev = %{version}-%{release}
Provides: linux-libc-headers-dev(aarch-64) = %{version}-%{release}

Source: @@KERNEL_SOURCE_ARCHIVE@@.tar.xz

%description
Linux kernel header for nxp-sdk

%prep
%setup -q -n @@KERNEL_SOURCE_ARCHIVE@@

%build

%install
rm -rf ${RPM_BUILD_ROOT}
make headers_install ARCH=arm64 INSTALL_HDR_PATH=${RPM_BUILD_ROOT}/usr

%files
%defattr(0644,root,root,0755)
/usr/include/*

