#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
%define keepstatic 1
Name     : readline
Version  : 7.0
Release  : 44
URL      : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz
Source0  : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz
Source99 : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz.asc
Summary  : Gnu Readline library for command line editing
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: readline-lib
Requires: readline-doc
Requires: readline-data
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
Patch1: 0001-Defaultinput-meta-output-meta-to-on.patch
Patch2: cve-2014-2524.nopatch
Patch3: 0001-Support-stateless-inputrc-configuration.patch
Patch4: build.patch
Patch5: readline-6.2-shlib.patch
Patch6: tinfow.patch

%description
Introduction
============
This is the Gnu Readline library, version 7.0.
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
Requires: readline-lib
Requires: readline-data
Provides: readline-devel

%description dev
dev components for the readline package.


%package dev32
Summary: dev32 components for the readline package.
Group: Default
Requires: readline-lib32
Requires: readline-data
Requires: readline-dev

%description dev32
dev32 components for the readline package.


%package doc
Summary: doc components for the readline package.
Group: Documentation

%description doc
doc components for the readline package.


%package extras
Summary: extras components for the readline package.
Group: Default

%description extras
extras components for the readline package.


%package lib
Summary: lib components for the readline package.
Group: Libraries
Requires: readline-data

%description lib
lib components for the readline package.


%package lib32
Summary: lib32 components for the readline package.
Group: Default
Requires: readline-data

%description lib32
lib32 components for the readline package.


%prep
%setup -q -n readline-7.0
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a readline-7.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496502750
unset LD_AS_NEEDED
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
%configure  --with-curses --enable-multibyte
make V=1  %{?_smp_mflags} SHLIB_LIBS="-ltinfo"

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure  --with-curses --enable-multibyte   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags} SHLIB_LIBS="-ltinfo"
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1496502750
rm -rf %{buildroot}
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
## make_install_append content
rm %{buildroot}/usr/lib64/libreadline.so
echo "INPUT(libreadline.so.7 -ltinfow)" > %{buildroot}/usr/lib64/libreadline.so
chmod 755 %{buildroot}/usr/lib64/*
## make_install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
%exclude /usr/share/readline/excallback.c
%exclude /usr/share/readline/fileman.c
%exclude /usr/share/readline/hist_erasedups.c
%exclude /usr/share/readline/hist_purgecmd.c
%exclude /usr/share/readline/histexamp.c
%exclude /usr/share/readline/manexamp.c
%exclude /usr/share/readline/rl-callbacktest.c
%exclude /usr/share/readline/rl-fgets.c
%exclude /usr/share/readline/rl.c
%exclude /usr/share/readline/rlbasic.c
%exclude /usr/share/readline/rlcat.c
%exclude /usr/share/readline/rlevent.c
%exclude /usr/share/readline/rlptytest.c
%exclude /usr/share/readline/rltest.c
%exclude /usr/share/readline/rlversion.c

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
/usr/lib64/*.a
/usr/lib64/libhistory.so
/usr/lib64/libreadline.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/*.a
/usr/lib32/libhistory.so
/usr/lib32/libreadline.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/readline/*
%doc /usr/share/info/*
%doc /usr/share/man/man3/*

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhistory.so.7
/usr/lib64/libhistory.so.7.0
/usr/lib64/libreadline.so.7
/usr/lib64/libreadline.so.7.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libhistory.so.7
/usr/lib32/libhistory.so.7.0
/usr/lib32/libreadline.so.7
/usr/lib32/libreadline.so.7.0
