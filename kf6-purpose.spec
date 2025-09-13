#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.18
%define		qtver		5.15.2
%define		kfname		purpose

Summary:	Offers available actions for a specific purpose
Name:		kf6-%{kfname}
Version:	6.18.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	a66f3f9ba573fc81cc604d42f6ef94ee
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	ka6-kaccounts-integration-devel
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kio-devel >= %{version}
BuildRequires:	kf6-kirigami-devel >= %{version}
BuildRequires:	libaccounts-glib-devel
BuildRequires:	libaccounts-qt6-devel
BuildRequires:	libsignon-qt6-devel >= 8.55
BuildRequires:	libutempter-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
%requires_eq_to Qt6Core Qt6Core-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This framework offers the possibility to create integrate services and
actions on any application without having to implement them
specifically. Purpose will offer them mechanisms to list the different
alternatives to execute given the requested action type and will
facilitate components so that all the plugins can receive all the
information they need.

%package twitter
Summary:	Twitter plugin for purpose
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kf5-%{kfname}-twitter < %{version}

%description twitter
Twitter plugin for purpose.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF6Purpose.so.6
%attr(755,root,root) %{_libdir}/libKF6Purpose.so.*.*
%ghost %{_libdir}/libKF6PurposeWidgets.so.6
%attr(755,root,root) %{_libdir}/libKF6PurposeWidgets.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/sharefileitemaction.so
%dir %{_libdir}/qt6/plugins/kf6/purpose
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/barcodeplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/bluetoothplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/clipboardplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/emailplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/imgurplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/kdeconnectplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/kdeconnectsmsplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/pastebinplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/phabricatorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/reviewboardplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/saveasplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/telegramplugin.so
%{_libdir}/qt6/qml/org/kde/purpose/AlternativesView.qml
%{_libdir}/qt6/qml/org/kde/purpose/JobView.qml
%{_libdir}/qt6/qml/org/kde/purpose/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/purpose/libpurposequickplugin.so
%dir %{_libdir}/qt6/qml/org/kde/purpose/phabricator
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/purpose/phabricator/libphabricatorquickplugin.so
%dir %{_libdir}/qt6/qml/org/kde/purpose
%{_libdir}/qt6/qml/org/kde/purpose/phabricator/qmldir
%{_libdir}/qt6/qml/org/kde/purpose/purposequickplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/purpose/qmldir
%dir %{_libdir}/qt6/qml/org/kde/purpose/reviewboard
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/purpose/reviewboard/librbpurposequickplugin.so
%{_libdir}/qt6/qml/org/kde/purpose/reviewboard/qmldir
%{_prefix}/libexec/kf6/purposeprocess
%{_iconsdir}/hicolor/128x128/apps/phabricator-purpose6.png
%{_iconsdir}/hicolor/128x128/apps/reviewboard-purpose6.png
%{_iconsdir}/hicolor/16x16/apps/phabricator-purpose6.png
%{_iconsdir}/hicolor/16x16/apps/reviewboard-purpose6.png
%dir %{_datadir}/kf6/purpose
%{_datadir}/kf6/purpose/barcodeplugin_config.qml
%{_datadir}/kf6/purpose/bluetoothplugin_config.qml
%{_datadir}/kf6/purpose/kdeconnectplugin_config.qml
%{_datadir}/kf6/purpose/phabricatorplugin_config.qml
%{_datadir}/kf6/purpose/reviewboardplugin_config.qml
%{_datadir}/kf6/purpose/saveasplugin_config.qml
%{_datadir}/qlogging-categories6/purpose.categories
%{_datadir}/qlogging-categories6/purpose.renamecategories

%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/nextcloudplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/purpose/youtubeplugin.so
%{_datadir}/accounts/services/kde/google-youtube.service
%{_datadir}/accounts/services/kde/nextcloud-upload.service
%{_datadir}/kf6/purpose/nextcloudplugin_config.qml
%{_datadir}/kf6/purpose/youtubeplugin_config.qml

%dir %{_libdir}/qt6/qml/org/kde/purpose/kdeconnect
%{_libdir}/qt6/qml/org/kde/purpose/kdeconnect/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/purpose/kdeconnect/kdeconnectQml.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/purpose/kdeconnect/libkdeconnectQml.so
%{_libdir}/qt6/qml/org/kde/purpose/kdeconnect/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/Purpose
%{_includedir}/KF6/PurposeWidgets
%{_libdir}/cmake/KF6Purpose
%{_libdir}/libKF6Purpose.so
%{_libdir}/libKF6PurposeWidgets.so
