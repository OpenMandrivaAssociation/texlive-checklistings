Name:		texlive-checklistings
Version:	38300
Release:	1
Summary:	Pass verbatim contents through a compiler and reincorporate the resulting output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/checklistings
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/checklistings.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package augments the fancyvrb and listings packages to
allow the source code they contain to be checked by an external
tool (like a compiler). The external tool's messages can be
automatically reincorporated into the original document. The
package does not focus on a specific programming language, but
it is designed to work well with languages and compilers in the
ML family.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/source/latex/checklistings
%{_texmfdistdir}/tex/latex/checklistings
%{_texmfdistdir}/scripts/checklistings
%doc %{_texmfdistdir}/doc/latex/checklistings

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
