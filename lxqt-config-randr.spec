%define git 20140803

Name: lxqt-config-randr
Version: 0.8.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: RandR config module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt-qt5)
BuildRequires: qt5-devel
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)

%description
RandR config module for LXQt

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q -c %{name}-%{version}
%endif
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
