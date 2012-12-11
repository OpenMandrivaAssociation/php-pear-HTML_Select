%define		_class		HTML
%define		_subclass	Select
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.0
Release:	%mkrel 4
Summary:	Class for generating HTML form select elements
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Select
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
HTML_Select provides an OOP way of generating HTML form select elements.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-4mdv2012.0
+ Revision: 742002
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3
+ Revision: 679353
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 613679
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 508989
- update to new version 1.3.0

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-10mdv2010.1
+ Revision: 478092
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-9mdv2010.0
+ Revision: 446486
- rebuild for missing binary

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-8mdv2010.0
+ Revision: 441178
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-7mdv2009.1
+ Revision: 322120
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdv2009.0
+ Revision: 236879
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2008.1
+ Revision: 171040
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-4mdv2008.0
+ Revision: 78154
- fix URL, and stop obsoleting itself

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-3mdv2008.0
+ Revision: 77684
- rebuild


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-2mdv2007.1
+ Revision: 121035
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2007.0
+ Revision: 81657
- Import php-pear-HTML_Select

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2007.0
- first mdv release

