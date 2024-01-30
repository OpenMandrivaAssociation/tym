%global debug_package %{nil}

Name: tym
Version: 3.5.0
Release: 1
Group:   Applications/System
License: MIT
Summary: Lua-configurable terminal emulator base on VTE
URL: https://github.com/endaaman/tym
Source0:https://github.com/endaaman/tym/archive/%{name}-%{version}.tar.gz

BuildRequires: (pkgconfig(lua) >= 5.4 with pkgconfig(lua) < 5.5)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: vte3-devel

%description
tym is a Lua-configurable terminal emulator base on VTE

%prep
%autosetup -n %{name}-%{version}
libtoolize --force ; aclocal ; autoheader ; automake -a ; autoconf

%build
# libdir is WRONG, but it's used only to install a systemd
# unit file, which doesn't belong in lib64
%configure --libdir=%{_prefix}/lib

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/tym
%{_userunitdir}/tym-daemon.service
%{_datadir}/applications/tym-daemon.desktop
%{_datadir}/applications/tym.desktop
%{_mandir}/man1/tym.1*
