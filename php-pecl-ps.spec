%define		_modname	ps
%define		_status		stable

Summary:	%{_modname} - an extension to create PostScript files
Summary(pl):	%{_modname} - rozszerzenie do tworzenia plików PostScript
Name:		php-pecl-%{_modname}
Version:	1.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	f70d7ae14155c3f4ee9fd0a18b0337d3
URL:		http://pecl.php.net/package/ps/
BuildRequires:	libtool
BuildRequires:	php-devel
BuildRequires:	pslib-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
ps is an extension similar to the pdf extension but for creating
PostScript files. Its api is modelled after the pdf extension.

In PECL status of this package is: %{_status}.

%description -l pl
ps jest rozszerzeniem podobnym do pdf ale s³u¿±cym do tworzenia plików
PostScript. Api jest wzorowany na rozszerzeniu pdf.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,examples}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
