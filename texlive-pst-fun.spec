Name:		texlive-pst-fun
Version:	17909
Release:	2
Summary:	Draw "funny" objects with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks related package for drawing funny objects,
like ant, bird, fish, kangaroo, ... Such objects may be useful
for testing other PSTricks macros and/or packages. (Or they can
be used for fun...).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-fun/pst-fun.pro
%{_texmfdistdir}/tex/generic/pst-fun/pst-fun.tex
%{_texmfdistdir}/tex/latex/pst-fun/pst-fun.sty
%doc %{_texmfdistdir}/doc/generic/pst-fun/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fun/README
%doc %{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-fun/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
