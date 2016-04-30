#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : readline
Version  : 6.3
Release  : 22
URL      : http://mirrors.kernel.org/gnu/readline/readline-6.3.tar.gz
Source0  : http://mirrors.kernel.org/gnu/readline/readline-6.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: readline-lib
Requires: readline-doc
Requires: readline-data
BuildRequires : ncurses-dev
Patch1: readline63-001
Patch2: readline63-002
Patch3: readline63-003
Patch4: readline63-004
Patch5: readline63-005
Patch6: readline63-006
Patch7: readline63-007
Patch8: readline63-008
Patch9: 0001-Defaultinput-meta-output-meta-to-on.patch
Patch10: cve-2014-2524.nopatch
Patch11: 0001-Support-stateless-inputrc-configuration.patch
Patch12: build.patch

%description
Introduction
============
This is the Gnu Readline library, version 6.3.
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
Requires: ncurses-dev

%description dev
dev components for the readline package.


%package doc
Summary: doc components for the readline package.
Group: Documentation

%description doc
doc components for the readline package.


%package lib
Summary: lib components for the readline package.
Group: Libraries
Requires: readline-data

%description lib
lib components for the readline package.


%prep
%setup -q -n readline-6.3
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch11 -p1
%patch12 -p1

%build
%configure  --with-curses
make V=1  %{?_smp_mflags} SHLIB_LIBS="-ltinfo"

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
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
/usr/share/readline/rlcat.c
/usr/share/readline/rlevent.c
/usr/share/readline/rlptytest.c
/usr/share/readline/rltest.c
/usr/share/readline/rlversion.c

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
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/readline/*
%doc /usr/share/info/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
