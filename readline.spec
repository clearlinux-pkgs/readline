#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
%define keepstatic 1
Name     : readline
Version  : 8.1
Release  : 60
URL      : https://mirrors.kernel.org/gnu/readline/readline-8.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/readline/readline-8.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/readline/readline-8.1.tar.gz.sig
Summary  : Gnu Readline library for command line editing
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: readline-data = %{version}-%{release}
Requires: readline-info = %{version}-%{release}
Requires: readline-lib = %{version}-%{release}
Requires: readline-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
Patch1: 0001-Defaultinput-meta-output-meta-to-on.patch
Patch2: 0001-Support-stateless-inputrc-configuration.patch
Patch3: 0001-Fix-to-use-tinfow.patch
Patch4: build.patch
Patch5: tinfow.patch
Patch6: pcfile.patch

%description
Introduction
============
This is the Gnu Readline library, version 8.1.
The Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in.  Both
Emacs and vi editing modes are available.  The Readline library includes
additional functions to maintain a list of previously-entered command
lines, to recall and perhaps reedit those lines, and perform csh-like
history expansion on previous commands.

%package data
Summary: data components for the readline package.
Group: Data

%description data
data components for the readline package.


%package dev
Summary: dev components for the readline package.
Group: Development
Requires: readline-lib = %{version}-%{release}
Requires: readline-data = %{version}-%{release}
Provides: readline-devel = %{version}-%{release}
Requires: readline = %{version}-%{release}

%description dev
dev components for the readline package.


%package dev32
Summary: dev32 components for the readline package.
Group: Default
Requires: readline-lib32 = %{version}-%{release}
Requires: readline-data = %{version}-%{release}
Requires: readline-dev = %{version}-%{release}

%description dev32
dev32 components for the readline package.


%package doc
Summary: doc components for the readline package.
Group: Documentation
Requires: readline-info = %{version}-%{release}

%description doc
doc components for the readline package.


%package extras
Summary: extras components for the readline package.
Group: Default

%description extras
extras components for the readline package.


%package info
Summary: info components for the readline package.
Group: Default

%description info
info components for the readline package.


%package lib
Summary: lib components for the readline package.
Group: Libraries
Requires: readline-data = %{version}-%{release}
Requires: readline-license = %{version}-%{release}

%description lib
lib components for the readline package.


%package lib32
Summary: lib32 components for the readline package.
Group: Default
Requires: readline-data = %{version}-%{release}
Requires: readline-license = %{version}-%{release}

%description lib32
lib32 components for the readline package.


%package license
Summary: license components for the readline package.
Group: Default

%description license
license components for the readline package.


%package staticdev
Summary: staticdev components for the readline package.
Group: Default
Requires: readline-dev = %{version}-%{release}

%description staticdev
staticdev components for the readline package.


%package staticdev32
Summary: staticdev32 components for the readline package.
Group: Default
Requires: readline-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the readline package.


%prep
%setup -q -n readline-8.1
cd %{_builddir}/readline-8.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a readline-8.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609809242
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --with-curses --enable-multibyte
make  %{?_smp_mflags}  SHLIB_LIBS="-ltinfow"

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure  --with-curses --enable-multibyte   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  SHLIB_LIBS="-ltinfow"
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1609809242
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/readline
cp %{_builddir}/readline-8.1/COPYING %{buildroot}/usr/share/package-licenses/readline/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## install_append content
rm %{buildroot}/usr/lib64/libreadline.so
echo "INPUT(libreadline.so.8 -ltinfow)" > %{buildroot}/usr/lib64/libreadline.so
chmod 755 %{buildroot}/usr/lib64/*
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/readline/rlkeymaps.c

%files dev
%defattr(-,root,root,-)
/usr/include/readline/chardefs.h
/usr/include/readline/history.h
/usr/include/readline/keymaps.h
/usr/include/readline/readline.h
/usr/include/readline/rlconf.h
/usr/include/readline/rlstdc.h
/usr/include/readline/rltypedefs.h
/usr/include/readline/tilde.h
/usr/lib64/libhistory.so
/usr/lib64/libreadline.so
/usr/lib64/pkgconfig/readline.pc
/usr/share/man/man3/history.3
/usr/share/man/man3/readline.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libhistory.so
/usr/lib32/libreadline.so
/usr/lib32/pkgconfig/32readline.pc
/usr/lib32/pkgconfig/readline.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/readline/*

%files extras
%defattr(-,root,root,-)
/usr/share/readline/excallback.c
/usr/share/readline/fileman.c
/usr/share/readline/hist_erasedups.c
/usr/share/readline/hist_purgecmd.c
/usr/share/readline/histexamp.c
/usr/share/readline/manexamp.c
/usr/share/readline/rl-callbacktest.c
/usr/share/readline/rl-fgets.c
/usr/share/readline/rl.c
/usr/share/readline/rlbasic.c
/usr/share/readline/rlcat.c
/usr/share/readline/rlevent.c
/usr/share/readline/rlptytest.c
/usr/share/readline/rltest.c
/usr/share/readline/rlversion.c

%files info
%defattr(0644,root,root,0755)
/usr/share/info/history.info
/usr/share/info/readline.info
/usr/share/info/rluserman.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhistory.so.8
/usr/lib64/libhistory.so.8.1
/usr/lib64/libreadline.so.8
/usr/lib64/libreadline.so.8.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libhistory.so.8
/usr/lib32/libhistory.so.8.1
/usr/lib32/libreadline.so.8
/usr/lib32/libreadline.so.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/readline/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libhistory.a
/usr/lib64/libreadline.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libhistory.a
/usr/lib32/libreadline.a
