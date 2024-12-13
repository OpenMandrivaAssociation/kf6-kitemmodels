%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version}|cut -d. -f1-2)

%define libname %mklibname KF6ItemModels
%define devname %mklibname KF6ItemModels -d
#define git 20240217

Name: kf6-kitemmodels
Version: 6.9.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kitemmodels/-/archive/master/kitemmodels-master.tar.bz2#/kitemmodels-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kitemmodels-%{version}.tar.xz
%endif
Summary: Set of item models extending the Qt model-view framework
URL: https://invent.kde.org/frameworks/kitemmodels
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6QuickWidgets)
Requires: %{libname} = %{EVRD}

%description
Set of item models extending the Qt model-view framework

%package -n %{libname}
Summary: Set of item models extending the Qt model-view framework
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Set of item models extending the Qt model-view framework

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Set of item models extending the Qt model-view framework

%prep
%autosetup -p1 -n kitemmodels-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kitemmodels.*

%files -n %{devname}
%{_includedir}/KF6/KItemModels
%{_libdir}/cmake/KF6ItemModels
%{_libdir}/qt6/doc/KF6ItemModels.*

%files -n %{libname}
%{_libdir}/libKF6ItemModels.so*
%{_libdir}/qt6/qml/org/kde/kitemmodels
