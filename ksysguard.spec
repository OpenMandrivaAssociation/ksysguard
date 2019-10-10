%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: ksysguard
Version: 5.17.0
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 System Guard application
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(libpcap)
BuildRequires: lm_sensors-devel
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5SysGuard)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5KDELibs4Support)

%description
KDE Plasma 5 System Guard application.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksysguard || touch ksysguard.lang

%files -f ksysguard.lang
%config %{_sysconfdir}/ksysguarddrc
%{_datadir}/knsrcfiles/ksysguard.knsrc
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_libdir}/libkdeinit5_ksysguard.so
%{_datadir}/applications/org.kde.ksysguard.desktop
%doc %{_docdir}/HTML/*/ksysguard
%{_datadir}/icons/*/*/*/*
%{_datadir}/knotifications5/ksysguard.notifyrc
%{_datadir}/ksysguard
%{_datadir}/kxmlgui5/ksysguard/ksysguardui.rc
%{_datadir}/metainfo/org.kde.ksysguard.appdata.xml
%{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_libdir}/qt5/plugins/ksysguard
