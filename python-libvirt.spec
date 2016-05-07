#
# Conditional build:
%bcond_without	lxc		# LXC support
%bcond_without	qemu		# Qemu support
%bcond_without	python3		# CPython 3.x module

# qemu available only on x86 and ppc
%ifnarch %{ix86} %{x8664} x32 ppc
%undefine	with_qemu
%endif

%define		origname	libvirt-python
Summary:	Python 2.x bindings to interact with virtualization capabilities
Summary(pl.UTF-8):	Wiązania Pythona 2.x do współpracy z funkcjami wirtualizacji
Name:		python-libvirt
Version:	1.2.20
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	ftp://ftp.libvirt.org/libvirt/python/%{origname}-%{version}.tar.gz
# Source0-md5:	2e17b3047c80291874bb96f0a80816db
URL:		http://www.libvirt.org/
BuildRequires:	libvirt-devel >= 1.0.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel >= 1:2.4
%if %{with python3}
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-devel >= 1:3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildConflicts:	python-PyXML < 0.8.4-13
Requires:	libvirt >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvirt is a C toolkit to interact with the virtualization
capabilities of recent versions of Linux.

This package contains the Python 2.x bindings for the libvirt library.

%description -l pl.UTF-8
Libvirt to zestaw narzędzi w C do współpracy z funkcjami wirtualizacji
obecnych wersji Linuksa.

Ten pakiet zawiera wiązania Pythona 2.x do biblioteki libvirt.

%package -n python3-libvirt
Summary:	Python 3.x bindings to interact with virtualization capabilities
Summary(pl.UTF-8):	Wiązania Pythona 3.x do współpracy z funkcjami wirtualizacji
Group:		Development/Languages/Python
Requires:	libvirt >= 1.0.2

%description -n python3-libvirt
Libvirt is a C toolkit to interact with the virtualization
capabilities of recent versions of Linux.

This package contains the Python 3.x bindings for the libvirt library.

%description -n python3-libvirt -l pl.UTF-8
Libvirt to zestaw narzędzi w C do współpracy z funkcjami wirtualizacji
obecnych wersji Linuksa.

Ten pakiet zawiera wiązania Pythona 3.x do biblioteki libvirt.

%prep
%setup -q -n %{origname}-%{version}

%build
%py_build

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{py_sitedir}/libvirtmod.so
%{py_sitedir}/libvirt.py[co]
%if %{with lxc}
%attr(755,root,root) %{py_sitedir}/libvirtmod_lxc.so
%{py_sitedir}/libvirt_lxc.py[co]
%endif
%if %{with qemu}
%attr(755,root,root) %{py_sitedir}/libvirtmod_qemu.so
%{py_sitedir}/libvirt_qemu.py[co]
%endif
%{py_sitedir}/libvirt_python-%{version}-py*.egg-info

%if %{with python3}
%files -n python3-libvirt
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{py3_sitedir}/libvirtmod.*.so
%{py3_sitedir}/libvirt.py
%{py3_sitedir}/__pycache__/libvirt.*.py[co]
%if %{with lxc}
%attr(755,root,root) %{py3_sitedir}/libvirtmod_lxc.*.so
%{py3_sitedir}/libvirt_lxc.py
%{py3_sitedir}/__pycache__/libvirt_lxc.*.py[co]
%endif
%if %{with qemu}
%attr(755,root,root) %{py3_sitedir}/libvirtmod_qemu.*.so
%{py3_sitedir}/libvirt_qemu.py
%{py3_sitedir}/__pycache__/libvirt_qemu.*.py[co]
%endif
%{py3_sitedir}/libvirt_python-%{version}-py*.egg-info
%endif
