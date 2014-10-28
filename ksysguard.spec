%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: ksysguard
Version: 5.1.0.1
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 System Guard application
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5SysGuard)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Plasma 5 System Guard application

%prep
%setup -qn %{name}-%{plasmaver}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang ksysguard

%files -f ksysguard.lang
%config %{_sysconfdir}/ksysguarddrc
%{_sysconfdir}/xdg/ksysguard.knsrc
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_libdir}/libkdeinit5_ksysguard.so
%{_datadir}/applications/ksysguard.desktop
%doc %{_docdir}/HTML/en/ksysguard
%{_datadir}/icons/*/*/*/*
%{_datadir}/knotifications5/ksysguard.notifyrc
%{_datadir}/ksysguard
%{_datadir}/kxmlgui5/ksysguard/ksysguardui.rc
