%define upstream_name    Scope-Upper
%define upstream_version 0.22
Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.22
Release:	1

Summary:    Act on upper scopes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Scope/Scope-Upper-0.22.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module lets you defer actions _at run-time_ that will take place when
the control flow returns into an upper scope. Currently, you can:

* *

  hook an upper scope end with the /reap manpage ;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.140.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 643459
- update to new version 0.14

* Thu Dec 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 626241
- new version

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 607543
- import perl-Scope-Upper


