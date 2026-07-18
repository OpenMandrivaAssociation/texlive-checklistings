%global tl_name checklistings
%global tl_revision 38300
%global tl_bin_links checklistings:%{_texmfdistdir}/scripts/checklistings/checklistings.sh

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Pass verbatim contents through a compiler and reincorporate the resulting output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/checklistings
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(checklistings.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package augments the fancyvrb and listings packages to allow the
source code they contain to be checked by an external tool (like a
compiler). The external tool's messages can be automatically
reincorporated into the original document. The package does not focus on
a specific programming language, but it is designed to work well with
languages and compilers in the ML family.

