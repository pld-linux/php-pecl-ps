%define		modname	ps
%define		status	stable
Summary:	%{modname} - an extension to create PostScript files
Summary(pl.UTF-8):	%{modname} - rozszerzenie do tworzenia plików PostScript
Name:		php-pecl-%{modname}
Version:	1.3.6
Release:	5
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	256c5cc3877b03b67963896b84fef306
URL:		http://pecl.php.net/package/ps/
BuildRequires:	php-devel >= 4:5.0.4
BuildRequires:	pslib-devel
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ps is an extension similar to the pdf extension but for creating
PostScript files. Its API is modelled after the pdf extension.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
ps jest rozszerzeniem podobnym do pdf ale służącym do tworzenia plików
PostScript. API jest wzorowane na rozszerzeniu pdf.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir},%{_examplesdir}/%{name}-%{version}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
%{_examplesdir}/%{name}-%{version}
