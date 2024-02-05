%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     ayaneo-platform
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux drivers for AYANEO x86 handhelds providing RGB control. 
License:  GPLv3
URL:      https://github.com/KyleGospo/ayaneo-platform

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux drivers for AYANEO x86 handhelds providing RGB control.

%prep
%setup -q -c %{name}-main

%files
%doc %{name}-main/README.md
%license %{name}-main/LICENSE

%changelog
{{{ git_dir_changelog }}}
