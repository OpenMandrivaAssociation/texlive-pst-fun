%global tl_name pst-fun
%global tl_revision 79050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.06
Release:	%{tl_revision}.1
Summary:	Draw funny objects with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fun
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fun.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a PSTricks related package for drawing funny objects, like ant,
bird, fish, kangaroo, ... Such objects may be useful for testing other
PSTricks macros and/or packages. (Or they can be used for fun...)

