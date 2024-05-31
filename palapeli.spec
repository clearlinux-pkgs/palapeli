#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : palapeli
Version  : 24.05.0
Release  : 70
URL      : https://download.kde.org/stable/release-service/24.05.0/src/palapeli-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/palapeli-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/palapeli-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: palapeli-bin = %{version}-%{release}
Requires: palapeli-data = %{version}-%{release}
Requires: palapeli-lib = %{version}-%{release}
Requires: palapeli-license = %{version}-%{release}
Requires: palapeli-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n palapeli-24.05.0
cd %{_builddir}/palapeli-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716476203
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716476203
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/palapeli
cp %{_builddir}/palapeli-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/palapeli/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/palapeli-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/palapeli/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/palapeli-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/palapeli/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/palapeli-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/palapeli/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/palapeli-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/palapeli/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/palapeli-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/palapeli/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/palapeli-%{version}/src/pics/LICENSE %{buildroot}/usr/share/package-licenses/palapeli/c27070819e7457aece740e2866204327de9c0080 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang palapeli
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/palapeli
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
/usr/share/kio/servicemenus/palapeli_servicemenu.desktop
/usr/share/knotifications6/palapeli.notifyrc
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
/usr/share/qlogging-categories6/palapeli.categories
/usr/share/xdg/palapeli-collectionrc

%files dev
%defattr(-,root,root,-)
/usr/include/Pala/Pala/Slicer
/usr/include/Pala/Pala/SlicerJob
/usr/include/Pala/Pala/SlicerMode
/usr/include/Pala/Pala/SlicerProperty
/usr/include/Pala/Pala/SlicerPropertySet
/usr/include/Pala/pala/libpala_export.h
/usr/include/Pala/pala/slicer.h
/usr/include/Pala/pala/slicerjob.h
/usr/include/Pala/pala/slicermode.h
/usr/include/Pala/pala/slicerproperty.h
/usr/include/Pala/pala/slicerpropertyset.h
/usr/lib64/cmake/Pala/PalaConfig.cmake
/usr/lib64/cmake/Pala/PalaConfigVersion.cmake
/usr/lib64/cmake/Pala/PalaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Pala/PalaTargets.cmake
/usr/lib64/libpala.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/palapeli/index.cache.bz2
/usr/share/doc/HTML/ca/palapeli/index.docbook
/usr/share/doc/HTML/de/palapeli/index.cache.bz2
/usr/share/doc/HTML/de/palapeli/index.docbook
/usr/share/doc/HTML/en/palapeli/document-export.png
/usr/share/doc/HTML/en/palapeli/document-import.png
/usr/share/doc/HTML/en/palapeli/edit-delete.png
/usr/share/doc/HTML/en/palapeli/go-previous.png
/usr/share/doc/HTML/en/palapeli/index.cache.bz2
/usr/share/doc/HTML/en/palapeli/index.docbook
/usr/share/doc/HTML/en/palapeli/puzzletable1.png
/usr/share/doc/HTML/en/palapeli/tools-wizard.png
/usr/share/doc/HTML/en/palapeli/view-preview.png
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
/V3/usr/lib64/libpala.so.0.2.0
/V3/usr/lib64/qt6/plugins/kf6/thumbcreator/palathumbcreator.so
/V3/usr/lib64/qt6/plugins/palapelislicers/palapeli_goldbergslicer.so
/V3/usr/lib64/qt6/plugins/palapelislicers/palapeli_jigsawslicer.so
/V3/usr/lib64/qt6/plugins/palapelislicers/palapeli_rectslicer.so
/usr/lib64/libpala.so.0
/usr/lib64/libpala.so.0.2.0
/usr/lib64/qt6/plugins/kf6/thumbcreator/palathumbcreator.so
/usr/lib64/qt6/plugins/palapelislicers/palapeli_goldbergslicer.so
/usr/lib64/qt6/plugins/palapelislicers/palapeli_jigsawslicer.so
/usr/lib64/qt6/plugins/palapelislicers/palapeli_rectslicer.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/palapeli/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/palapeli/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/palapeli/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/palapeli/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/palapeli/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/palapeli/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/palapeli/c27070819e7457aece740e2866204327de9c0080

%files locales -f palapeli.lang
%defattr(-,root,root,-)

