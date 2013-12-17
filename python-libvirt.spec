#
# Conditional build:
%bcond_without	lxc		# LXC support
%bcond_without	qemu		# Qemu support

# qemu available only on x86 and ppc
%ifnarch %{ix86} %{x8664} ppc
%undefine	with_qemu
%endif

%define		origname	libvirt-python
Summary:	Python bindings to interact with virtualization capabilities
Summary(pl.UTF-8):	Wiązania Pythona do współpracy z funkcjami wirtualizacji
Name:		python-libvirt
Version:	1.2.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	ftp://ftp.libvirt.org/libvirt/python/%{origname}-%{version}.tar.gz
# Source0-md5:	38158e5740be65f17eef9f99ffa5dadf
URL:		http://www.libvirt.org/
BuildRequires:	libvirt-devel >= 1.0.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 2
BuildRequires:	python-devel >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.627
Requires:	libvirt >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvirt is a C toolkit to interact with the virtualization
capabilities of recent versions of Linux.

This package contains the Python bindings for the libvirt library.

%description -l pl.UTF-8
Libvirt to zestaw narzędzi w C do współpracy z funkcjami wirtualizacji
obecnych wersji Linuksa.

Ten pakiet zawiera wiązania Pythona do biblioteki libvirt.

%prep
%setup -q -n %{origname}-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

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
