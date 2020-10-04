#
# Conditional build:
%bcond_without	lxc		# LXC support
%bcond_without	qemu		# Qemu support
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module

# qemu available only on x86 and ppc
%ifnarch %{ix86} %{x8664} x32 ppc
%undefine	with_qemu
%endif

%define		origname	libvirt-python
Summary:	Python 2.x bindings to interact with virtualization capabilities
Summary(pl.UTF-8):	Wiązania Pythona 2.x do współpracy z funkcjami wirtualizacji
Name:		python-libvirt
# keep 5.x here for python2 support
Version:	5.10.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	https://libvirt.org/sources/python/%{origname}-%{version}.tar.gz
# Source0-md5:	045c8b45a1aed0725d874ce072027570
URL:		https://libvirt.org/
BuildRequires:	libvirt-devel >= 5.10.0
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildConflicts:	python-PyXML < 0.8.4-13
Requires:	libvirt >= 5.10.0
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
Requires:	libvirt >= 5.10.0

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
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
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
%endif

%if %{with python3}
%files -n python3-libvirt
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{py3_sitedir}/libvirtmod.*.so
%{py3_sitedir}/libvirt.py
%{py3_sitedir}/__pycache__/libvirt.*.py[co]
%{py3_sitedir}/libvirtaio.py
%{py3_sitedir}/__pycache__/libvirtaio.*.py[co]
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
