%define module Catalyst-Plugin-Cache-FastMmap
%define name	perl-%module
%define version	0.8
%define release %mkrel 1

Summary:	Mmap cache for Catalyst applications
Name:		%name
Version:	%version
Release:	%release
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%module/
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{module}-%{version}.tar.gz
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This package is part of the Catalyst Cache family. It allows
integration of Cache::FastMmap and Catalyst.

%prep
%setup -q -n %module-%version

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/Catalyst
%_mandir/*/*

