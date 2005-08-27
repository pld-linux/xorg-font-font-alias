# $Rev: 3194 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-alias
Summary(pl):	font-alias
Name:		xorg-font-font-alias
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-alias-%{version}.tar.bz2
# Source0-md5:	31344a6fad2a6ec4c8ab995231d5a746
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-alias-%{version}-root-%(id -u -n)

%description
font-alias

%description -l pl
font-alias


%prep
%setup -q -n font-alias-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/100dpi/fonts.alias
%{_libdir}/X11/fonts/75dpi/fonts.alias
%{_libdir}/X11/fonts/cyrillic/fonts.alias
%{_libdir}/X11/fonts/misc/fonts.alias
