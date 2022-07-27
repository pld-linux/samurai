Summary:	ninja-compatible build tool written in C
Name:		samurai
Version:	1.2
Release:	1
License:	Apache v2.0
Group:		Development/Tools
Source0:	https://github.com/michaelforney/samurai/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9991b88c2e7c4789222b0b46ec7d8940
URL:		https://github.com/michaelforney/samurai
#Provides:	ninja = 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ninja-compatible build tool written in C.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/samu
%{_mandir}/man1/samu.1*
