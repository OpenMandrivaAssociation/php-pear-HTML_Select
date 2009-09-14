%define		_class		HTML
%define		_subclass	Select
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	%mkrel 8
Summary:	Class for generating HTML form select elements
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/HTML_Select
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
HTML_Select provides an OOP way of generating HTML form select elements.

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/pear/%{_class}

install %{_pearname}-%{version}/Select.php %{buildroot}%{_datadir}/pear/%{_class}

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{_pearname}.xml
