%define git 20140803

Name: lxqt-config-randr
Version: 0.8.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Patch0: lxqt-config-randr-20140803-no-qt4.patch
Summary: RandR config module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt-qt5)
BuildRequires: qt5-devel
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: pkgconfig(xrandr)
BuildRequires: desktop-file-utils

%description
RandR config module for LXQt.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q -c %{name}-%{version}
%endif
%apply_patches
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

for desktop in %{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop; do
        desktop-file-edit --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done


%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
