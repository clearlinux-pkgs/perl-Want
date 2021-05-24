#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Want
Version  : 0.29
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Want-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Want-0.29.tar.gz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-Want-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
-----------------------------------------------------------------------------
| Want v0.29    - Robin Houston, 2016-02-26
-----------------------------------------------------------------------------

%package dev
Summary: dev components for the perl-Want package.
Group: Development
Provides: perl-Want-devel = %{version}-%{release}
Requires: perl-Want = %{version}-%{release}

%description dev
dev components for the perl-Want package.


%package perl
Summary: perl components for the perl-Want package.
Group: Default
Requires: perl-Want = %{version}-%{release}

%description perl
perl components for the perl-Want package.


%prep
%setup -q -n Want-0.29
cd %{_builddir}/Want-0.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Want.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Want.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Want/Want.so
