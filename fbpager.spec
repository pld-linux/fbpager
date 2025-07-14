Summary:	a pager application for the Fluxbox window manager
Name:		fbpager
Version:	0.1.4
Release:	1
License:	MIT
Group:		X11/Window Managers/Tools
# Source0:	http://fluxbox.org/download/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.man.szczecin.pl/pub/FreeBSD/ports/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	89aac82e217ef366634dfd768b1b5dff
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-namespace.patch
URL:		http://fluxbox.sourceforge.net/fbpager/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbpager is a pager for Fluxbox with support of the following features:

  - mouse gestures with button binding
  - great number of configuration items
  - alpha channel transparency
  - ability to reside in the slit

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
