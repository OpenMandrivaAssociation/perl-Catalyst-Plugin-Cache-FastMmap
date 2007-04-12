%define realname Catalyst-Plugin-Cache-FastMmap
%define name	perl-%realname

%define version	0.6

%define rel	3
%define release %mkrel %rel

Summary:	Mmap cache for Catalyst applications
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%realname/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%realname-%version.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
Buildroot:	%_tmppath/%name-buildroot

%description
This package is part of the Catalyst Cache family. It allows
integration of Cache::FastMmap and Catalyst.

%prep
%setup -q -n %realname-%version

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=%buildroot

%files
%defattr(644,root,root,755)
%doc Changes README
%perl_vendorlib/Catalyst
%_mandir/*/*

%clean
rm -rf $RPM_BUILD_ROOT

