# revision 17909
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fun
# catalog-date 2010-04-18 16:26:27 +0200
# catalog-license lppl
# catalog-version 0.04
Name:		texlive-pst-fun
Version:	0.04
Release:	1
Summary:	Draw "funny" objects with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a PSTricks related package for drawing funny objects,
like ant, bird, fish, kangaroo, ... Such objects may be useful
for testing other PSTricks macros and/or packages. (Or they can
be used for fun...).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
