%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Validate_IE
Summary:	%{_pearname} - Validation class for Ireland
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawność dla Irlandii
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	64799a491718cdbda3afcaef194e52b5
URL:		http://pear.php.net/package/Validate_IE/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Validate_Finance >= 0.5.4
Obsoletes:	php-pear-Validate_IE-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains validation for Irish credentials:
 - PostalCodes (hoax)
 - Passport Numbers
 - Phone Numbers
 - Bank Account Numbers
 - swift codes
 - IBAN codes
 - Drivers Licence Numbers
 - PPSN / SSN Numbers
 - Swift numbers

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Irlandii danych takich jak:
 - kod pocztowy (plotka),
 - numer paszportu,
 - numer telefonu,
 - numer konta bankowego,
 - kod swift,
 - kod IBAN,
 - numer prawa jazdy,
 - numery PPSN / SSN,
 - numery swift

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/IE.php