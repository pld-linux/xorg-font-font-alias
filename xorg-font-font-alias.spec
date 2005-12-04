Summary:	X font alias databases
Summary(pl):	Baza aliasów fontów X
Name:		xorg-font-font-alias
Version:	0.99.0
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-alias-%{version}.tar.bz2
# Source0-md5:	ab102077178a9dbfc90ac091c62ead03
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font alias databases.

%description -l pl
Baza aliasów fontów X.

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
