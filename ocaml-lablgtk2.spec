#
# Conditional build:
%bcond_without	opengl		# lablgtkgl library
%bcond_without	glade		# lablgtkglade library
%bcond_without	gnome		# lablgtkgnome library (incompatible with GNOME 3)
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)
#
# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	GTK+ binding for OCaml
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla
Name:		ocaml-lablgtk2
Version:	2.18.12
Release:	2
License:	LGPL v2.1 with linking exceptions
Group:		Libraries
#Source0Download: https://github.com/garrigue/lablgtk/releases
Source0:	https://github.com/garrigue/lablgtk/archive/%{version}/lablgtk-%{version}.tar.gz
# Source0-md5:	96e5ee228ce26c7ec71a253f87e6d7f7
URL:		https://github.com/garrigue/lablgtk
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
BuildRequires:	ocaml-camlp4 >= 1:3.09.2
%{?with_opengl:BuildRequires:	ocaml-lablgl-devel >= 1.04}
BuildRequires:	sed >= 4.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	GtkSourceView_types GtkSourceView2_types

%description
GTK+ binding for OCaml. This package contains files needed to run
bytecode OCaml programs using LablGtk.

%description -l pl.UTF-8
Wiązania GTK+ dla OCamla. Pakiet ten zawiera binaria potrzebne do
uruchamiania programów używających LablGtk.

%package devel
Summary:	GTK+ binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - część programistyczna
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

%if %{without ocaml_opt}
%{__sed} -i -e '/exists_if/ s/,[^,]*cmx[as]\?//g' META
%endif

%build
%configure \
	CC="%{__cc} %{rpmcflags} -fPIC" \
	%{!?with_gnome:--without-gnomecanvas} \
	%{!?with_glade:--without-glade} \
	%{!?with_opengl:--without-gl}

%{__make} -j1 \
	all %{?with_ocaml_opt:opt}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/stublibs,%{_examplesdir}/%{name}-%{version}}

%{__make} old-install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2 \
	DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# .mli files stay, they are the only documentation, but .ml go
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.ml
gzip -9nf $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.mli
%{__mv} $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2/*.gz .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/lablgtk2
%{_libdir}/ocaml/lablgtk2/META
%{_libdir}/ocaml/lablgtk2/lablgtk.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgtk.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk2.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdk_pixbuf_mlsource
%{_libdir}/ocaml/lablgtk2/g[ABCDEFLMOPRTUW]*.cmi
%{_libdir}/ocaml/lablgtk2/gaux.cmi
%{_libdir}/ocaml/lablgtk2/gdk*.cmi
%{_libdir}/ocaml/lablgtk2/glib.cmi
%{_libdir}/ocaml/lablgtk2/gobject.cmi
%{_libdir}/ocaml/lablgtk2/gpointer.cmi
%{_libdir}/ocaml/lablgtk2/gtk.cmi
%{_libdir}/ocaml/lablgtk2/gtk[ABDEFILMNOPRTW]*.cmi
%{_libdir}/ocaml/lablgtk2/gtkSignal.cmi
%{_libdir}/ocaml/lablgtk2/gtkStock.cmi
%{_libdir}/ocaml/lablgtk2/gutf8.cmi
%{_libdir}/ocaml/lablgtk2/ogtk*.cmi
%{_libdir}/ocaml/lablgtk2/pango*.cmi
%{_libdir}/ocaml/lablgtk2/gtkInit.cmo
%{_libdir}/ocaml/lablgtk2/gtkThInit.cmo
%{_libdir}/ocaml/lablgtk2/gtkThread.cmo
%{_libdir}/ocaml/lablgtk2/liblablgtk2.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/g[ABCDEFLMOPRTUW]*.cmx
%{_libdir}/ocaml/lablgtk2/gaux.cmx
%{_libdir}/ocaml/lablgtk2/gdk*.cmx
%{_libdir}/ocaml/lablgtk2/glib.cmx
%{_libdir}/ocaml/lablgtk2/gobject.cmx
%{_libdir}/ocaml/lablgtk2/gpointer.cmx
%{_libdir}/ocaml/lablgtk2/gtk.cmx
%{_libdir}/ocaml/lablgtk2/gtk[ABDEFILMNOPRTW]*.cmx
%{_libdir}/ocaml/lablgtk2/gtkSignal.cmx
%{_libdir}/ocaml/lablgtk2/gtkStock.cmx
%{_libdir}/ocaml/lablgtk2/gutf8.cmx
%{_libdir}/ocaml/lablgtk2/ogtk*.cmx
%{_libdir}/ocaml/lablgtk2/pango*.cmx
%{_libdir}/ocaml/lablgtk2/gtkInit.o
%{_libdir}/ocaml/lablgtk2/gtkThread.o
%{_libdir}/ocaml/lablgtk2/lablgtk.a
%{_libdir}/ocaml/lablgtk2/lablgtk.cmxa
%endif
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
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/propcc
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/varcc
%{_examplesdir}/%{name}-%{version}

%if %{with opengl}
%files gl
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgtkgl.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgtkgl.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkgl2.so

%files gl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/glGtk.cmi
%{_libdir}/ocaml/lablgtk2/liblablgtkgl2.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/glGtk.cmx
%{_libdir}/ocaml/lablgtk2/lablgtkgl.a
%{_libdir}/ocaml/lablgtk2/lablgtkgl.cmxa
%endif
%{_libdir}/ocaml/lablgtk2/gtkgl_tags.h
%endif

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablglade.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablglade.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablglade2.so

%files glade-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgladecc2
%{_libdir}/ocaml/lablgtk2/glade.cmi
%{_libdir}/ocaml/lablgtk2/liblablglade2.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/glade.cmx
%{_libdir}/ocaml/lablgtk2/lablglade.a
%{_libdir}/ocaml/lablgtk2/lablglade.cmxa
%endif
%endif

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.cma
%{_libdir}/ocaml/lablgtk2/lablgnomeui.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgnomecanvas.cmxs
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgnomeui.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomecanvas.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomeui.so

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gnoCanvas*.cmi
%{_libdir}/ocaml/lablgtk2/gnoDruid.cmi
%{_libdir}/ocaml/lablgtk2/gnomeCanvas*.cmi
%{_libdir}/ocaml/lablgtk2/gnomeDruid.cmi
%{_libdir}/ocaml/lablgtk2/liblablgnomecanvas.a
%{_libdir}/ocaml/lablgtk2/liblablgnomeui.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/gnoCanvas*.cmx
%{_libdir}/ocaml/lablgtk2/gnoDruid.cmx
%{_libdir}/ocaml/lablgtk2/gnomeCanvas*.cmx
%{_libdir}/ocaml/lablgtk2/gnomeDruid.cmx
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.a
%{_libdir}/ocaml/lablgtk2/lablgnomecanvas.cmxa
%{_libdir}/ocaml/lablgtk2/lablgnomeui.a
%{_libdir}/ocaml/lablgtk2/lablgnomeui.cmxa
%endif
%endif

%files gtkspell
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgtkspell.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgtkspell.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkspell.so

%files gtkspell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gtkSpell.cmi
%{_libdir}/ocaml/lablgtk2/liblablgtkspell.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/gtkSpell.cmx
%{_libdir}/ocaml/lablgtk2/lablgtkspell.a
%{_libdir}/ocaml/lablgtk2/lablgtkspell.cmxa
%endif

%files gtksourceview
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgtksourceview.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgtksourceview.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtksourceview.so

%files gtksourceview-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gSourceView.cmi
%{_libdir}/ocaml/lablgtk2/gtkSourceView.cmi
%{_libdir}/ocaml/lablgtk2/sourceViewEnums.cmi
%{_libdir}/ocaml/lablgtk2/liblablgtksourceview.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/gSourceView.cmx
%{_libdir}/ocaml/lablgtk2/gtkSourceView.cmx
%{_libdir}/ocaml/lablgtk2/sourceViewEnums.cmx
%{_libdir}/ocaml/lablgtk2/lablgtksourceview.a
%{_libdir}/ocaml/lablgtk2/lablgtksourceview.cmxa
%endif
%{_libdir}/ocaml/lablgtk2/sourceView_tags.h

%files gtksourceview2
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablgtksourceview2.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablgtksourceview2.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtksourceview2.so

%files gtksourceview2-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/gSourceView2.cmi
%{_libdir}/ocaml/lablgtk2/gtkSourceView2.cmi
%{_libdir}/ocaml/lablgtk2/sourceView2Enums.cmi
%{_libdir}/ocaml/lablgtk2/liblablgtksourceview2.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/gSourceView2.cmx
%{_libdir}/ocaml/lablgtk2/gtkSourceView2.cmx
%{_libdir}/ocaml/lablgtk2/sourceView2Enums.cmx
%{_libdir}/ocaml/lablgtk2/lablgtksourceview2.a
%{_libdir}/ocaml/lablgtk2/lablgtksourceview2.cmxa
%endif
%{_libdir}/ocaml/lablgtk2/sourceView2_tags.h

%files rsvg
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/lablrsvg.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk2/lablrsvg.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablrsvg.so

%files rsvg-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk2/rsvg.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk2/rsvg.cmx
%{_libdir}/ocaml/lablgtk2/lablrsvg.cmxa
%{_libdir}/ocaml/lablgtk2/lablrsvg.a
%endif
%{_libdir}/ocaml/lablgtk2/liblablrsvg.a

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk2
