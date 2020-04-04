%{?scl:%scl_package perl-Module-Load}

Name:           %{?scl_prefix}perl-Module-Load
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.34
Release:        451%{?dist}
Summary:        Run-time require of both modules and files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-Load
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-Load-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
BuildRequires:  %{?scl_prefix}perl(vars)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
If you consult "perldoc -f require" you will see that "require" will behave
differently when given a bare-word or a string. In the case of a string,
"require" assumes you are wanting to load a file. But in the case of
a bare-word, it assumes you mean a module.

This gives nasty overhead when you are trying to dynamically require modules
at run-time, since you will need to change the module notation to a file
notation fitting the particular platform you are on.

"load" eliminates the need for this overhead and will just DWYM.

%prep
%setup -q -n Module-Load-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} '%{buildroot}'/*

%check
unset PERL_CORE
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.34-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.34-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.34-438
- Increase release to favour standalone package

* Mon Feb 11 2019 Petr Pisar <ppisar@redhat.com> - 1:0.34-1
- 0.34 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.32-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.32-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 1:0.32-1
- 0.32 bump

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 1:0.30-1
- 0.30 bump

* Tue Jan 07 2014 Petr Pisar <ppisar@redhat.com> - 1:0.28-1
- 0.28 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-3
- Perl 5.18 rebuild

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-2
- Set epoch to compete with perl.spec

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> 0.24-1
- Specfile autogenerated by cpanspec 1.78.
