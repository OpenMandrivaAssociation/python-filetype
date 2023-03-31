%global pypi_name filetype

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        3
Summary:        Infer file type and MIME type of any file/buffer

License:        MIT
URL:            https://github.com/h2non/filetype.py
Source0:        %{url}/archive/v%{version}/%{pypi_name}.py-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pytest

%{?python_provide:%python_provide python3-%{pypi_name}}

BuildArch:      noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.


%prep
%setup -q -n %{pypi_name}.py-%{version}
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py

%build
%py_build

%install
%py_install
rm -rf %{buildroot}%{python_sitelib}/examples

%files
%doc README.rst History.md examples
%license LICENSE
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py*.egg-info
