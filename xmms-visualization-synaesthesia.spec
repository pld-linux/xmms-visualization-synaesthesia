Summary:	Synaesthesia for xmms
Summary(pl):	Synaesthesia dla xmms
Name:		xmms-visualization-synaesthesia
Version:	0.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://staff.xmms.org/zinx/xmms/synaesthesia-xmms-%{version}-rc3.tar.gz
URL:		http://staff.xmms.org/zinx/xmms/
Requires:	xmms
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Synaesthesia port for xmms.

%description -l pl
Port Synaesthesii dla xmms.

%prep
%setup -q -n synaesthesia-xmms-%{version}-rc3

%build
rm -f missing                                                                   
libtoolize --copy --force                                                       
aclocal                                                                         
autoconf                                                                        
automake -a -c
%configure 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/*/*.so
