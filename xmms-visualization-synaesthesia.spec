Summary:	Synaesthesia for xmms
Summary(pl):	Synaesthesia dla xmms
Name:		xmms-visualization-synaesthesia
Version:	0.0.3
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://staff.xmms.org/zinx/xmms/synaesthesia-xmms-%{version}-rc3.tar.gz
URL:		http://staff.xmms.org/zinx/xmms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Synaesthesia port for xmms.

%description -l pl
Port Synaesthesii dla xmms.

%prep
%setup -q -n synaesthesia-xmms-%{version}-rc3

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
