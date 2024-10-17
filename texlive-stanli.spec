Name:		texlive-stanli
Version:	54512
Release:	2
Summary:	TikZ Library for Structural Analysis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stanli
License:	gpl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stanli.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stanli.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
stanli is a STructural ANalysis LIbrary based on PGF/TikZ.
Creating new assignments and tests, at university, is usually a
very time-consuming task, especially when this includes drawing
graphics. In the field of structural engineering, those small
structures are a key part for teaching. This package permits to
create such 2D and 3D structures in a very fast and simple way.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/stanli
%doc %{_texmfdistdir}/doc/latex/stanli

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
