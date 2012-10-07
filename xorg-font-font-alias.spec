Summary:	X font alias databases
Summary(pl.UTF-8):	Baza aliasów fontów X
Name:		xorg-font-font-alias
Version:	1.0.3
Release:	2
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-alias-%{version}.tar.bz2
# Source0-md5:	6d25f64796fef34b53b439c2e9efa562
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X font alias databases.

%description -l pl.UTF-8
Baza aliasów fontów X.

%prep
%setup -q -n font-alias-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-fontrootdir=%{_fontsdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for d in 100dpi 75dpi cyrillic misc ; do
	mv $RPM_BUILD_ROOT%{_fontsdir}/$d/fonts.alias $RPM_BUILD_ROOT%{_fontsdir}/$d/fonts.alias.xorg
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 100dpi
fontpostinst 75dpi
fontpostinst cyrillic
fontpostinst misc

%postun
fontpostinst 100dpi
fontpostinst 75dpi
fontpostinst cyrillic
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/100dpi/fonts.alias.xorg
%{_fontsdir}/75dpi/fonts.alias.xorg
%{_fontsdir}/cyrillic/fonts.alias.xorg
%{_fontsdir}/misc/fonts.alias.xorg
