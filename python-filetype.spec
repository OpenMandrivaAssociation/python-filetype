%global pypi_name filetype

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        1%{?dist}
Summary:        Infer file type and MIME type of any file/buffer

License:        MIT
URL:            https://github.com/h2non/filetype.py
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Buildrequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%prep
%setup -q -n %{pypi_name}.py-%{version}
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/examples

%check
pytest-%{python3_version} -v tests --ignore tests/test_benchmark.py

%files -n python3-%{pypi_name}
%doc README.rst History.md examples
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
