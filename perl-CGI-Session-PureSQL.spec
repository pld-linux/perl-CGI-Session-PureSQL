#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Session-PureSQL
Summary:	CGI::Session::PureSQL - driver with no embedded Perl stored in the database
Summary(pl.UTF-8):   CGI::Session::PureSQL - sterownik nie przechowujący osadzonego Perla w bazie danych
Name:		perl-CGI-Session-PureSQL
Version:	0.54
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c8e9eff4a11b1b9e0fb2dbc2d50f13c
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Date-Calc
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Session::PureSQL - driver with no embedded Perl stored in the
database.

%description -l pl.UTF-8
CGI::Session::PureSQL - sterownik nie przechowujący osadzonego Perla w
bazie danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build
				
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/CGI/Session/*.pm
%{perl_vendorlib}/CGI/Session/Serialize
%{_mandir}/man3/*
