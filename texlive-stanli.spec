%global tl_name stanli
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	TikZ Library for Structural Analysis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/stanli
License:	gpl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stanli.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stanli.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
stanli is a STructural ANalysis LIbrary based on PGF/TikZ. Creating new
assignments and tests, at university, is usually a very time-consuming
task, especially when this includes drawing graphics. In the field of
structural engineering, those small structures are a key part for
teaching. This package permits to create such 2D and 3D structures in a
very fast and simple way.

