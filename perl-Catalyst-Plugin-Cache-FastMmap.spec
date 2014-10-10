%define upstream_name    Catalyst-Plugin-Cache-FastMmap
%define upstream_version 0.9

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Mmap cache for Catalyst applications
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

%description
This package is part of the Catalyst Cache family. It allows
integration of Cache::FastMmap and Catalyst.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL installdirs=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1mdv2011.0
+ Revision: 648058
- update to new version 0.9

* Sat Feb 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.800.0-1mdv2011.0
+ Revision: 505418
- rebuild using %%perl_convert_version

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-1mdv2010.0
+ Revision: 378164
- new version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6-4mdv2009.0
+ Revision: 136676
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-4mdv2008.0
+ Revision: 85995
- rebuild


* Wed May 03 2006 Scott Karns <scottk@mandriva.org> 0.6-3mdk
- Add BuildRequires perl(Class::Data::Inheritable)

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-2mdk
- Add BuildRequires

* Thu Apr 27 2006 Scott Karns <scottk@mandriva.org> 0.6-1mdk
- Initial MDV RPM

