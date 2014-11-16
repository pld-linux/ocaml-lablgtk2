#
# Conditional build:
%bcond_without	opengl	# without lablgtkgl
%bcond_without	glade	# without lablgtkglade
%bcond_without	gnome	# with lablgtkgnome (incompatible with GNOME 3)
#
%define		ocaml_ver	1:3.09.2
Summary:	GTK+ binding for OCaml
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla
Name:		ocaml-lablgtk2
Version:	2.18.3
Release:	1
License:	LGPL with linking exceptions
Group:		Libraries
#Source0Download: http://lablgtk.forge.ocamlcore.org/
Source0:	https://forge.ocamlcore.org/frs/download.php/1479/lablgtk-%{version}.tar.gz
# Source0-md5:	bcbad64a28c3dc40f24cc7a4d2f1d0dd
URL:		http://lablgtk.forge.ocamlcore.org/
BuildRequires:	gtk+2-devel >= 2:2.10.0
%{?with_opengl:BuildRequires:	gtkglarea-devel >= 1.99}
BuildRequires:	gtkspell-devel >= 2.0
BuildRequires:	gtksourceview-devel
BuildRequires:	gtksourceview2-devel
%{?with_glade:BuildRequires:	libglade2-devel >= 2.0}
%if %{with gnome}
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeui-devel
%endif
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	ocaml-camlp4 >= %{ocaml_ver}
%{?with_opengl:BuildRequires:	ocaml-lablgl-devel >= 1.04}
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
GTK+ binding for OCaml. This package contains files needed to develop
OCaml programs using LablGtk.

%description devel -l pl.UTF-8
Wiązania GTK+ dla OCamla. Pakiet ten zawiera pliki niezbędne do
tworzenia programów używających LablGtk.

%package gl
Summary:	GTK+ binding for OCaml - GtkGL support
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkGL
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkGL, część programistyczna
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla Glade
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla Glade, część programistyczna
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GNOME
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GNOME, część programistyczna
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - obsługa GtkSpella
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description gtkspell
GTK+ binding for OCaml, GtkSpell support.

%description gtkspell -l pl.UTF-8
Wiązania GTK+ dla OCamla, obsługa GtkSpella

%package gtkspell-devel
Summary:	GTK+ binding for OCaml - GtkSpell support, development part
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - obsługa GtkSpella, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtkspell = %{version}-%{release}
%requires_eq	ocaml

%description gtkspell-devel
GTK+ binding for OCaml, GtkSpell support. This package contains files
needed to develop OCaml programs using LablGtk-GtkSpell.

%description gtkspell-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, obsługa GtkSpella. Ten pakiet zawiera pliki
niezbędne do tworzenia programów używających LablGtk-GtkSpell.

%package gtksourceview
Summary:	GTK+ binding for OCaml - GtkSourceView support
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkSourceView
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview
GTK+ binding for OCaml, GtkSourceView support. This package contains
files needed to run bytecode OCaml programs using
LablGtk-GtkSourceView.

%description gtksourceview -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkSourceView. Pakiet ten
zawiera binaria potrzebne do uruchamiania programów używających
LablGtk-GtkSourceView.

%package gtksourceview-devel
Summary:	GTK+ binding for OCaml - GtkSourceView support, development part
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkSourceView, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtksourceview = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview-devel
GTK+ binding for OCaml, GtkSourceView support. This package contains
files needed to develop OCaml programs using LablGtk-GtkSourceView.

%description gtksourceview-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkSourceView. Pakiet ten
zawiera pliki niezbędne do tworzenia programów używających
LablGtk-GtkSourceView.

%package gtksourceview2
Summary:	GTK+ binding for OCaml - GtkSourceView2 support
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkSourceView2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview2
GTK+ binding for OCaml, GtkSourceView2 support. This package contains
files needed to run bytecode OCaml programs using
LablGtk-GtkSourceView2.

%description gtksourceview2 -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkSourceView2. Pakiet ten
zawiera binaria potrzebne do uruchamiania programów używających
LablGtk-GtkSourceView2.

%package gtksourceview2-devel
Summary:	GTK+ binding for OCaml - GtkSourceView2 support, development part
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla GtkSourceView2, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtksourceview2 = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview2-devel
GTK+ binding for OCaml, GtkSourceView2 support. This package contains
files needed to develop OCaml programs using LablGtk-GtkSourceView2.

%description gtksourceview2-devel -l pl.UTF-8
Wiązania GTK+ dla OCamla, wsparcie dla GtkSourceView2. Pakiet ten
zawiera pliki niezbędne do tworzenia programów używających
LablGtk-GtkSourceView2.

%package rsvg
Summary:	GTK+ binding for OCaml - RSVG support
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla RSVG
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - wsparcie dla RSVG, część programistyczna
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
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - system interaktywny
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
	%{!?with_opengl:--without-gl}

%{__make} -j1 \
	all opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{stublibs,site-lib/labl{gtk2,gnomecanvas,glade,gtkgl,gtkspell,rsvg}},%{_examplesdir}/%{name}-%{version}}

%{__make} old-install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2 \
	DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# .mli files stay, they are the only documentation, but .ml go
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.ml
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
%attr(755,root,root) %{_bindir}/gdk_pixbuf_mlsource
%{_libdir}/ocaml/lablgtk2/g[ABCDEFLMOPRTUW]*.cm*
%{_libdir}/ocaml/lablgtk2/gaux.cm*
%{_libdir}/ocaml/lablgtk2/gdk*.cm*
%{_libdir}/ocaml/lablgtk2/glib.cm*
%{_libdir}/ocaml/lablgtk2/gobject.cm*
%{_libdir}/ocaml/lablgtk2/gpointer.cm*
%{_libdir}/ocaml/lablgtk2/gtk.cm*
%{_libdir}/ocaml/lablgtk2/gtk[ABDEFILMNOPRTW]*.cm*
%{_libdir}/ocaml/lablgtk2/gtkSignal.cm*
%{_libdir}/ocaml/lablgtk2/gtkStock.cm*
%{_libdir}/ocaml/lablgtk2/gutf8.cm*
%{_libdir}/ocaml/lablgtk2/ogtk*.cm*
%{_libdir}/ocaml/lablgtk2/pango*.cm*
%{_libdir}/ocaml/lablgtk2/gtkInit.o
%{_libdir}/ocaml/lablgtk2/gtkThread.o
%{_libdir}/ocaml/lablgtk2/gdk_tags.h
%{_libdir}/ocaml/lablgtk2/gdkpixbuf_tags.h
%{_libdir}/ocaml/lablgtk2/gdkprivate-win32.h
%{_libdir}/ocaml/lablgtk2/glib_tags.h
%{_libdir}/ocaml/lablgtk2/gnomeui_tags.h
%{_libdir}/ocaml/lablgtk2/gobject_tags.h
%{_libdir}/ocaml/lablgtk2/gtk_tags.h
%{_libdir}/ocaml/lablgtk2/ml_*.h
%{_libdir}/ocaml/lablgtk2/pango_tags.h
%{_libdir}/ocaml/lablgtk2/win32.h
%{_libdir}/ocaml/lablgtk2/wrappers.h
%{_libdir}/ocaml/lablgtk2/lablgtk.a
%{_libdir}/ocaml/lablgtk2/lablgtk.cm*
%{_libdir}/ocaml/lablgtk2/liblablgtk2.a
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/propcc
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/varcc
%{_libdir}/ocaml/site-lib/lablgtk2
%{_examplesdir}/%{name}-%{version}

%if %{with opengl}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkgl2.so

%files gl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/glGtk.cm*
%{_libdir}/ocaml/lablgtk2/gtkgl_tags.h
%{_libdir}/ocaml/lablgtk2/lablgtkgl.a
%{_libdir}/ocaml/lablgtk2/lablgtkgl.cm*
%{_libdir}/ocaml/lablgtk2/liblablgtkgl2.a
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
%{_libdir}/ocaml/lablgtk2/lablglade.a
%{_libdir}/ocaml/lablgtk2/lablglade.cm*
%{_libdir}/ocaml/lablgtk2/liblablglade2.a
%{_libdir}/ocaml/site-lib/lablglade
%endif

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomecanvas.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomeui.so

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gnoCanvas*.cm*
%{_libdir}/ocaml/lablgtk2/gnoDruid.cm*
%{_libdir}/ocaml/lablgtk2/gnomeCanvas*.cm*
%{_libdir}/ocaml/lablgtk2/gnomeDruid.cm*
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.a
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.cm*
%{_libdir}/ocaml/lablgtk2/lablgnomeui.a
%{_libdir}/ocaml/lablgtk2/lablgnomeui.cm*
%{_libdir}/ocaml/lablgtk2/liblablgnomecanvas.a
%{_libdir}/ocaml/lablgtk2/liblablgnomeui.a
%{_libdir}/ocaml/site-lib/lablgnomecanvas
%endif

%files gtkspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkspell.so

%files gtkspell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gtkSpell.cm*
%{_libdir}/ocaml/lablgtk2/lablgtkspell.a
%{_libdir}/ocaml/lablgtk2/lablgtkspell.cm*
%{_libdir}/ocaml/lablgtk2/liblablgtkspell.a
%{_libdir}/ocaml/site-lib/lablgtkspell

%files gtksourceview
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtksourceview.so

%files gtksourceview-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gSourceView.cm*
%{_libdir}/ocaml/lablgtk2/gtkSourceView.cm*
%{_libdir}/ocaml/lablgtk2/sourceViewEnums.cm*
%{_libdir}/ocaml/lablgtk2/sourceView_tags.h
%{_libdir}/ocaml/lablgtk2/lablgtksourceview.a
%{_libdir}/ocaml/lablgtk2/lablgtksourceview.cm*
%{_libdir}/ocaml/lablgtk2/liblablgtksourceview.a

%files gtksourceview2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtksourceview2.so

%files gtksourceview2-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gSourceView2.cm*
%{_libdir}/ocaml/lablgtk2/gtkSourceView2.cm*
%{_libdir}/ocaml/lablgtk2/sourceView2Enums.cm*
%{_libdir}/ocaml/lablgtk2/sourceView2_tags.h
%{_libdir}/ocaml/lablgtk2/lablgtksourceview2.a
%{_libdir}/ocaml/lablgtk2/lablgtksourceview2.cm*
%{_libdir}/ocaml/lablgtk2/liblablgtksourceview2.a

%files rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablrsvg.so

%files rsvg-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/rsvg.cm*
%{_libdir}/ocaml/lablgtk2/lablrsvg.a
%{_libdir}/ocaml/lablgtk2/lablrsvg.cm*
%{_libdir}/ocaml/lablgtk2/liblablrsvg.a
%{_libdir}/ocaml/site-lib/lablrsvg

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk2
