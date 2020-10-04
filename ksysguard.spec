%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: ksysguard
Version: 5.19.90
Release: 2
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
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libnl-3.0)
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
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)

%description
KDE Plasma 5 System Guard application.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang ksysguard --all-name || touch ksysguard.lang

%files -f ksysguard.lang
%config %{_sysconfdir}/ksysguarddrc
%{_datadir}/knsrcfiles/ksysguard.knsrc
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_libdir}/libkdeinit5_ksysguard.so
%{_libdir}/libksgrdbackend.so
%{_datadir}/applications/org.kde.ksysguard.desktop
%doc %{_docdir}/HTML/*/ksysguard
%{_datadir}/dbus-1/services/org.kde.ksystemstats.service
%{_datadir}/icons/*/*/*/*
%{_datadir}/knotifications5/ksysguard.notifyrc
%{_datadir}/ksysguard
%{_datadir}/kxmlgui5/ksysguard/ksysguardui.rc
%{_datadir}/metainfo/org.kde.ksysguard.appdata.xml
%{_libdir}/libexec/ksysguard/ksgrd_network_helper
%{_libdir}/qt5/plugins/ksysguard
%{_bindir}/ksystemstats
%{_bindir}/kstatsviewer
