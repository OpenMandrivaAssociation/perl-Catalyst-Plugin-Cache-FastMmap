%define upstream_name    Catalyst-Plugin-Cache-FastMmap
%define upstream_version 0.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Mmap cache for Catalyst applications
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Build)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/Catalyst
%_mandir/*/*
