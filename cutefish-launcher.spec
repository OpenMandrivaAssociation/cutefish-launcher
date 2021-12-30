%define oname launcher

Name:           cutefish-launcher
Version:        0.7
Release:        1
Summary:        Menu Launcher
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cutefishos/launcher
Source:         https://github.com/cutefishos/launcher/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)

Requires:       fishui

%description
Cutefish Launcher - CutefishOS's full-screen application launcher.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
