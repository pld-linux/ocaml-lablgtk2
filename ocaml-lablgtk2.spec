#
# Conditional build:
%bcond_without	gl	# without lablgtkgl
%bcond_without	gnome	# without lablgtkgnome
%bcond_without	glade	# without lablgtkglade
#
%define		ocaml_ver	1:3.09.2
Summary:	GTK+ binding for OCaml
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla
Name:		ocaml-lablgtk2
Version:	2.6.0
Release:	4
License:	LGPL w/ linking exceptions
Group:		Libraries
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk-%{version}.tar.gz
# Source0-md5:	47319aacbbb761323bdfab67513829df
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
BuildRequires:	gtk+2-devel >= 2.0
%{?with_gl:BuildRequires:	gtkglarea-devel >= 1.99}
BuildRequires:	gtkspell-devel >= 2.0
%{?with_glade:BuildRequires:	libglade2-devel >= 2.0}
%if %{with gnome}
BuildRequires:	gnome-panel-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeui-devel
%endif
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	ocaml-camlp4 >= %{ocaml_ver}
%{?with_gl:BuildRequires:	ocaml-lablgl-devel}
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ binding for OCaml. This package contains files needed to run
bytecode OCaml programs using LablGtk.

%description -l pl.UTF-8
Wiązania GTK+ dla OCamla. Pakiet ten zawiera binaria potrzebne do
uruchamiania programów używających LablGtk.

%package devel
Summary:	GTK+ binding for OCaml - development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel

%description devel
GTK+ binding for OCaml. This package contains files needed to develop
OCaml programs using LablGtk.

%description devel -l pl.UTF-8
Wiązania GTK+ dla OCamla. Pakiet ten zawiera pliki niezbędne do
tworzenia programów używających LablGtk.

%package gl
Summary:	GTK+ binding for OCaml - GtkGL support
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla GtkGL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-lablgl
%requires_eq	ocaml-runtime

%description gl
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GtkGL.

%description gl -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów używających LablGtk-GtkGL.

%package gl-devel
Summary:	GTK+ binding for OCaml - GtkGL support, development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla GtkGL, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gl = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel

%description gl-devel
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to develop OCaml programs using LablGtk-GtkGL.

%description gl-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających LablGtk-GtkGL.

%package glade
Summary:	GTK+ binding for OCaml - Glade support
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla Glade
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description glade
GTK+ binding for OCaml, Glade support. This package contains files
needed to run bytecode OCaml programs using LablGtk-Glade.

%description glade -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów używających LablGtk-Glade.

%package glade-devel
Summary:	GTK+ binding for OCaml - Glade support, development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla Glade, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-glade = %{version}-%{release}
%requires_eq	ocaml

%description glade-devel
GTK+ binding for OCaml, Glade support. This package contains files
needed to develop OCaml programs using LablGtk-Glade.

%description glade-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających LablGtk-Glade.

%package gnome
Summary:	GTK+ binding for OCaml - GNOME support
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla GNOME
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description gnome
GTK+ binding for OCaml, GNOME support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GNOME.

%description gnome -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów używających LablGtk-GNOME.

%package gnome-devel
Summary:	GTK+ binding for OCaml - GNOME support, development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla GNOME, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gnome = %{version}-%{release}
%requires_eq	ocaml

%description gnome-devel
GTK+ binding for OCaml, GNOME support. This package contains files
needed to develop OCaml programs using LablGtk-GNOME.

%description gnome-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających LablGtk-GNOME.

%package gtkspell
Summary:	GTK+ binding for OCaml - GtkSpell support
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - obsługa GtkSpella
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description gtkspell
GTK+ binding for OCaml, GtkSpell support.

%description gtkspell -l pl.UTF-8
Wiązania GTK+ dla OCamla, obsługa GtkSpella

%package gtkspell-devel
Summary:	GTK+ binding for OCaml - GtkSpell support, development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - obsługa GtkSpella, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtkspell = %{version}-%{release}
%requires_eq	ocaml

%description gtkspell-devel
GTK+ binding for OCaml, GtkSpell support. This package contains files
needed to develop OCaml programs using LablGtk-GtkSpell.

%description gtkspell-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, obsługa GtkSpella. Ten pakiet zawiera pliki
niezbędne do tworzenia programów używających LablGtk-GtkSpell.

%package rsvg
Summary:	GTK+ binding for OCaml - RSVG support
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla RSVG
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description rsvg
GTK+ binding for OCaml, RSVG support. This package contains files
needed to run bytecode OCaml programs using LablGtk-RSVG.

%description rsvg -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla RSVG. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów używających LablGtk-RSVG.

%package rsvg-devel
Summary:	GTK+ binding for OCaml - RSVG support, development part
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - wsparcie dla RSVG, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-rsvg = %{version}-%{release}
%requires_eq	ocaml

%description rsvg-devel
GTK+ binding for OCaml, RSVG support. This package contains files
needed to develop OCaml programs using LablGtk-RSVG.

%description rsvg-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla RSVG. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających LablGtk-RSVG.

%package toplevel
Summary:	GTK+ binding for OCaml - interactive system
Summary(pl.UTF-8):   Wiązania GTK+ dla OCamla - system interaktywny
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%requires_eq	ocaml

%description toplevel
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains OCaml toplevel interactive system linked with
lablgtk.

%description toplevel -l pl.UTF-8
Wiązania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest dołączone.
Pakiet ten zawiera system interaktywny OCamla skonsolidowany z
lablgtk.

%prep
%setup -q -n lablgtk-%{version}

%build
%configure \
	CC="%{__cc} %{rpmcflags} -fPIC" \
	%{!?with_gnome:--without-gnomecanvas} \
	%{!?with_glade:--without-glade} \
	%{!?with_gl:--without-gl}

%{__make} -j1 \
	all opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{stublibs,site-lib/labl{gtk2,gnomecanvas,glade,gtkgl,gtkspell,rsvg}},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2 \
	DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# .mli files stay, they are the only documentation, but .ml go
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.ml
gzip -9nf $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.mli
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.gz .

# make METAs for findlib
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/lablgtk2/META <<EOF
# Specifications for the "lablgtk2" library:
requires = ""
version = "%{version}"
directory = "+lablgtk2"
archive(byte) = "lablgtk.cma gtkInit.cmo"
archive(native) = "lablgtk.cmxa gtkInit.cmx"
linkopts = ""
EOF

for f in glade %{?with_gnome:gnomecanvas} gtkgl gtkspell rsvg ; do
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/labl$f/META <<EOF
# Specifications for the "lablgtk" library:
requires = "lablgtk2"
version = "%{version}"
directory = "+lablgtk2"
archive(byte) = "labl$f.cma"
archive(native) = "labl$f.cmxa"
linkopts = ""
EOF
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/lablgtk2
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk2.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdk-pixbuf-mlsource
%{_libdir}/ocaml/lablgtk2/g[BCDELMOPRTUWadp]*.cm*
%{_libdir}/ocaml/lablgtk2/gAction.cm*
%{_libdir}/ocaml/lablgtk2/gFile.cm*
%{_libdir}/ocaml/lablgtk2/glib.cm*
%{_libdir}/ocaml/lablgtk2/gobject.cm*
%{_libdir}/ocaml/lablgtk2/gtk.cm*
%{_libdir}/ocaml/lablgtk2/gtkFile.cm*
%{_libdir}/ocaml/lablgtk2/gtkObject.cm*
%{_libdir}/ocaml/lablgtk2/pango*.cm*
%{_libdir}/ocaml/lablgtk2/gtk[ABDEILMNPRSTW]*.cm*
%{_libdir}/ocaml/lablgtk2/*.[ho]
%{_libdir}/ocaml/lablgtk2/lablgtk.*
%{_libdir}/ocaml/lablgtk2/liblablgtk2.*
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/varcc
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/propcc
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/lablgtk2

%if %{with gl}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkgl2.so

%files gl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/glGtk.cm*
%{_libdir}/ocaml/lablgtk2/lablgtkgl.*
%{_libdir}/ocaml/lablgtk2/liblablgtkgl2.*
%{_libdir}/ocaml/site-lib/lablgtkgl
%endif

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablglade2.so

%files glade-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgladecc2
%{_libdir}/ocaml/lablgtk2/glade.cm*
%{_libdir}/ocaml/lablgtk2/lablglade.*
%{_libdir}/ocaml/lablgtk2/liblablglade2.*
%{_libdir}/ocaml/site-lib/lablglade
%endif

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomecanvas.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomeui.so

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/*Canvas*.cm*
%{_libdir}/ocaml/lablgtk2/*Druid.cm*
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.*
%{_libdir}/ocaml/lablgtk2/liblablgnomecanvas.*
%{_libdir}/ocaml/lablgtk2/lablgnomeui.cm*
%{_libdir}/ocaml/lablgtk2/*lablgnomeui.a
%{_libdir}/ocaml/site-lib/lablgnomecanvas
%endif

%files gtkspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkspell.so

%files gtkspell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgtkspell.*
%{_libdir}/ocaml/lablgtk2/liblablgtkspell.a
%{_libdir}/ocaml/site-lib/lablgtkspell

%files rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablrsvg.so

%files rsvg-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/rsvg.cm*
%{_libdir}/ocaml/lablgtk2/lablrsvg.*
%{_libdir}/ocaml/lablgtk2/liblablrsvg.*
%{_libdir}/ocaml/site-lib/lablrsvg

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk2
