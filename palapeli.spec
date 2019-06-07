#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : palapeli
Version  : 19.04.2
Release  : 10
URL      : https://download.kde.org/stable/applications/19.04.2/src/palapeli-19.04.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.2/src/palapeli-19.04.2.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.2/src/palapeli-19.04.2.tar.xz.sig
Summary  : A single-player jigsaw puzzle game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: palapeli-bin = %{version}-%{release}
Requires: palapeli-data = %{version}-%{release}
Requires: palapeli-lib = %{version}-%{release}
Requires: palapeli-license = %{version}-%{release}
Requires: palapeli-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
The Goldberg Slicer: Versatile grid generator for the KDE puzzle game Palapeli
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

%package bin
Summary: bin components for the palapeli package.
Group: Binaries
Requires: palapeli-data = %{version}-%{release}
Requires: palapeli-license = %{version}-%{release}

%description bin
bin components for the palapeli package.


%package data
Summary: data components for the palapeli package.
Group: Data

%description data
data components for the palapeli package.


%package dev
Summary: dev components for the palapeli package.
Group: Development
Requires: palapeli-lib = %{version}-%{release}
Requires: palapeli-bin = %{version}-%{release}
Requires: palapeli-data = %{version}-%{release}
Provides: palapeli-devel = %{version}-%{release}
Requires: palapeli = %{version}-%{release}
Requires: palapeli = %{version}-%{release}

%description dev
dev components for the palapeli package.


%package doc
Summary: doc components for the palapeli package.
Group: Documentation

%description doc
doc components for the palapeli package.


%package lib
Summary: lib components for the palapeli package.
Group: Libraries
Requires: palapeli-data = %{version}-%{release}
Requires: palapeli-license = %{version}-%{release}

%description lib
lib components for the palapeli package.


%package license
Summary: license components for the palapeli package.
Group: Default

%description license
license components for the palapeli package.


%package locales
Summary: locales components for the palapeli package.
Group: Default

%description locales
locales components for the palapeli package.


%prep
%setup -q -n palapeli-19.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559904293
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1559904293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/palapeli
cp COPYING %{buildroot}/usr/share/package-licenses/palapeli/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/palapeli/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/palapeli/COPYING.LIB
cp src/pics/LICENSE %{buildroot}/usr/share/package-licenses/palapeli/src_pics_LICENSE
pushd clr-build
%make_install
popd
%find_lang palapeli

%files
%defattr(-,root,root,-)
/usr/lib64/libpala/libpala-config.cmake
/usr/lib64/libpala/pala-targets-relwithdebinfo.cmake
/usr/lib64/libpala/pala-targets.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/palapeli

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.palapeli.desktop
/usr/share/icons/hicolor/128x128/apps/palapeli.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-palapeli.png
/usr/share/icons/hicolor/16x16/apps/palapeli.png
/usr/share/icons/hicolor/16x16/mimetypes/application-x-palapeli.png
/usr/share/icons/hicolor/24x24/apps/palapeli.png
/usr/share/icons/hicolor/24x24/mimetypes/application-x-palapeli.png
/usr/share/icons/hicolor/32x32/apps/palapeli.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-palapeli.png
/usr/share/icons/hicolor/48x48/apps/palapeli.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-palapeli.png
/usr/share/icons/hicolor/64x64/apps/palapeli.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-palapeli.png
/usr/share/knotifications5/palapeli.notifyrc
/usr/share/kservices5/ServiceMenus/palapeli_servicemenu.desktop
/usr/share/kservices5/palapeli_goldbergslicer.desktop
/usr/share/kservices5/palapeli_jigsawslicer.desktop
/usr/share/kservices5/palapeli_rectslicer.desktop
/usr/share/kservices5/palathumbcreator.desktop
/usr/share/kservicetypes5/libpala-slicerplugin.desktop
/usr/share/kxmlgui5/palapeli/palapeliui.rc
/usr/share/metainfo/org.kde.palapeli.appdata.xml
/usr/share/mime-packages/palapeli-mimetypes.xml
/usr/share/palapeli/backgrounds/Eliminator-Funk-2.jpg
/usr/share/palapeli/backgrounds/Rear-Admiral-Diplomat-1.jpg
/usr/share/palapeli/backgrounds/Time-For-Lunch-2.jpg
/usr/share/palapeli/backgrounds/background.svg
/usr/share/palapeli/backgrounds/gon-defends-the-critters-1.jpg
/usr/share/palapeli/backgrounds/mahogany-handjob-1.jpg
/usr/share/palapeli/collection/castle-maintenon.desktop
/usr/share/palapeli/collection/castle-maintenon.jpg
/usr/share/palapeli/collection/cincinnati-bridge.desktop
/usr/share/palapeli/collection/cincinnati-bridge.jpg
/usr/share/palapeli/collection/citrus-fruits.desktop
/usr/share/palapeli/collection/citrus-fruits.jpg
/usr/share/palapeli/collection/european-honey-bee.desktop
/usr/share/palapeli/collection/european-honey-bee.jpg
/usr/share/palapeli/collection/panther-chameleon-female.desktop
/usr/share/palapeli/collection/panther-chameleon-female.jpg
/usr/share/palapeli/palapeli.kcfg
/usr/share/xdg/palapeli-collectionrc
/usr/share/xdg/palapeli.categories

%files dev
%defattr(-,root,root,-)
/usr/include/Pala/Slicer
/usr/include/Pala/SlicerJob
/usr/include/Pala/SlicerMode
/usr/include/Pala/SlicerProperty
/usr/include/Pala/SlicerPropertySet
/usr/include/libpala/libpala_export.h
/usr/include/libpala/slicer.h
/usr/include/libpala/slicerjob.h
/usr/include/libpala/slicermode.h
/usr/include/libpala/slicerproperty.h
/usr/include/libpala/slicerpropertyset.h
/usr/lib64/libpala.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/palapeli/index.cache.bz2
/usr/share/doc/HTML/de/palapeli/index.docbook
/usr/share/doc/HTML/en/palapeli/index.cache.bz2
/usr/share/doc/HTML/en/palapeli/index.docbook
/usr/share/doc/HTML/en/palapeli/puzzletable1.png
/usr/share/doc/HTML/es/palapeli/index.cache.bz2
/usr/share/doc/HTML/es/palapeli/index.docbook
/usr/share/doc/HTML/et/palapeli/index.cache.bz2
/usr/share/doc/HTML/et/palapeli/index.docbook
/usr/share/doc/HTML/fr/palapeli/index.cache.bz2
/usr/share/doc/HTML/fr/palapeli/index.docbook
/usr/share/doc/HTML/fr/palapeli/puzzletable1.png
/usr/share/doc/HTML/it/palapeli/index.cache.bz2
/usr/share/doc/HTML/it/palapeli/index.docbook
/usr/share/doc/HTML/nl/palapeli/index.cache.bz2
/usr/share/doc/HTML/nl/palapeli/index.docbook
/usr/share/doc/HTML/pt/palapeli/index.cache.bz2
/usr/share/doc/HTML/pt/palapeli/index.docbook
/usr/share/doc/HTML/pt_BR/palapeli/index.cache.bz2
/usr/share/doc/HTML/pt_BR/palapeli/index.docbook
/usr/share/doc/HTML/ru/palapeli/index.cache.bz2
/usr/share/doc/HTML/ru/palapeli/index.docbook
/usr/share/doc/HTML/sv/palapeli/index.cache.bz2
/usr/share/doc/HTML/sv/palapeli/index.docbook
/usr/share/doc/HTML/uk/palapeli/index.cache.bz2
/usr/share/doc/HTML/uk/palapeli/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpala.so.0
/usr/lib64/libpala.so.0.2.0
/usr/lib64/qt5/plugins/palapeli_goldbergslicer.so
/usr/lib64/qt5/plugins/palapeli_jigsawslicer.so
/usr/lib64/qt5/plugins/palapeli_rectslicer.so
/usr/lib64/qt5/plugins/palathumbcreator.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/palapeli/COPYING
/usr/share/package-licenses/palapeli/COPYING.DOC
/usr/share/package-licenses/palapeli/COPYING.LIB
/usr/share/package-licenses/palapeli/src_pics_LICENSE

%files locales -f palapeli.lang
%defattr(-,root,root,-)

