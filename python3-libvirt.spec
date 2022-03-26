#
# Conditional build:
%bcond_without	lxc		# LXC support
%bcond_without	qemu		# Qemu support

# qemu available only on x86 and ppc
%ifnarch %{ix86} %{x8664} x32 ppc
%undefine	with_qemu
%endif

%define		origname	libvirt-python
Summary:	Python 3.x bindings to interact with virtualization capabilities
Summary(pl.UTF-8):	Wiązania Pythona 3.x do współpracy z funkcjami wirtualizacji
Name:		python3-libvirt
Version:	6.6.0
Release:	5
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	https://libvirt.org/sources/python/%{origname}-%{version}.tar.gz
# Source0-md5:	f153718d1d47c2e101b2e152e75fabd3
URL:		https://libvirt.org/
BuildRequires:	libvirt-devel >= 6.6.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildConflicts:	python-PyXML < 0.8.4-13
Requires:	libvirt >= 6.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvirt is a C toolkit to interact with the virtualization
capabilities of recent versions of Linux.

This package contains the Python 3.x bindings for the libvirt library.

%description -l pl.UTF-8
Libvirt to zestaw narzędzi w C do współpracy z funkcjami wirtualizacji
obecnych wersji Linuksa.

Ten pakiet zawiera wiązania Pythona 3.x do biblioteki libvirt.

%prep
%setup -q -n %{origname}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py3_sitedir}/libvirtmod.cpython-*.so
%{py3_sitedir}/libvirt.py
%{py3_sitedir}/__pycache__/libvirt.cpython-*.py[co]
%{py3_sitedir}/libvirtaio.py
%{py3_sitedir}/__pycache__/libvirtaio.cpython-*.py[co]
%if %{with lxc}
%attr(755,root,root) %{py3_sitedir}/libvirtmod_lxc.cpython-*.so
%{py3_sitedir}/libvirt_lxc.py
%{py3_sitedir}/__pycache__/libvirt_lxc.cpython-*.py[co]
%endif
%if %{with qemu}
%attr(755,root,root) %{py3_sitedir}/libvirtmod_qemu.cpython-*.so
%{py3_sitedir}/libvirt_qemu.py
%{py3_sitedir}/__pycache__/libvirt_qemu.cpython-*.py[co]
%endif
%{py3_sitedir}/libvirt_python-%{version}-py*.egg-info
