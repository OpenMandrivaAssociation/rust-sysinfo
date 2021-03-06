# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate sysinfo

Name:           rust-%{crate}
Version:        0.11.1
Release:        1%{?dist}
Summary:        Library to get system information such as processes, processors, disks, components and networks

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/sysinfo
Source:         %{crates_source}
# Initial patched metadata
# * No Windows deps
Patch0:         sysinfo-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to get system information such as processes, processors, disks,
components and networks.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+c-interface-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+c-interface-devel %{_description}

This package contains library source intended for building other packages
which use "c-interface" feature of "%{crate}" crate.

%files       -n %{name}+c-interface-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Feb 10 22:04:53 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 08 23:58:50 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.0-1
- Update to 0.11.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 19:57:32 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.5-1
- Update to 0.10.5

* Mon Jan 06 08:24:39 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.4-1
- Update to 0.10.4

* Sat Dec 21 01:11:12 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.3-1
- Update to 0.10.3

* Fri Dec 13 18:40:36 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.2-2
- Enable tests

* Thu Dec 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.2-1
- Update to 0.10.2

* Mon Nov 25 07:57:54 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.6-1
- Initial package
